/**
 * Created by .
 * User: Maxim Kolchin
 * Date: 19.02.11
 * Time: 0:00
 */


$(function(){
    //Обработка действия
    $("table#reviews tr td#action a").click(function(){action($(this).attr("action"))})
})

//Обработчик действий над отзывами
function action(action){
    if(action==="show"){

    }if(action=="delete"){
        deleteReview()
    }
}