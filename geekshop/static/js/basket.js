window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let elem = event.target;
        $.ajax({
            url: "/baskets/edit/" + elem.name + "/" + elem.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result)
                console.log(data)
            },
        })
        console.log(elem.name, elem.value)


    });
    event.preventDefault();
}