document.addEventListener("DOMContentLoaded", function () {
  var rows = document.getElementById("result_list").getElementsByTagName("tr");
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var cssClass = row.getAttribute("class");
    if (cssClass.indexOf("red") !== -1) {
      row.style.backgroundColor = "#ffcccc"; // Light red
    } else if (cssClass.indexOf("green") !== -1) {
      row.style.backgroundColor = "#ccffcc"; // Light green
    }
  }
});
