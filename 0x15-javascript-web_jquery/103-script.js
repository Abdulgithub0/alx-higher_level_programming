$(document).ready(function () {
  $('INPUT#btn_translate').bind('click keypress', function (event) {
    const lan = $('INPUT#language_code').val();
    if ((event.type === 'keypress' && event.which === 13) || (event.type === 'click')) {
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/' + '?lang=' + lan,
        success: function (data) {
          $('DIV#hello').html(data.hello);
        }
      });
    }
  });
});
