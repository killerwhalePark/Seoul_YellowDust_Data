


document.querySelector("#cellSizeSlider").addEventListener("input", (e) => {
  var val = parseInt(e.target.value);
  var date_label = document.getElementById("DateText");

  date_label.innerHTML = air_data;

});