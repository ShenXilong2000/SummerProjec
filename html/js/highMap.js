var chart;

chart = Highcharts.chart('container1', {
	chart: {
		type: 'heatmap',
		// marginTop: 40,
		// marginBottom: 80,
		plotBorderWidth: 1,
	},
	title: {
		text: null
	},
	xAxis: {
		categories: ['RW', 'ISRW', 'RN', 'RJ', 'RE', 'TIES', 'BFS', 'DFS'],
	},
	yAxis: {
		categories: null,
		title: null
	},
	colorAxis: {
		min: 0,
		minColor: '#FFFFFF',
		maxColor: '#32A287',
		// maxColor: Highcharts.getOptions().colors[7]
	},
	legend: {
		align: 'right',
		layout: 'vertical',
		margin: 0,
		verticalAlign: 'top',
		y: 25,
		symbolHeight: 280
	},
	tooltip: {
		enabled:false
	},
	series: [{
		borderWidth: 1,
		
		data: [[0, 0, 10], [0, 1, 100], [0, 2, 8], [0, 3, 24], [0, 4, 67], [1, 0, 92], [1, 1, 58], [1, 2, 78],
			   [1, 3, 17], [1, 4, 48], [2, 0, 35], [2, 1, 15], [2, 2, 13], [2, 3, 64], [2, 4, 52], [3, 0, 72], 
			   [3, 1, 12], [3, 2, 14], [3, 3, 19], [3, 4, 16], [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 17],
			   [4, 4, 15], [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 12], [6, 0, 13], [6, 1, 44], 
			   [6, 2, 88], [6, 3, 98], [6, 4, 96], [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30], 
		],
	}],

	// plotOptions: {
	// 	series: {
	// 		cursor: 'pointer',
	// 		events: {
	// 			click: function(e) {
	// 				console.log(
	// 					// Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', e.xAxis.value), 
	// 					yAxis
	// 				)
	// 			},
	// 		}
	// 	}
	// },
});
document.getElementsByClassName('highcharts-credits')[0].style.display="none";
// document.getElementsByClassName('highcharts-axis-labels highcharts-yaxis-labels')[0].style.display="none";

// console.log(chart.series);
// while (chart.series.length > 0) {
// 	chart.series[0].remove(true);
// }
// console.log("asdasds");