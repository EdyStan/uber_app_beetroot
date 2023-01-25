var start_lat = 0.0
var start_lon = 0.0
var end_lat = 0.0
var end_lon = 0.0

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
    bounds.extend(start);
    bounds.extend(end);
    addPin(start, map, "►");
    addPin(end, map, "◼︎");
}

function addPin(location, map, label) {
    var marker = new google.maps.Marker({
        position: location,
        map: map,
        label: {
           text: label,
           fontSize: "16px",
           color: "#ffdddd",
           fontFamily: "montserrat"
        }
     });
}
  
window.initMap = initMap;