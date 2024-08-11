from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from compiler.views import run_code
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .models import Problem, Testcase

@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk = problem_id )
    if request.method == 'POST':
        action = request.POST.get('action')
        language = request.POST.get('language')
        code = request.POST.get('code')

        if action == 'run':
            input_data = request.POST.get('input_data')
            output = run_code(language, code, input_data)
            return JsonResponse({'output': output})
        
        if action == 'submit':
            testcases = Testcase.objects.filter(problem = problem)
            passed_count = 0
            total_count = testcases.count()
            output = 0
            for testcase in testcases:
                input_data = testcase.input
                expected_output = testcase.expected_output
                actual_output = run_code(language,code,input_data)
                if actual_output.strip() == expected_output.strip():
                    passed_count += 1
                output = expected_output
            verdict = 'Accepted' if passed_count == total_count else 'Rejected'
            return JsonResponse({'verdict': verdict, 'passed_count': passed_count, 'total_count': total_count})
    return render(request, 'Problemset/problem_detail.html', {'problem': problem})


def custom_logout_view(request):
    logout(request)
    return render(request, 'users/welcome.html') 