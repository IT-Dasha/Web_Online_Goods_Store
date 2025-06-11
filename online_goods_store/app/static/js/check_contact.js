    const checkbox = document.getElementById('checkbox_contact');
    const button = document.getElementById('button_contact');
    const surnameInput = document.getElementById('surname');
    const nameInput = document.getElementById('name');
    const patronymicInput = document.getElementById('patronymic');
    const phoneInput = document.getElementById('phone');
    const passwordInput = document.getElementById('password');
    const adress = document.getElementById('adress');

    checkbox.addEventListener('change', function() {
        if (checkbox.checked & surnameInput.value !== '' & nameInput.value !== '' & patronymicInput.value !== '' & phoneInput.value !== '' & passwordInput.value !== '' & adress.value !== '') {
button.style.pointerEvents = 'auto';
        } else {
          button.style.pointerEvents = 'none';
        }
    });