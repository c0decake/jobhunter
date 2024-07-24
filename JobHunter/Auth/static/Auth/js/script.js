$(document).ready(function() {
        $('#phone_number').mask('+7(999) 999-9999');
    });
const post_input = document.getElementById('post_input');

inputElement.type = 'select';

const maskedInput = document.getElementById('phone_number');
    let savedValue = '';

    maskedInput.addEventListener('click', function() {
      // Получаем текущее значение поля
      const currentValue = maskedInput.value;

      // Находим индекс последнего непустого символа
      let lastIndex = currentValue.length - 1;
      console.log(currentValue[lastIndex]);
      while (lastIndex >= 0 && (currentValue[lastIndex] === ' ' || currentValue[lastIndex] === '(' || currentValue[lastIndex] === ')' || currentValue[lastIndex] === '-')) {
        lastIndex--;
      }

      // Перемещаем курсор в конец маски
      maskedInput.setSelectionRange(currentValue.length, currentValue.length);
    });

    maskedInput.addEventListener('blur', function() {
      // Сохраняем значение в буфер обмена
      savedValue = maskedInput.value;
    });

    maskedInput.addEventListener('focus', function() {
      // Восстанавливаем значение из буфера обмена
      maskedInput.value = savedValue;
    });
