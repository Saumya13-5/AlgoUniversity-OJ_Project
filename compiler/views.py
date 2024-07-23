from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from django.contrib.auth.decorators import login_required

@login_required
def compile_code(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        code = request.POST.get('code')
        input_data = request.POST.get('input_data')

        # Save the code snippet (optional)
        # snippet = CodeSnippet.objects.create(language=language, code=code, input_data=input_data)

        # Compile and run the code
        output = run_code(language, code, input_data)

        return JsonResponse({'output': output})

    return render(request, 'compiler/compiler.html')

def run_code(language, code, input_data):
    if language == 'python':
        filename = 'temp.py'
        with open(filename, 'w') as file:
            file.write(code)
        command = f'python {filename}'
    elif language == 'cpp':
        filename = 'temp.cpp'
        with open(filename, 'w') as file:
            file.write(code)
        compile_command = f'g++ {filename} -o temp'
        subprocess.run(compile_command, shell=True)
        command = './temp'
    else:
        return 'Language not supported.'

    try:
        result = subprocess.run(command, input=input_data.encode(), capture_output=True, text=True, shell=True, timeout=5)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return 'Execution timed out.'

    return 'Error running code.'
