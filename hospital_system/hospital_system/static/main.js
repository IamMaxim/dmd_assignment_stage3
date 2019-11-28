window.onload = function () {

};

table_entry_template = `
<tr>
    <td>$1</td>
    <td>$2</td>
</tr>`;

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

    let p_id = $('#fq_name').val();
    let first_letter = $('#fq_fl').val();
    let second_letter = $('#fq_sl').val();

    performRequest(`SELECT * FROM first_query(${p_id}, '${first_letter}', '${second_letter}')`,
        (msg) => {
            let obj = JSON.parse(msg);
            appendMessage('first_query_log', 'Possible doctors: ' + obj.join(', '));
        })
}

function doSecondRequest() {
    appendMessage('second_query_log', 'Going to execute the second request...');
    performRequest("SELECT * FROM second_query()",
        (msg) => {
            let obj = JSON.parse(msg);
            // appendMessage('second_query_log', obj);
            // console.log(obj);

            let body = $('#sq_table_body');
            body.empty();
            obj.forEach(e => {
                body.append(
                    table_entry_template
                        .replace('$1', e[0])
                        .replace('$2', e[1])
                )
            });
        })
}

function doThirdRequest() {
    appendMessage('third_query_log', 'Going to execute the third request...');
    performRequest("SELECT * FROM third_query()",
        (msg) => {
            let obj = JSON.parse(msg);

            // appendMessage('third_query_log', msg);

            appendMessage('third_query_log', 'Patients who have visited hospital at least twice a week:<br>    ' + obj.map(e => "SSN: " + e[3] + '; Name: ' + e[4]).join('<br>    '));
        })
}

function doFourthRequest() {
    appendMessage('fourth_query_log', 'Going to execute the fourth request...');
    performRequest("SELECT * FROM fourth_query()",
        (msg) => {
            let obj = JSON.parse(msg);

            // appendMessage('fourth_query_log', msg)

            appendMessage('fourth_query_log', 'Projected income is ' + obj[0]);
        })
}

function doFifthRequest() {
    appendMessage('fifth_query_log', 'Going to execute the fifth request...');
    performRequest("SELECT * FROM fifth_query()",
        (msg) => {
            let obj = JSON.parse(msg);

            appendMessage('fifth_query_log', 'Experienced doctors:<br>    ' + obj.map(e => "License ID: " + e[4] + '; Name: ' + e[3]).join('<br>    '));
        })
}
