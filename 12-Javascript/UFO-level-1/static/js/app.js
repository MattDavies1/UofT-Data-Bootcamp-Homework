// from data.js
var tableData = data;

// select button
var button = d3.select("#filter-btn");

// select form
var form = d3.select("#form");

// select table body for data insert
var tbody = d3.select("tbody");

// event handelers
button.on("click", filterFunc);
form.on("submit", filterFunc);

// function to filter table
function filterFunc() {

    // prevend auto-refresh
    d3.event.preventDefault();

    // accept value from input feild
    var inputVal = d3.select("#datetime").node().value

    // create filtered data
    var filteredData = tableData.filter(event => event.datetime == inputVal)

    // clear data in table
    d3.selectAll("td").remove()

    // insert filtered data
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });

    // clear input feild
    d3.select("#datetime").node().value = ""
};

// init function to add every variable to the table on page load
data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
