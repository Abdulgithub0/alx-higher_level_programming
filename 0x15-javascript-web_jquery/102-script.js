$(document).ready(function () {
  $('INPUT#btn_translate').bind('click', function () {
    const lan = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + '?lang=' + lan,
      success: function (data) {
        $('DIV#hello').html(data.hello);
      }
    });
  });
});
