function initMap() {
    const center = {lat: 40.731, lng: -73.997};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: center
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            };
            map.setCenter(pos);
        },
            () => {
                console.log("Someting went wrong!");
            });
    }

    let marker;
    let infoWindow;
    let locations = [
        {name: "Kensington Pantry", lat: 49.275440467796386, lng: -123.1119283030811, type: "Fridge"},
        {name: "Women's Shelter", lat: 49.28333290043626, lng: -123.10237964365506, type: "Shelter"}
    ];

    for (let i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
            map: map,
            title: locations[i].name
        });

        (function(marker, i) {
            google.maps.event.addListener(marker, "click", () => {
                if (infoWindow) {
                    infoWindow.close();
                }
                infoWindow = new google.maps.InfoWindow({
                    title: locations[i].name,
                    content: locations[i].type
                });
                infoWindow.open({
                    map,
                    anchor: marker,
                    shouldFocus: true,
                });
                map.panTo(marker.getPosition());
            });
        })(marker, i);
    }
}

initMap();