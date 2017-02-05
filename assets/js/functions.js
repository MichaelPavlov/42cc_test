function showLoadingScreen() {
    $("body").append("<div class='loading-overlay'><div class='loader'></div></div>");
}

function hideLoadingScreen() {
    $(".loading-overlay").remove()
}

function disableForm() {
    $("#contact-edit-form").find(":input").each(function () {
        $(this).attr('disabled', 'disabled');
    });
}

function enableForm() {
    $("#contact-edit-form").find(":input").each(function () {
        $(this).removeAttr('disabled');
    });
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function renderRequestStamps(data) {
    var currentStampIDs = [];
    var tableContents;
    var newStamps = 0;
    data.forEach(function (stamp) {
        currentStampIDs.push(stamp.pk);
        var td = `<td>${stamp.pk}</td><td>${stamp.fields.path}</td><td>${stamp.fields.method}</td><td>${stamp.fields.ip}</td>`;
        var tr;
        if (stamp.fields.new) {
            tr = `<tr class="active">${td}</tr>`;
            newStamps++;
        } else {
            tr = `<tr>${td}</tr>`;
        }
        tableContents += tr;
    });

    if (newStamps > 0) {
        document.title = document.title.replace(/^\(\d+\)\ /i, "");
        document.title = `(${newStamps}) ` + document.title;
    }

    if (!arraysEqual(window.cachedStamps, currentStampIDs)) {
        $("#requests-table").html(tableContents);
        window.cachedStamps = currentStampIDs;
    }
}


function submitContactEditForm() {
    $("#contact-edit-form").submit()
    data = {
        "first_name": $("#first_name"),
        "last_name": $("#v"),
        "birth_date": $("#birth_date"),
        "photo": $("#photo"),
        "email": $("#email"),
        "jabber": $("#jabber"),
        "skype": $("#skype"),
        "other_contacts": $("#other_contacts"),
        "bio": $("#bio")
    };

    $.ajax({
        'method': "post",
        'url': editContactSubmitURL,
        'data': data,
        'success': function (data) {
            console.log(data)
        },
        'error': function (err) {
//            console.log(method, url, err);
            console.log(err.responseText);
        }
    })
}

function markRequestsAsRead() {
    document.title = document.title.replace(/^\(\d+\)\ /i, "");
    data = {
        "requests": window.cachedStamps
    };
    ajax("POST", markRequestsReadUrl, data, function () {
        $("#requests-table").children().removeClass('active');
    })
}

function arraysEqual(arr1, arr2) {
    if (arr1 == undefined ||
        arr2 == undefined ||
        arr1.constructor !== Array ||
        arr2.constructor !== Array
    ) return false;

    return (arr1.length == arr2.length) && arr1.every(function (element, index) {
            return element === arr2[index];
        });
}

function ajax(method, url, data, success) {
    $.ajax({
        'method': method,
        'url': url,
        'data': data,
        'success': function (data) {
            success(data)
        },
        'error': function (err) {
//            console.log(method, url, err);
            console.log(err.responseText);
        },
        headers: {
            "X_CSRFTOKEN": csrftoken
        }
    })
}

var csrftoken = getCookie('csrf_token');
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X_CSRFTOKEN", csrftoken);
        }
    }
});