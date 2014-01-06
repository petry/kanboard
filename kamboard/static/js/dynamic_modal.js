$('body').on('click', 'a[data-toggle="modal"]', function (e) {
    var action = $(this).attr('data-href');
    $.ajax({
        url: action,
        type: "GET",
        success: function (response) {
            $('<div class="modal fade"></div>').html(response).modal();
        }
    });
    e.preventDefault();
});

$('body').on('hidden.bs.modal', '.modal', function () {
    $(this).remove();
});