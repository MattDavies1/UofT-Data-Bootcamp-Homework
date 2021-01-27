// event listener to handle dropdown menu selection
function optionChanged(subject_id) {
    var subject_id = d3.select("#selDataset").node().value;
    // barFunc
    barFunction(subject_id)
    // bubbleFunc
    bubbleFunction(subject_id)
    // metadataFunc
    metadataFunction(subject_id)
    //guage
    guageFunction(subject_id)
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

    // populate page with object functions
    // barFunc
    barFunction("940");
    // bubbleFunc
    bubbleFunction("940");
    // metadataFunc
    metadataFunction("940");
    // guageFunction
    guageFunction("940");
};


// Bar
function barFunction(subject_id){
    // load json file
    d3.json("samples.json").then((data) => {
        var allSamples = data.samples
        var matched = allSamples.filter(obj => {
            return obj.id === subject_id
        })
        var otu_ids = matched[0].otu_ids.slice(0,10)
        var sample_values = matched[0].sample_values.slice(0,10)
        var labels = matched[0].otu_labels.slice(0,10)

        barTrace = {
            y:otu_ids,
            x:sample_values,
            text:labels,
            type: "bar",
            orientation: 'h'
        }

        data = [barTrace];

        layout = {
            title:"10 most abundant OTUs",
            'xaxis': {
                title:"sample value"
            },
            'yaxis': {
                title:"OTU id",
                'type': 'category'
            }
        };

        Plotly.newPlot("bar", data, layout)

    })
};

// Bubble
function bubbleFunction(subject_id){
    // load json file
    d3.json("samples.json").then((data) => {
        var allSamples = data.samples
        var matched = allSamples.filter(obj => {
            return obj.id === subject_id
        })
        var otu_ids = matched[0].otu_ids.slice(0,10)
        var sample_values = matched[0].sample_values.slice(0,10)
        var labels = matched[0].otu_labels.slice(0,10)

        bubbleTrace = {
            x: otu_ids,
            y: sample_values,
            mode: "markers",
            marker: {
                size: sample_values
            },
            text:labels
        };

        dataBubble = [bubbleTrace];

        layoutBubble = {
            title:"10 most abundant OTUs",
            'xaxis': {
                title:"sample value"
            },
            'yaxis': {
                title:"OTU id",
            }
        };

        Plotly.newPlot("bubble", dataBubble, layoutBubble)
    })
    
};

// Meta
function metadataFunction(subject_id){
    d3.json("samples.json").then((data) => {
        d3.selectAll("p").remove()
        var demoData = data.metadata
        var matched = demoData.filter(obj => {
            return obj.id == subject_id
        })
        Object.entries(matched[0]).forEach(([key, value]) => {
            d3.select("#sample-metadata").append("p").text(`${key} : ${value}`)
            
        })
        
    })
    
};

function guageFunction(subject_id){
    // load json file
    d3.json("samples.json").then((data) => {
        var demoData = data.metadata
        var matched = demoData.filter(obj => {
            return obj.id == subject_id
        })
        console.log(matched)
        var wfreq = matched[0].wfreq

        var data = [
            {
              type: "indicator",
              mode: "gauge+number",
              value: wfreq,
              title: { text: "Washing Frequency", font: { size: 24 } },
              gauge: {
                axis: { range: [null, 9], tickwidth: 2, tickcolor: "black" },
                bar: { color: "green" },
                bgcolor: "white",
                borderwidth: 2,
                bordercolor: "gray",
                steps: [
                  { range: [0, 7], color: "white" },
                  { range: [7, 9], color: "lightgreen" }
                ]
              }
            }
          ];
          
        var layout = {
          };
          
        Plotly.newPlot('gauge', data, layout);

    })
};

// initialzie page
initialize();
