$(document).ready(function () {
  $('DIV#add_item').bind('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').bind('click', function () {
    const list = $('li');
    $(list[list.length - 1]).remove();
  });
  $('DIV#clear_list').bind('click', function () {
    $('li').remove();
  });
});
