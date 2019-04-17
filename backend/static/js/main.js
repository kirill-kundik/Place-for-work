$(function () {

    $('.more-button').hover(function () {
        $(this).find('i').addClass('hover');
    }, function () {
        $(this).find('i').removeClass('hover');
    });

    $('#sign_up').click(function () {
        $(this).toggleClass('active');
        if ($(this).hasClass('active')) {

            if ($('#sign_in').hasClass('active'))
                $('#close_sign_in').click();

            $('#sign_up_window').show();


        } else
            $('#sign_up_window').hide();
    });

    $('#sign_in').click(function () {
        $(this).toggleClass('active');
        if ($(this).hasClass('active')) {

            if ($('#sign_up').hasClass('active'))
                $('#close_sign_up').click();


            $('#sign_in_window').show();
        } else
            $('#sign_in_window').hide();

    });

    $('#close_sign_in').click(function () {
        $('#sign_in_window').hide();
        $('#sign_in').removeClass('active')
    });

    $('#close_sign_up').click(function () {
        $('#sign_up_window').hide();
        $('#sign_up').removeClass('active')
    })

});
