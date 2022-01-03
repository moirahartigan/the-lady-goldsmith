let countrySelected = $('#id_default_country').val();
if(!countrySelected) {  // if country selected is false.Then we want the colour of this element to be that grey placeholder colour
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {  // capture the change event
    countrySelected = $(this).val();  // and every time the box changes we'll get the value of it.
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');  // then determine the proper colour
    } else {
        $(this).css('color', '#000');
    }
});