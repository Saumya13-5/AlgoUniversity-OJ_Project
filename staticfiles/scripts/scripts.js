document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('compilerForm').addEventListener('submit', async function (event) {
        event.preventDefault();

        const code = document.getElementById('code').value;
        const language = document.getElementById('language').value;
        const userInput = document.getElementById('input').value;

        const response = await fetch('/run_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ code, language, input: userInput })
        });

        const result = await response.json();
        if (result.success) {
            document.getElementById('output').value = result.output;
        } else {
            document.getElementById('output').value = 'Error: ' + result.message;
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
