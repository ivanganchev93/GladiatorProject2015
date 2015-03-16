$(document).ready(function() {
    
    $('.item').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/equip_item/", {item_id: itemid}, function(data){
            $('#all_items').html(data);
        });
    });
});