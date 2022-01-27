/**
 * [Favourites sorting functionality
 * Credit: Code Institute project Boutique Ado ]
 */
$('.btt-link').click(function(e) {
    window.scrollTo(0, 0);
});

$('#myModal').on('shown.bs.modal', function() {
    $('#myInput').trigger('focus');
});