
function sendPostRequest(url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            var responseData = JSON.parse(xhr.responseText);
            callback(null, responseData);
        } else {
            callback("Request failed with status: " + xhr.status, null);
        }
    };

    xhr.onerror = function () {
        callback("Request failed", null);
    };

    var jsonData = JSON.stringify(data);
    xhr.send(jsonData);
}

var apiUrl = "http://10.131.60.27:8080/registration";
var requestData = { name: "afsaff", lastname: "lastname", email: "volkov_av07@mail.ru", password: "dsafsaf"  };

sendPostRequest(apiUrl, requestData, function (error, responseData) {
    if (error) {
        console.error(error);
    } else {
        console.log(responseData);
    }
});
