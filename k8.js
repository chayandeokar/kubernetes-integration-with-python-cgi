function kube_op() {
    
    var cmd =  document.getElementById("fname").value 

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://192.168.1.9/cgi-bin/kube.py?x=" + cmd, true);
    document.getElementById("outputwindow").innerHTML = '<div class="loader"></div>';
    xhr.send()
    xhr.onload = function () {
        document.getElementById("outputwindow").innerHTML = xhr.responseText;
    }
}
