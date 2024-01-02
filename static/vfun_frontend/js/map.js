function sportshalls_map_init(map, options) {
    // default view -- Dublin
    map.setView([53.349804, -6.260310], 10);

    const sportshalls = JSON.parse(document.getElementById('sportshalls-data').textContent)

    if (!navigator.geolocation) {
        for (const [key, hall] of Object.entries(sportshalls)) {
            const point = [hall.location.coordinates[1], hall.location.coordinates[0]];
            L.marker(point).addTo(map).on('click', function() {
                $('#hallcollapse' + hall.id).collapse('show');
            });
        }
    } else {
        let routingControl = null;

        let addRoutingControl = function(waypoints) {
            if (routingControl != null)
                removeRoutingControl();

            routingControl = L.Routing.control({
                waypoints: waypoints,
                fitSelectedRoutes: true,
            }).addTo(map);
        }

        let removeRoutingControl = function() {
            if (routingControl != null) {
                map.removeControl(routingControl);
                routingControl = null;
            }
        }

        navigator.geolocation.getCurrentPosition(async function (position) {
            let lat = position.coords.latitude;
            let lon = position.coords.longitude;

            L.circleMarker([lat, lon], {
                stroke: false,
                color: 'red',
                radius: position.coords.accuracy,
            }).addTo(map);

            L.circle([lat, lon], {
                fill: true,
            }).addTo(map);

            map.flyTo([lat, lon], 15);

            for (const [key, hall] of Object.entries(sportshalls)) {
                const point = [hall.location.coordinates[1], hall.location.coordinates[0]];
                L.marker(point).addTo(map).on('click', function(e) {
                    $('#hallcollapse' + hall.id).collapse('show');
                    addRoutingControl([L.latLng(lat, lon), e.latlng]);
                });
            }

            $('.hall-card').on('click', function () {
                let hallLoc = $(this).data().point;
                let cardBodyId = $(this).data().target.slice(1);
                let cardBodyElement = document.getElementById(cardBodyId);

                if (!cardBodyElement.classList.contains("show")) {
                    addRoutingControl([L.latLng(lat, lon), L.latLng(hallLoc[1], hallLoc[0])]);
                } else {
                    removeRoutingControl();
                    map.flyTo([lat, lon], 15);
                }
            })
        });
    }
}


function manage_sportshalls_map_init(map, options) {
    // default view -- Dublin
    map.setView([53.349804, -6.260310], 10);

    const sportshalls = JSON.parse(document.getElementById('mysportshalls-data').textContent)

    for (const [key, hall] of Object.entries(sportshalls)) {
        const point = [hall.location.coordinates[1], hall.location.coordinates[0]];
        L.marker(point).addTo(map);
    }

    $('.hall-detail-btn').on('click', function () {
        let hallLoc = $(this).data().point;
        map.flyTo([hallLoc[1], hallLoc[0]], 15);

        let hallId = $(this).data().id;
        const hall = sportshalls[hallId];

        let container = document.getElementById('sportshall-container');
        container.innerHTML = '';

        let redirectUrl = 'http://127.0.0.1:8000/mysportshalls/';

        let hallForm = document.createElement('div');
        hallForm.className = 'form-content';
        hallForm.innerHTML = `<form>
                                <div class="form-group row">
                                    <label for="hallName" class="col-sm-2 col-form-label">Name</label>
                                    <div class="col-sm-10">
                                        <input class="form-control" type="text" id="hallName" placeholder="${hall.name}">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="hallAddress" class="col-sm-2 col-form-label">Address</label>
                                    <div class="col-sm-10">
                                        <input class="form-control" type="text" id="hallAddress" placeholder="${hall.address}">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="hallCourts" class="col-sm-2 col-form-label">Courts</label>
                                    <div class="col-sm-10">
                                        <input class="form-control" type="text" id="hallCourts" placeholder="${hall.courts}">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <label for="hallPhone" class="col-sm-2 col-form-label">Phone No.</label>
                                    <div class="col-sm-10">
                                        <input class="form-control" type="text" id="hallPhone" placeholder="${hall.phone_no}">
                                    </div>
                                </div>
                                <br>
                                <div class="form-group row">
                                    <div class="col-6 d-flex align-items-center">
                                        <button type="submit" class="btn btn-success btn-lg">Save Changes</button>
                                    </div>
                                    <div class="col-3 d-flex align-items-center">
                                        <button class="btn btn-danger btn-lg">Delete</button>
                                    </div>
                                    <div class="col-3 d-flex align-items-center">
                                        <a role="button" class="btn btn-dark btn-lg" href="${redirectUrl}">Back</a>
                                    </div>
                                </div>
                               </form>`

        container.appendChild(hallForm);
    });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
