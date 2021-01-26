// event listener to handle dropdown menu
function optionChanged(subject_id) {
    var subject_id = d3.select("#selDataset").node().value;
    // barFunc
    barFunction(subject_id)
    // bubbleFunc
    // metadataFunc
};

// InitFunction
function initialize(subject_id) {
    var dropdown = d3.select("#selDataset")
    
    // Fill dropdown
    d3.json("samples.json").then((data) => {   
        // grab samples
        var sampleData = data.samples
    
        // create array of sample IDs
        var ids = sampleData.map(sample => sample.id)
    
        // fill drp down bar w/ subject IDs
        ids.forEach(id => {
            var option = dropdown.append("option").text(`BB_${id}`)
            option.node().value = id
        });
    })

    // barFunc
    barFunction("940");
    // bubbleFunc
    // metadataFunc
};


// Bar
function barFunction(subject_id){
    console.log(subject_id)
};

// Bubble
function bubbleFunction(subject_id){
    console.log(subject_id)
};

// Meta
function metadataFunction(subject_id){
    console.log(subject_id)
};

// initialzie page
initialize();