function getForecast() {
    city = $("#city_search").val()
    $.get( "/forecast/"+city, function( data ) {
        box = $("#forecast");
        box.empty();

        data['data'].forEach(entry => {
            box.append("<div class='card'><h5 class='card-header'>Vorhersage für: "+entry['date']+
            "</h5><div class='card-body'><div class='row row-cols-2'><div class='col'>Sonne:<h3>"+
            entry['sunrise']+" - "+entry['sunset']+"</h3> </div><div class='col'>Temperatur: <h3>"+
            entry['lowest_temperature']+"°C bis "+entry['highest_temperature']+"°C</h3></div></div></div></div>")
        });
    });
}