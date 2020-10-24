const url = "http://127.0.0.1:5000/get_list";
const infoUrl = "/get_file/";

$.get(url, function (data) {
    $("#counter").append(data["counter"]);

    const name = data["file_list"];
    for(let i=0; i<name.length; i++){
        $("#list").append("<li><a href='" + infoUrl + name[i] + "'>" + name[i] + "</a></li>");
    }
});
