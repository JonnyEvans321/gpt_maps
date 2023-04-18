// Declare the map variable globally
let map;

// Load the map
function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('map-container'), {
        credentials: bingApiKey,
        center: new Microsoft.Maps.Location(0, 0),
        mapTypeId: Microsoft.Maps.MapTypeId.road,
        zoom: 2,
    });
}

// Function to add markers to the map
function addMarkers(coords) {
    // Clear existing map markers
    map.entities.clear();

    // Create an array to store Microsoft.Maps.Location objects
    const locations = [];

    // Add new markers
    coords.forEach(function (coord) {
        const latitude = coord['latitude'];
        const longitude = coord['longitude'];
        const label = coord['label'];

        const location = new Microsoft.Maps.Location(latitude, longitude);
        const pushpin = new Microsoft.Maps.Pushpin(location, {title: label});
        map.entities.push(pushpin);
        locations.push(location);
        
    });

    // Adjust map view to fit all markers
    const bounds = Microsoft.Maps.LocationRect.fromLocations(locations);
    map.setView({ bounds: bounds, padding: 20 });
}

function plotCoordinates(description) {
    console.log('Plotting coordinates for real');
    $("#plotting").show();
    try {
        $.post("/plot_coordinates", { description: description }, function(data) {
            console.log(data);

            // Get the list of coordinates and add markers to the map
            addMarkers(data);
            $("#plotting").hide();
        });
    } catch (error) {
        // If parsing fails, display an error message
        $("#plotting").hide();
        alert("Error while creating valid coordinates. Please try again.");
    }
}




$(document).ready(function() {
    $("#input-form").submit(function(event) {
        event.preventDefault();
        var userInput = $("#user-input").val();

        if (userInput) {
            // Show the loading message
            $("#loading").show();
            
            $.post("/", { user_input: userInput }, function(data) {
                // Hide the loading message
                $("#loading").hide();
                
                // Save the generated description in session storage
                sessionStorage.setItem("generatedText", data);

                // Redirect to the response page
                window.location.href = '/response';
            });
        }
    });

    $('#home-button').click(function(event) {
        event.preventDefault();
        console.log('Home button clicked!');
        window.location.href = '/';
    });

    // Check if the description textarea exists and the session storage has the "generatedText" item
    if ($("#description").length && sessionStorage.getItem("generatedText")) {
        // Get the description from session storage and set it to the textarea
        var description = sessionStorage.getItem("generatedText");
        $("#description").val(description);

        // Plot the coordinates using the description
        plotCoordinates(description);
    }

    $('#plot-coordinates').click(function(event) {
        event.preventDefault();
        console.log('Plotting coordinates');
        var currentDescription = $("#description").val();
        plotCoordinates(currentDescription);
    });
});
