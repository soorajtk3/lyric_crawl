function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artist',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list += '<li class="list-box">' + element.name + '</li>';
      });
      tag = `<ul>${list}<ul/>`;
      $('div.artist').html(tag);
      console.log(data);
    },
  });
}
$(main);
