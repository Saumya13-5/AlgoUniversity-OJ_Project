document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');

    if (registerForm) {
        registerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('registerUsername').value;
            const email = document.getElementById('registerEmail').value;
            const password = document.getElementById('registerPassword').value;

            if (username === '' || email === '' || password === '') {
                showError('All fields are required.');
            } else {
                const response = await fetch('/register/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const result = await response.json();
                if (!result.success) {
                    showError(result.message);
                } else {
                    showPopup('Registration Successful!');
                    window.location.href = '/login/';
                }
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('loginUsername').value;
            const password = document.getElementById('loginPassword').value;

            if (username === '' || password === '') {
                showError('All fields are required.');
            } else {
                const response = await fetch('/login/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });
                const result = await response.json();
                if (!result.success) {
                    showError(result.message);
                } else {
                    showPopup('Login Successful!');
                    window.location.href = result.redirect_url;
                }
            }
        });
    }

    function showError(message) {
        const errorMessageElement = document.getElementById('error-message');
        errorMessageElement.textContent = message;
    }

    function showPopup(message) {
        alert(message);  // Basic alert popup, you can use more stylish popups like Bootstrap modal, SweetAlert, etc.
    }
});
