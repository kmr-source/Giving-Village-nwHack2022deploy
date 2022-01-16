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

    return map;
}

function placeMarkers(map, data, getContent) {
    let marker;
    let infoWindow;
    let locations = [
        {name: "Kensington Pantry", lat: 49.275440467796386, lng: -123.1119283030811, type: "Fridge"},
        {name: "Women's Shelter", lat: 49.28333290043626, lng: -123.10237964365506, type: "Shelter"}
    ];

    for (let i = 0; i < locations.length; i++) {
        // let contentString = getContent(data);

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
                    content: contentString
                });
                infoWindow.open({
                    map,
                    anchor: marker,
                    shouldFocus: false,
                });
                map.panTo(marker.getPosition());
            });
        })(marker, i);
    }
}

function fridgeContentString(data) {
    return `
        <div id="content">
        <h4>${data.name}</h4>
        <p><b>Open:</b> $(data.hrs)</p>
        <p><b>Additional Info:</b> $(data.fridge_info)</p>
        </div>
    `
}

function initFridge(data) {
    let map = initMap();
    placeMarkers(map, data, fridgeContentString);
}

