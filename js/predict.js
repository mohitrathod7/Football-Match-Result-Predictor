$(document).ready(function() {
    $('#prediction-form').on('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission

        $.ajax({
            type: 'POST',
            url: '/',  // The URL for the form submission
            data: $(this).serialize(),  // Serialize form data
            success: function(response) {
                // Update the prediction result on the page
                if (response.error) {
                    $('#prediction-result').html('<p>Error: ' + response.error + '</p>');
                } else {
                    $('#prediction-result').html(
                        '<p>Winning chances: <span>' + response.win_probability + '%</span></p>'
                    );

                    // Prepare data for the chart
                    const winProbability = response.win_probability;  // Assuming this is a percentage
                    const lossProbability = 100 - winProbability;

                    // Create or update the donut chart only after loading overlay is hidden
                    createOrUpdateDonutChart([winProbability, lossProbability]);
                }
            },
            error: function(xhr) {
                // Show error message
                $('#prediction-result').html('<p>Error: ' + xhr.responseText + '</p>');
            }
        });
    });
});
