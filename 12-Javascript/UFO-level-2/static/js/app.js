// from data.js
var tableData = data;

// select button
var button = d3.select("#filter-btn");

// detect inputs
var form = d3.select("#datetime");

// select table body for data insert
var tbody = d3.select("tbody");

// event handelers
button.on("click", multiFilter)
form.on("submit", multiFilter)

function multiFilter() {

    // prevend auto-refresh
    d3.event.preventDefault();

    var dateFilter = d3.select("#datetime").node().value
    var cityFilter = d3.select("#city").node().value
    var stateFilter = d3.select("#state").node().value
    var countryFilter = d3.select("#country").node().value
    var shapeFilter = d3.select("#shape").node().value
    // Date
    if (dateFilter != ""){var filtered1 = tableData.filter(event => event.datetime == dateFilter)}
    else {var filtered1 = tableData}
    // City
    if (cityFilter != ""){var filtered2 = filtered1.filter(event => event.city == cityFilter)}
    else {var filtered2 = filtered1}
    // State
    if (stateFilter != ""){var filtered3 = filtered2.filter(event => event.state == stateFilter)}
    else {var filtered3 = filtered2}
    // Country
    if (countryFilter != ""){var filtered4 = filtered3.filter(event => event.country == countryFilter)}
    else {var filtered4 = filtered3}
    // Shape
    if (shapeFilter != "default"){var filtered5 = filtered4.filter(event => event.shape == shapeFilter)}
    else {var filtered5 = filtered4}

    // clear data in table
    d3.selectAll("td").remove()

    // insert filtered data
    filtered5.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
};

// init function to add every variable to the table on page load
data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
