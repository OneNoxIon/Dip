function deleteAllCookies() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
    console.log('deleteallcookie')
    window.location.replace('/logins')
}


function deleteTasks() {
    var element = document.getElementById("tasks");
    element.parentNode.removeChild(element);
    var element = document.getElementById("tasks");
    if (element) {
        deleteTasks();
    } else {
        console.log("deletetasks");
    }
}


function FindFIO() {
    fetch('/profile')
}