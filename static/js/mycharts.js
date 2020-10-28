$(document).ready(function () {
    // Load google charts
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);
    
});


// Draw the chart and set the chart values
function drawChart() {
    var exp_data = $('#txt_data').val(), idx = 0;
    var tdata = [['Description', 'Expenditure']];
    exp_data = JSON.parse(exp_data);
    for(idx= 0; idx < exp_data.length; idx++){
        tmp_data = JSON.parse(exp_data[idx]);
        for (const [key, value] of Object.entries(tmp_data)) {
            tdata.push([key, value]);
        };
    };
    
    console.log(typeof tdata);
    console.log(tdata);
    var data = google.visualization.arrayToDataTable(tdata);

    // Optional; add a title and set the width and height of the chart
    var options = { 'title': 'Household Expenditure in 2019', 'width': 550, 'height': 400 };

    // Display the chart inside the <div> element with id="piechart"
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}