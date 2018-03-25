window.onload = function() {

  console.log('controller')

  var date = document.getElementById('date').innerHTML;
  var location = document.getElementById('posted').innerHTML;
  var high_temp = document.getElementById('high_temp').innerHTML;
  var low_temp = document.getElementById('low_temp').innerHTML;
  var summary = document.getElementById('summary').innerHTML;
  var precipitation = document.getElementById('precipitation').innerHTML;

  document.getElementById('id_date').value = date;
  document.getElementById('id_date_res').value = date;
  document.getElementById('id_location').value = location;
  document.getElementById('id_high_temp').value = high_temp;
  document.getElementById('id_low_temp').value = low_temp;
  document.getElementById('id_summary').value = summary;
  document.getElementById('id_precipitation').value = precipitation;

  console.log('values set')

  /* skeleton data object */
  var chartData = {
    labels: [],
    datasets: [
      {
        label: 'High Temps',
        data: [],
        backgroundColor: 'rgb(255, 99, 89)',
        borderColor: 'rgb(255, 99, 132)',
      },
      {
        label: 'Low Temps',
        data: [],
        backgroundColor: 'rgb(89, 99, 255)',
        borderColor: 'rgb(200, 200, 240)',
      },
      {
        label: 'Precipitation',
        data: [],
        backgroundColor: 'rgb(210, 236, 232)',
        borderColor: 'rgb(156, 188, 174)',
        yAxisID: 'precipYAxis',
      },
    ]
  }

  var tab = document.getElementById("tab");
  for (var i = 1, row; row = tab.rows[i]; i++) {
      chartData['labels'][i-1] = row.cells[0].innerHTML + row.cells[1].innerHTML;
      chartData['datasets'][0]['data'][i-1] = row.cells[2].innerHTML;
      chartData['datasets'][1]['data'][i-1] = row.cells[3].innerHTML;
      chartData['datasets'][2]['data'][i-1] = row.cells[4].innerHTML;
  }

  console.log('chartdata: ' + chartData['datasets'][0]['data'])

  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: {
          legend: {
            position: 'top'
          },
          scales: {
              yAxes: [{
                scaleLabel: {
                  display: true,
                  labelString: 'Temperature (\xBAC)',
                },
                ticks: {
                    beginAtZero:true
                }
              }, {
                id: 'precipYAxis',
                scaleLabel: {
                  display: true,
                  labelString: 'Precipitation (\")',
                },
                position: 'right',
                ticks: {
                  beginAtZero:true
                },
                gridLines: {
                  display: false,
                }
              },]
          }
      }
  });

  document.getElementById("exportButton").onclick = function() {
    csvExport();
  }

}
