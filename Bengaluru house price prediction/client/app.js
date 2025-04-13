function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) {
      return parseInt(uiBathrooms[i].value); // Corrected to return value instead of index
    }
  }
  return -1; // Invalid value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i = 0; i < uiBHK.length; i++) {
    if (uiBHK[i].checked) {
      return parseInt(uiBHK[i].value); // Corrected to return value instead of index
    }
  }
  return -1; // Invalid value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");

  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // Check if all fields have valid values before making the API call
  if (bhk === -1 || bathrooms === -1 || location.value === "" || isNaN(sqft.value) || parseFloat(sqft.value) <= 0) {
    alert("Please provide valid inputs for all fields.");
    return; // Exit the function if inputs are invalid
  }

  var url = "http://127.0.0.1:8000/predict_home_price"; // Use this if you are NOT using nginx

  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" +  data.estimated_price.toFixed(2)+ " Lakh</h2>";
    console.log(status);
  });
}

function onPageLoad() {
  console.log("document loaded");

  var url = "http://127.0.0.1:8000/get_location_names"; // Use this if you are NOT using nginx

  $.get(url, function(data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
