/**
 * Created by charm-beauty.ru.
 * User: Maxim Kolchin
 * Date: 08.06.11
 * Time: 15:43
 */

$(document).ready(function(){
    $('.pred').click(function(){
        loadPhoto($(this).attr('id'));
    });
    $('.next').click(function(){
        loadPhoto($(this).attr('id'));
    });
    $('a.origin_image[rel="gallery"]').colorbox({
        transition: 'none',
        width: "75%",
        speed: 300,
        opacity: 0.7,
        close: 'закрыть',
        next: 'след',
        previous: 'пред',
        current: ' ({current} из {total})'
            });
});

function loadPhoto(id){
    $.post('photo/'+id,
            {
                id: id
            },
            function(data){
                $('#gallery p').text(data.name);
                $('#gallery img').attr({'id':data.id,'src':data.url});
                $('.pred').attr('id',data.id-1);
                $('.next').attr('id',data.id+1);
            }
    );
}