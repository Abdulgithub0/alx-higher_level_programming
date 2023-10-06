$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (data) {
    const movies = data.results;
    $.each(movies, function (index, ele) {
      const li = `<li>${ele.title}</li>`;
      $('UL#list_movies').append(li);
    });
  }
});
