$(document).ready(function () {
    // 1. Переменные - флаги результатов валидации:
    let res1 = false;
    let res2 = false;
    let res3 = false;
    let res4 = false;

    // 2. Валидация логина:
    $('#login').blur(function () {
        let loginX = $('#login').val(); // возвращает велью
        let loginR = /^[a-zA-z]+[a-zA-z0-9_]{5,15}$/;
        if (loginR.test(loginX)) {
            // проверка занятости логина
            $.ajax({
                url: '/account/ajax_reg', // обычный новый юрл для любой страницы
                data: 'login=' + loginX,
                success: function (result) { // ответ сервера
                    if (result.message === 'Логин занят') {
                        $('#login-err').text('Логин занят, введите другой')
                        res1 = false;
                    } else {
                        res1 = true
                        $('#login-err').text('')
                    }
                }
            });
        } else {
            $('#login-err').text('Логин неправильный!')
            res1 = false;
        }
    })

    // 3. Валидация первого пароля
    $('#pass1').blur(function () {
        let pass1X = $('#pass1').val(); // возвращает велью
        let pass1R = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-z0-9_]{8,}$/;
        if (pass1R.test(pass1X)) {
            $('#pass1-err').text('')
            res2 = true;
        } else {
            res2 = false;
            $('#pass1-err').text('Пароль неправильный!')
        }
    })

    // 4. Валидация второго пароля
    $('#pass2').blur(function () {
        let pass1X = $('#pass1').val(); // возвращает велью
        let pass2X = $('#pass2').val(); // возвращает велью
        if (pass1X === pass2X) {
            $('#pass2-err').text('')
            res3 = true;
        } else {
            res3 = false;
            $('#pass2-err').text('Пароли не совпадают!')
        }
    })

    // 5. Валидация email
    $('#email').blur(function () {
        let emailX = $('#email').val(); // возвращает велью
        let emailR = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailR.test(emailX)) {
            $('#email-err').text('')
            res4 = true;
        } else {
            res4 = false;
            $('#email-err').text('Email неправильный!')
        }
    })

    $('#submit').click(function () {
        // 6. Финальная проверка:
        if (res1 && res2 && res3 && res4) {
            $('#form-1').attr('onsubmit', 'return true'); // разблокировка формы
        } else {
            $('#form-1').attr('onsubmit', 'return false'); // переблокировка формы
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!')
        }
    });
});