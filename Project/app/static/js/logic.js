$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePrediction();
    });
});


// call Flask API endpoint
function makePredictions() {
    let gender = $("#gender").val();
    let customer_type = $("#customer_type")
    let age = $("#age").val();
    let travel_type = $("#travel_type").val();
    let travel_class = $("#travel_class").val();
    let distance = $("#distance").val();
    let wifi = $("#wifi").val();
    let time_convenience = $("#time_convenience").val();
    let booking = $("#booking").val();
    let gate = $("#gate").val();
    let food = $("#food").val();
    let boarding = $("#boarding").val();
    let comfort = $("#comfort").val();
    let entertainment = $("#entertainment").val();
    let onboard_service = $("#onboard_service").val();
    let legroom = $("#legroom").val();
    let baggage = $("#baggage").val();
    let checkin_service = $("#checkin_service").val();
    let inflight_service = $("#inflight_service").val();
    let cleanliness = $("#cleanliness").val();
    let delay_d = $("#delay_d").val();
    let delay_a= $("#delay_a").val();

    // check if inputs are valid

    // create the payload
    var payload = {
        "gender": gender,
        "customer_type": customer_type,
        "age": age,
        "travel_type": travel_type,
        "travel_class": travel_class,
        "distance": distance,
        "wifi": wifi,
        "time_convenience": time_convenience, 
        "booking": booking,
        "gate": gate,
        "food": food,
        "boarding": boarding,
        "comfort": comfort,
        "entertainment": entertainment,
        "onboard_service": onboard_service,
        "legroom": legroom,
        "baggage": baggage, 
        "checkin_service": checkin_service, 
        "inflight_service": inflight_service,
        "cleanliness": cleanliness,
        "delay_d": delay_d,
        "delay_a": delay_a
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`This customer is likely satisfied with a satisfaction probability of ${prob}.`);
            } else {
                $("#output").text(`This customer is likely neutral or dissatisfied with a satisfaction probability of ${prob}.`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

