function initMap() {
  latitude = document.getElementById("latitude").innerHTML;
  longitude = document.getElementById("longitude").innerHTML;
  console.log("lat long" + latitude + " " + longitude)
  /* + character converts strings to floats for Google Maps API */
  var mark = {lat: +latitude, lng: +longitude};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: mark
  });
  var marker = new google.maps.Marker({
    position: mark,
    map: map
  });
}
