$(function () {

    $('section.register .button-handler button').click(function () {
        if ($(this).hasClass('active'))
            return;
        $('section.register .button-handler button').each(function () {
            $(this).removeClass('active')
        });

        $(this).addClass('active');

        let notNeededForm = $('section.register .form-handler:not(.active)');
        $('section.register .form-handler').each(function () {
            $(this).removeClass('active');
            $(this).hide()
        });

        notNeededForm.addClass('active');
        notNeededForm.show()

    })

});