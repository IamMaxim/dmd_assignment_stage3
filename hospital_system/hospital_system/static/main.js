window.onload = function () {

};

function performRequest(request, callback) {
    const Http = new XMLHttpRequest();
    const url = '/requests/?query=' + encodeURIComponent(request);
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200)
                callback(Http.responseText);
            else
                console.log('error occurred while performing request: ' + Http.status + ": " + Http.responseText)
        }
    }
}

function appendMessage(textfield_name, message) {
    $(`#${textfield_name}`).append(message + '<br>')
}

function populate() {
    appendMessage('populate_log', 'Going to populate the database...');

}

function doFirstRequest() {
    appendMessage('first_query_log', 'Going to execute the first request...');
    performRequest("SELECT * FROM first_query(0, 'A', 'B')",
        (msg) => appendMessage('first_query_log', msg))
}

function doSecondRequest() {

}

function doThirdRequest() {

}

function doFourthRequest() {

}

function doFifthRequest() {

}
