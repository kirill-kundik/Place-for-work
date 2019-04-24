$(function () {

    $('#logo').click(function () {
        location.href = 'http://' + location.host
    });

    $('.more-button').hover(function () {
        $(this).find('i').addClass('hover');
    }, function () {
        $(this).find('i').removeClass('hover');
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
    });

    $('#search_button').click(function () {
        location.href = 'http://' + location.host + '/search?keywords=' + encodeURIComponent($('#search_input').val());
    })

});
