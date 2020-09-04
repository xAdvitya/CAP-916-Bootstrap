$(() => {
    $('[data-toggle="popover"]').popover();
});

$(document).ready(function () {
    $('img').hover(
        function () {
            $(this).animate({ 'zoom': 1.2 }, 400);
        },
        function () {
            $(this).animate({ 'zoom': 1 }, 400);
        });
});