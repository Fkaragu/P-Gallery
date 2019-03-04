function copyUrl() {
  var copyText = document.getElementById("{{img_item.id}}-url");
  copyText.select();
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}
