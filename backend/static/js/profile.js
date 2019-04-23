$(function () {

    function hideBlocks() {
        $('.button').each(function () {
            $(this).removeClass('active')
        });
        $('.form-handler').each(function () {
            $(this).hide().removeClass('active');
        });
    }

    $('#profile_preview').click(function () {

        hideBlocks();
        $(this).addClass('active');
        $('#profile_previewing').addClass('active').show();
    });

    $('#profile_edit').click(function () {

        hideBlocks();
        $(this).addClass('active');

        $('#profile_editing').addClass('active').show();

    });

    $('#resume_preview').click(function () {

        hideBlocks();
        $(this).addClass('active');
        $('#resume_container').addClass('active').show();
    });

});