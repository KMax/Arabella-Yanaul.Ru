
$(document).ready(function(){
    $("#service_list li + ul").css('display','none');
    $("#service_list nav > ul > li").mouseenter(function(){
        $(this).next().show();
    });
    $("#service_list a").click(loadDesc);
});

var services = new Array();

function loadDesc(event){
    var place = $("#service_des");
    place.html("<h2>Загрузка. Пожалуйста подождите...</h2>");
    if(services[event.target.href]){
        place.html(json_to_html(services[event.target.href]));
    }else{
        $.getJSON(
                ''+event.target.href,
                function(data){
                    services[event.target.href] = data;
                    place.html(json_to_html(services[event.target.href]));
                }
        );
    }
    return false;
}

function json_to_html(data){
    var temp = "<h1>"+data.section+"</h1>" +
            "<h2>"+data.title+"</h2>" +
            "<p>"+data.description+"</p>" +
            "<section>" +
                "<h2>Цены</h2>" +
                "<ul>";
    $.each(data.prices,function(index, value){
        temp+= "<li><p>"+value.title+"</p><p>"+value.price+"</p></li>";
    });
    temp +="</ul></section>";
    return temp;
}