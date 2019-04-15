$(function () {

    $('.more-button').hover(function () {
        $(this).find('i').addClass('hover');
    }, function () {
        $(this).find('i').removeClass('hover');
    });

    $('#sign_up').click(function () {
        $(this).toggleClass('active');
        if ($(this).hasClass('active'))
            $('#sign_up_window').show();
        else
            $('#sign_up_window').hide();
    })

});
