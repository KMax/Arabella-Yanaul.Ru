/**
 * @author Maxim Kolchin
 */
$(document).ready(function(){
	$("div.buttons").click(function(){
		if($(this).parent().children("div .more").css('display') == "none"){
			$(this).find("a").html("Свернуть");
		}else{
			$(this).find("a").html("Развернуть");
		}
		$(this).parent().children("div .more").slideToggle("fast");
	})
})
