// Initialize the chart variable
let myDonutChart;

// Function to create or update the donut chart
function createOrUpdateDonutChart(data) {
    const ctx = document.getElementById('myDonutChart').getContext('2d');

    if (myDonutChart) {
        // Update existing chart
        console.log('Updating existing chart...');
        myDonutChart.data.datasets[0].data = data; // Update the data
        myDonutChart.update();  // Redraw the chart with the new data
    } else {
        // Create a new chart
        console.log('Creating a new chart...');
        myDonutChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Win', 'Loss/Draw'],
                datasets: [{
                    label: 'Match Winning Chances',
                    data: data, // Initialize with data from the response
                    backgroundColor: [
                        'rgba(212, 237, 218, 1)', // Light green for Win
                        'rgba(238, 238, 238, 1)'
                    ],
                    borderColor: [
                        'rgba(40, 167, 69, 1)', // Vibrant green for win
                        'rgba(238, 238, 238, 1)'
                    ],
                    borderWidth: 1,
                    hoverOffset: 2
                }]
            },
            options: {
                responsive: true,
                animation: {
                    animateScale: false,
                    animateRotate: true
                },
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            font: {
                                size: 16 // Adjust this value to increase the legend label size
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return tooltipItem.label + ': ' + tooltipItem.raw + '%'; // Display value on hover
                            }
                        },
                        titleFont: {
                            size: 16 // Adjust this value to increase the tooltip title size
                        },
                        bodyFont: {
                            size: 14 // Adjust this value to increase the tooltip body label size
                        }
                    }
                },
                cutout: '75%', // Set the cutout percentage to control the width of the donut
            }
        });
    }
}
