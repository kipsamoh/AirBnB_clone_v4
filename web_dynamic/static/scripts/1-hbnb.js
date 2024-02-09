$(function () {
  const amenities = {};
  $('div.amenities li input').change(function (){
    if ($(this).is(':checked')) {
      amenities[($(this).attr('data-id'))] = $(this).attr('data-name');
    } else {
      delete amenities[($(this).attr('data-id'))];
    }
    $('div.amenities h4').text(Object.values(amenities).join(', '));
  });
});
