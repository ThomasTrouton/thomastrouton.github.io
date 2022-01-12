!function(exports) {
  exports.submitGoogleForm = submitGoogleForm;
  exports.populateInstagram = populateInstagram;

  function submitGoogleForm(form) {
    try {
      var data = [].slice.call(form).map(function(control) {
        return 'value' in control && control.name ?
          control.name + '=' + (control.value === undefined ? '' : control.value) :
          '';
      }).join('&');
      var xhr = new XMLHttpRequest();

      xhr.open('POST', form.action + '/formResponse', true);
      xhr.setRequestHeader('Accept',
          'application/xml, text/xml, */*; q=0.01');
      xhr.setRequestHeader('Content-type',
          'application/x-www-form-urlencoded; charset=UTF-8');
      xhr.send(data);
    } catch(e) {}

    form.parentNode.className += ' submitted';
    form.reset()
    document.getElementById("sendButton").value = "Sent"
    document.getElementById("sendButton2").value = "Sent"

    return false;
  }

  function populateInstagram(posts) {
    var row = document.getElementById("instagramRow")
    posts.forEach(x => {
      var column = document.createElement("div")
      column.className = "col-lg-2 col-sm-6"
      var link = document.createElement("a")
      link.href = "https://www.instagram.com/p/" + x;
      var image = document.createElement("img");
      image.src = "images/xxs/instagram/" + x + ".webp";
      image.width = "100"
      image.height = "100"
      image.style = "width:100%"
      image.className = "img-fluid mb-3";
      link.appendChild(image);
      column.appendChild(link);
      row.appendChild(column);
    })
  }

}(typeof module === 'undefined' ? window : module.exports);
