window.onload = function () {
    var _quantity, _price, _orderitem_num, delta_quantity, orderitem_quantity, _delta_cost;
    var quantity_arr = [];
    var price_arr = [];

    var TOTAL_FORMS = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    var order_total_price = parseFloat($('.order_total_cost').text().replace(',', '.'))||0;

    for (var i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price
        } else {
            price_arr[i] = 0
        }
    }
        // console.log(quantity_arr)
        // console.log(price_arr)
    $('.order_form').on('click','input=type[number]', function () {
        
    })
}