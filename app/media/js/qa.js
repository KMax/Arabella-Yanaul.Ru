/**
 * User: Maxim Kolchin
 * Date: 20.12.2010
 * Time: 19:28:00
 */

//Функия выполнится в момент полной готовности DOM-модели документа
$(function(){
    $("section#module_content ul li").click(function(){
        $(this).find("div#answer").toggle();
    })

    //Отправка отзыва
    $("div a.add").click(function(){
                            add_review($(this).attr("id"))
                        })
})

function add_review(type){
    var form = $("<div id='dialog-form' title='Добавить отзыв'>"+
	"<p class='validateTips'>Все поля должны быть заполнены.</p>"+
	    "<form>"+
            "<fieldset>"+
                "<label for='name'>Имя</label>"+
                "<input type='text' name='name' id='name'/>"+
                "<label for='email'>Емайл</label>"+
                "<input type='email' name='email' id='email' value=''/>"+
                "<label for='question'>Вопрос</label>"+
                "<textarea name='question' id='question' value=''/>"+
            "</fieldset>"+
	    "</form>"+
    "</div>")

    var progressbar = $("<div id='progressbar'></div>")

    var name = $("input#name", form),
        email = $("input#email",form),
        question = $("textarea#question",form)

    form.dialog(
            {
                autoOpen: false,
                height: 300,
                width: 300,
                modal: true,
                buttons: {
                    "Отправить": function(){
                        $.post("/qa/add/",
                                { name: name.val(), email: email.val(), review: question.val(), type: type},
                                function(data){
                                    alert(data)
                                })
                        $(this).dialog("close")
                    },
                    "Отменить": function(){
                        $(this).dialog("close")
                    }
                }
            }
            );
    form.dialog("open")
    return false
}