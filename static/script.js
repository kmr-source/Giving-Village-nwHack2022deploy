let geocoder;
let map;

function init() {
    geocoder = new google.maps.Geocoder();
    const center = {lat: 40.731, lng: -73.997};
    map = new google.maps.Map(document.getElementById("map"), {
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
}

function placeMarkers(data, getContent) {
    let marker;
    let infoWindow;

    for (let i = 0; i < data.length; i++) {
        let contentString = getContent(data[i]);

        geocoder.geocode({'address': data[i].location}, function(results, status) {
            if (status == "OK") {
                let latLng = results[0].geometry.location;
                marker = new google.maps.Marker({
                    position: new google.maps.LatLng(latLng.lat(), latLng.lng()),
                    map: map,
                    title: data[i].name
                });
                marker.setMap(map);
            } else {
                let defaultLatLng = {lat: 40.731, lng: -73.997};
                marker = new google.maps.Marker({
                    position: new google.maps.LatLng(defaultLatLng.lat, defaultLatLng.lng),
                    map: map,
                    title: data[i].name
                });
                marker.setMap(map);
            }

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
        });
    }
}

function fridgeContentString(data) {
    console.log(data.description);
    return `
        <div id="content">
        <h4>${data.name}</h4>
        <b>Description:</b> ${data.description} <br/>
        <b>Open:</b> ${data.hrs} <br/>
        <b>Additional Info:</b> ${data.fridge_info} <br/>
        </div>
    `
}

function initFridge(data) {
    init();
    placeMarkers(data.fridges, fridgeContentString);
}

