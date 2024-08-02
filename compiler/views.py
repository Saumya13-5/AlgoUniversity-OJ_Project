from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from django.contrib.auth.decorators import login_required
import tempfile
import os

@login_required
def compile_code(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        code = request.POST.get('code')
        input_data = request.POST.get('input_data')

        # Compile and run the code
        output = run_code(language, code, input_data)

        return JsonResponse({'output': output})

    return render(request, 'compiler/compiler.html')

def run_code(language, code, input_data):
    try:
        if language == 'python':
            with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as source_file:
                source_file.write(code.encode())
                source_file.flush()
                command = f'python {source_file.name}'
                result = subprocess.run(command, input=input_data, capture_output=True, text=True, shell=True, timeout=5)
                
        elif language == 'cpp':
            with tempfile.NamedTemporaryFile(suffix='.cpp', delete=False) as source_file:
                source_file.write(code.encode())
                source_file.flush()
                executable = source_file.name.replace('.cpp', '.exe')
                compile_command = f'g++ {source_file.name} -o {executable}'
                compile_result = subprocess.run(compile_command, shell=True, capture_output=True, text=True)

                if compile_result.returncode != 0:
                    return compile_result.stderr

                command = executable
                result = subprocess.run(command, input=input_data, capture_output=True, text=True, shell=True, timeout=5)
        else:
            return 'Language not supported.'

        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return 'Execution timed out.'
    finally:
        if os.path.exists(source_file.name):
            os.remove(source_file.name)
        if language == 'cpp' and os.path.exists(executable):
            os.remove(executable)

    return 'Error running code.'
