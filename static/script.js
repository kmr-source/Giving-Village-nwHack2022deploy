initMap();

function initMap() {
    const center = {lat: 40.731, lng: -73.997};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: center
    });

    const infoWindow = new google.maps.InfoWindow();

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent("Location found.");
            infoWindow.open(map);
            map.setCenter(pos);
        },
            () => {
                console.log("Someting went wrong!");
            });
    }
}