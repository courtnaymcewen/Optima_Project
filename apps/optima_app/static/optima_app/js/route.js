function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {
            lat: 41.85,
            lng: -87.65
        }
    });
    directionsDisplay.setMap(map);

    document.getElementById('submit').addEventListener('click', function () {
        calculateAndDisplayRoute(directionsService, directionsDisplay);
    });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var waypts = [];
    var checkboxArray = document.getElementsByClassName('waypoints');
    for (var i = 0; i < checkboxArray.length; i++) {
        var address = checkboxArray[i].value;
        if (address !== '') {
            waypts.push({
                location: address,
                stopover: true
            });
        }
    }

    directionsService.route({
        origin: document.getElementById('start').value,
        destination: document.getElementById('end').value,
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
    }, function (response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
            console.log(response);
            var route = response.routes[0];
            console.log(route.legs[0].distance.value);
            var summaryPanel = document.getElementById('directions-panel');
            summaryPanel.innerHTML = '';
            // For each route, display summary information
            // Added a var to hold the total sum of a route
            var sum = 0;
            for (var i = 0; i < route.legs.length; i++) {
                var routeSegment = i + 1;
                summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
                    '</b><br>';
                summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
                summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
                summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
                // sum calculation                
                sum += route.legs[i].distance.value;

            }
            console.log('route sum', sum);
            //push all locations into an array
            var locations = [document.getElementById('start').value, document.getElementById('end').value]
            console.log(locations);
            for (var i = 0; i < waypts.length; i++) {
                locations.push(waypts.value);
            }
            console.log(locations);
            //get all possible variations of the array
            //plug in each variation into the google api
            //capture the total distance of each variation
            //display the route with the lowest distance to the user

        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}
