$('#pagination-courses').twbsPagination({
        totalPages: $(".course-page").length,
        startPage: 1,
        visiblePages: 8,
        initiateStartPageClick: true,

        href: false,

        first: 'First',
        last: 'Last',

        loop: false,

        onPageClick: function (event, page) {
            $('.course-page').removeClass('active');
            $('#course-page' + (page-1)).addClass('active')
        },

        paginationClass: 'pagination',
        nextClass: 'page-item next',
        prevClass: 'page-item prev',
        lastClass: 'page-item last',
        firstClass: 'page-item first',
        pageClass: 'page-item',
        activeClass: 'active',
        disabledClass: 'disabled',
    })