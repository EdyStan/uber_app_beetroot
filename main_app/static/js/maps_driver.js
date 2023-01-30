var start_lat
var start_lon
var end_lat
var end_lon
var startSvgMarkerConfig
var stopSvgMarkerConfig
var marker;

const startPath = "M -2 12 l 6 -5 l -6 -4 z M 0 0 q 2.906 0 4.945 2.039 t 2.039 4.945 q 0 1.453 -0.727 3.328 t -1.758 3.516 t -2.039 3.07 t -1.711 2.273 l -0.75 0.797 q -0.281 -0.328 -0.75 -0.867 t -1.688 -2.156 t -2.133 -3.141 t -1.664 -3.445 t -0.75 -3.375 q 0 -2.906 2.039 -4.945 t 4.945 -2.039 z"
const stopPath = "M -4 11 l 8 0 l 0 -8 L -4 3 z M 0 0 q 2.906 0 4.945 2.039 t 2.039 4.945 q 0 1.453 -0.727 3.328 t -1.758 3.516 t -2.039 3.07 t -1.711 2.273 l -0.75 0.797 q -0.281 -0.328 -0.75 -0.867 t -1.688 -2.156 t -2.133 -3.141 t -1.664 -3.445 t -0.75 -3.375 q 0 -2.906 2.039 -4.945 t 4.945 -2.039 z"

function setup(start_lat, start_lon, end_lat, end_lon) {
    console.log("SETUP");
    console.log(start_lat);
    console.log(start_lon);
    console.log(end_lat);
    console.log(end_lon);
    this.start_lat = start_lat;
    this.start_lon = start_lon;
    this.end_lat = end_lat;
    this.end_lon = end_lon;
}

function initMap() {
    const myLatLng = { lat: (this.start_lat+this.end_lat)/2.0, lng: (this.start_lon+this.end_lon)/2.0 };
    var bounds = new google.maps.LatLngBounds();
    console.log(myLatLng.lat, myLatLng.lng);

    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: myLatLng,
    });
    console.log("ADD PINS");
    const start = {lat: this.start_lat, lng: this.start_lon};
    const end = {lat: this.end_lat, lng: this.end_lon};
    this.startSvgMarkerConfig = {
        path: startPath,
        fillColor: "red",
        fillOpacity: 0.6,
        strokeWeight: 0,
        rotation: 0,
        scale: 2,
        anchor: new google.maps.Point(0, 20),
      };
    this.stopSvgMarkerConfig = {
        path: stopPath,
        fillColor: "gray",
        fillOpacity: 0.6,
        strokeWeight: 0,
        rotation: 0,
        scale: 2,
        anchor: new google.maps.Point(0, 20),
      };
    bounds.extend(start);
    bounds.extend(end);
    this.startSvgMarker = addPin(start, map, startSvgMarkerConfig);
    this.stopSvgMarker = addPin(end, map, stopSvgMarkerConfig);
    google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
    });
}

function placeMarker(location) {
  if ( marker ) {
    marker.setPosition(location);
  } else {
    console.log("WTF! we must have the marker!!!");
  }

  $("#location").val(location);
}

function select_pin(field) {
    switch (field.id) {
        case "start_location":
            console.log("START LOCATION SELECTED");
            marker = this.startSvgMarker;
        break;
        default:
            console.log("STOP LOCATION SELECTED");
            marker = this.stopSvgMarker;
    }
}

function addPin(location, map, icon) {
    var marker = new google.maps.Marker({
        position: location,
        icon: icon,
        map: map
     });
     return marker
}
  
window.initMap = initMap;