// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

// Arrow function to add every variable to the table
data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

// Add listener for search function
d3.selectAll("#button").on("click", filterFunc)

// function to filter table
function filterFunc() {}