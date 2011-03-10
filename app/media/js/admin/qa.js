/**
 * Created by .
 * User: Maxim Kolchin
 * Date: 19.02.11
 * Time: 0:00
 */

$(function() {
    /**
     * Установка обработчика клика на кнопке действия над отзывом
     */
    $("table#reviews tr td#action a[action=delete]").live("click",function() {
        delete_review($(this));
        return false;
    });
    $("table#reviews tr:has(td[id])").live("click",function() {
        show_review($(this))
    });

    /**
     * Установка обработчика события наведения мышки на строку списка отзывов
     */
    $("table#reviews tr:has(td[id])").live("mouseover mouseout", function(){
        $(this).toggleClass("mouseover");
    })

    /**
     * Установка обработчика клика на поле в меню
     */
    $("aside#menu nav a").click(function(){ action_tab($(this)) });
})

/**
 *
 * @param obj
 */
function delete_review(obj){
    var row = obj.closest("tr");
    var id = row.find("td[id]:first").text();
    var showArea = $("table#reviews tr:has(td[id="+id+"]) + tr.show td");

    if (confirm("Вы уверены что хотите удалить отзыв №" + id + "?")) {
        showArea.hide();
        row.hide();
        $.post('qa/delete/', 'id='+id, function(data,textStatus) {
                
        });
    }
}

/**
 *
 * @param obj
 */
function show_review(obj){
    var row = obj.closest("tr");
    var id = row.find("td[id]:first").text();
    var showArea = $("table#reviews tr:has(td[id="+id+"]) + tr.show td");

    //Проверяем скачали ли мы уже текст отзыва
    if(showArea.length){
        //Если да, то скрываем или показываем поле вывода
        showArea.parent().toggle();
    }else{
        //Если нет, то скачиваем
        row.after("<tr class='show'><td colspan='5'></td></tr>");
        showArea = $("table#reviews tr:has(td[id="+id+"]) + tr.show td")
                .css("display", "none");
        $.post('qa/show/', 'id='+id, function(data) {
            
                showArea.show('fast').text(data.text);
        });
    }
}

/**
 * Преобразует JSON-объект отзыва, в HTML элемент tr, который не содержит текст
 * отзыва
 * @param obj
 */
function json_to_html_review(obj){
    return "<tr>"+
                "<td id='id'>"+obj.id+"</td>"+
                "<td>"+obj.owner_name+"</td>"+
                "<td>"+obj.date+"</td>"+
                "<td>"+obj.owner_email+"</td>"+
                "<td id='action'>" +
                    "|<a action='delete' href='#reviews'>удалить</a>|" +
                "</td>" +
            "</tr>"
}

/**
 * Отправляет POST-запрос по адресу {uri}, в ответ сервер посылает массив
 * JSON-объектов, каждый элемент которого обрабатывается функцией {func} и
 * вставляется в конец элемента {obj}.
 * @param uri
 * @param obj
 * @param func
 */
function get_and_put_review(uri,obj,func){
    $.post(uri, null, function(data, textStatus){
                $.each(data, function(key,val){
                    obj.append(func(val))
                })
            },'json');
}

/**
 * 
 * @param tab
 */
function action_tab(tab){
    $("nav#menu_qa a").removeClass("selected");
    tab.addClass("selected");

    var href = tab.attr("href");
    var area = $("table#reviews tbody");

    area.find("tr").remove();

    if(href == "#unanswered"){
        get_and_put_review('qa/show/unanswered/',area,json_to_html_review);
    }
    if(href == "#all"){
        get_and_put_review('qa/show/all/',area,json_to_html_review);
    }
    if(href == "#complaint"){
        get_and_put_review('qa/show/complaint/',area,json_to_html_review);
    }
    if(href == "#supply"){
        get_and_put_review('qa/show/supply/',area,json_to_html_review);
    }
    if(href == "#question"){
        get_and_put_review('qa/show/question/',area,json_to_html_review);
    }
}