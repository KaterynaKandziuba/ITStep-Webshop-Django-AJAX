$(document).ready(function() {
    $('.add-to-cart-btn').click(function() {
        let productId = $(this).prev().val() // берем предыдущий элемент перед кнопкой и достаем его велью
        let userId = $(this).prev().prev().val() // берем предыдущий элемент перед кнопкой и достаем его велью

        if (userId == 'None') {
            alert('Для использования корзины необходимо авторизоваться!');
            window.location = '/account/entry'; // переносит юзера на страничку авторизации
        } else {
            let uid = userId;
            let pid = productId;
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${uid}&pid=${pid}`,
                success: function(result) {
                    alert('Товар успешно добавлен в корзину!');
                    $('#count').text(result.count);
                }
            })
        }
    });
});
// this - отвечает за то, на какую кнопку мы сейчас кликаем
// нам нужно записывать товар для отдельного юзера