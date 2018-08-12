// Initialize and add the map
function initMap() {
  // The location of Kwako
    let gps = {"lat":27.675064, "lon":85.332715};
    var kwako = {lat: gps["lat"], lng: gps["lon"]};
    // The map, centered at Kwako
    var map = new google.maps.Map(
    document.getElementById('map'), {zoom: 18, center: kwako});
    // The marker, positioned at Kwako
    var marker = new google.maps.Marker({position: kwako, map: map});
}

setInterval(function(){
    $.getJSON('/gpsdata',
            function(data) {
                let gps = data;
                var kwako = {lat: gps["lat"], lng: gps["lon"]};
                // The map, centered at Kwako
                var map = new google.maps.Map(
                document.getElementById('map'), {zoom: 18, center: kwako});
                // The marker, positioned at Kwako
                var marker = new google.maps.Marker({position: kwako, map: map});
        });

}, 20000);
