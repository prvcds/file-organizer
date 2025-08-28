// Hardcoded credentials
const VALID_USERNAME = "kalvian@example.com";
const VALID_PASSWORD = "Kalvi@2025";
const MAX_ATTEMPTS = 3;
let attempts = 0;

const loginForm = document.getElementById('loginForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const showPassword = document.getElementById('showPassword');
const loginBtn = document.getElementById('loginBtn');
const messageDiv = document.getElementById('message');

function validateEmail(email) {
	// Simple regex for email validation
	return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
}

function validateInputs() {
	const username = usernameInput.value.trim();
	const password = passwordInput.value;
	if (!username) {
		showMessage('Username is required.');
		return false;
	}
	if (!validateEmail(username)) {
		showMessage('Please enter a valid email address.');
		return false;
	}
	if (!password) {
		showMessage('Password is required.');
		return false;
	}
	showMessage('');
	return true;
}

function showMessage(msg, success = false) {
	messageDiv.textContent = msg;
	messageDiv.className = success ? 'message success' : 'message';
}

usernameInput.addEventListener('input', validateInputs);
passwordInput.addEventListener('input', validateInputs);

showPassword.addEventListener('change', function() {
	passwordInput.type = this.checked ? 'text' : 'password';
});

loginForm.addEventListener('submit', function(e) {
	e.preventDefault();
	loginBtn.disabled = true;
	if (!validateInputs()) {
		loginBtn.disabled = false;
		return;
	}
	const username = usernameInput.value.trim();
	const password = passwordInput.value;
	if (username === VALID_USERNAME && password === VALID_PASSWORD) {
		showMessage('Login successful! Redirecting...', true);
		setTimeout(() => {
			window.location.href = 'success.html';
		}, 1200);
	} else {
		attempts++;
		if (attempts >= MAX_ATTEMPTS) {
			showMessage('Too many failed attempts. Please try again later.');
			loginBtn.disabled = true;
			usernameInput.disabled = true;
			passwordInput.disabled = true;
		} else {
			showMessage(`Invalid credentials. Attempts left: ${MAX_ATTEMPTS - attempts}`);
			loginBtn.disabled = false;
		}
	}
});
