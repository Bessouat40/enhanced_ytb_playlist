


function createChartLegend(chart){

		var div = document.createElement('div');
        div.setAttribute("class","row justify-content-center mt-2")
        for(var i=0; i<chart.data.datasets.length; i++){
            var label = chart.data.datasets[i].label;
            var color = chart.data.datasets[i].borderColor;           		
            var text = `<div class="col-auto">
            <div class="dot row-3" style="background-color: ${color};"></div><span class='mx-1 col-3'>${label}</span>
            </div>`;
            div.innerHTML = div.innerHTML + text
		}
        
        return div;
}


function createLikesChart(canva_name,data,container_name){

        var ctx = document.getElementById(canva_name);
        var color = '#0ec411'
        var color2 ='#FF0000'

        var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data['labels'],
            datasets: [
                {
                    label: "Likes",
                    data: data['values'],
                    lineTension: 0.4,
                    backgroundColor: HexToRGB(color,0), //Area
                    borderColor: color, //line
                    borderWidth: 2,
                    pointRadius: 3.5,
                    pointBackgroundColor: 'white', //Point
                    pointBorderColor: color,
                    pointHoverRadius: 4,
                    pointHoverBackgroundColor: color,
                    pointHoverBorderColor: color,
                    pointHitRadius: 15,

                },
                {
                    label: "Dislikes",
                    data: data['values2'],
                    lineTension: 0.4,
                    backgroundColor: HexToRGB(color2,0), //Area
                    borderColor: color2, //line
                    borderWidth: 2,
                    pointRadius: 3.5,
                    pointBackgroundColor: 'white', //Point
                    pointBorderColor: color2,
                    pointHoverRadius: 4,
                    pointHoverBackgroundColor: color2,
                    pointHoverBorderColor: color2,
                    pointHitRadius: 15,

                }
            ]

        },
        options: {

            scales: {
                    xAxes: [
                      {
                        time: {
                          unit: "date",
                        },
                        gridLines: {
                          display: false,
                          drawBorder: false,
                        },
                        ticks: {maxRotation: 0,minRotation: 0},
                      },
                    ],
                  yAxes: [{
                    ticks: {
                      maxTicksLimit: 8,
                      padding: 1,
                      
                    },
                    gridLines: {
                      color: "rgb(234, 236, 244)",
                      zeroLineColor: "rgb(234, 236, 244)",
                      drawBorder: false,
                }
              }],
             },

            legend: {
                display: false,
                onClick: function(event, legendItem) {},
                position: 'bottom'
  
             },

            legendCallback: function(chart){

                return(createChartLegend(chart))

            },

            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                titleMarginBottom: 10,
                titleFontColor: "#6e707e",
                titleFontSize: 14,
                borderColor: "#dddfeb",
                borderWidth: 0.7,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                intersect: false,
                mode: "index",
                caretPadding: 10,
                
            },
        }
        });

        var container = document.getElementById(container_name);
        div = myLineChart.generateLegend();
        container.appendChild(div)
    
    }

function createViewChart(canva_name,data,container_name){

        var ctx = document.getElementById(canva_name);
        var color = '#f0953c'
        
        var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data['labels'],
            datasets: [
                {
                    label: "Views",
                    data: data['values'],
                    lineTension: 0.4,
                    backgroundColor: HexToRGB(color,0), //Area
                    borderColor: color, //line
                    borderWidth: 2,
                    pointRadius: 3.5,
                    pointBackgroundColor: 'white', //Point
                    pointBorderColor: color,
                    pointHoverRadius: 4,
                    pointHoverBackgroundColor: color,
                    pointHoverBorderColor: color,
                    pointHitRadius: 15,

                },
                
            ]
        },
        options: {
            scales: {
                    xAxes: [
                      {
                        time: {
                          unit: "date",
                        },
                        gridLines: {
                          display: false,
                          drawBorder: false,
                        },
                        ticks: {maxRotation: 0,minRotation: 0},
                      },
                    ],
                  yAxes: [{
                    ticks: {
                      maxTicksLimit: 5,
                      padding: 1 
                    },
                    gridLines: {
                      color: "rgb(234, 236, 244)",
                      zeroLineColor: "rgb(234, 236, 244)",
                      drawBorder: false,
                }
              }],
             },
            legend: {
                display: false,
                onClick: function(event, legendItem) {},
                position: 'bottom',




             },
            legendCallback: function(chart){
                return(createChartLegend(chart))
            },
            
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                titleMarginBottom: 10,
                titleFontColor: "#6e707e",
                titleFontSize: 14,
                borderColor: "#dddfeb",
                borderWidth: 0.7,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                intersect: false,
                mode: "index",
                caretPadding: 10,   
            },
        }
        });

        var container = document.getElementById(container_name);
        div = myLineChart.generateLegend();
        container.appendChild(div)
    
    }