// updates label text of registration form
const emailLabel = document.querySelector('#id_email').previousElementSibling;
emailLabel.innerHTML = 'Email:';
const emailInput = document.querySelector('#id_email')
emailInput.required = true;