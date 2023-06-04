$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (resp, status) {
    if (status === 'success') {
      $('#character').text(resp.name);
    }
  });
});
