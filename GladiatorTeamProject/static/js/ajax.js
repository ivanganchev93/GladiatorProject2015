$(document).ready(function() {
    
    $('.equip').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/equip_item/", {item_id: itemid}, function(data){
            $('#all_items').html(data);
        });
    });

    $('.unequip').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/unequip_item/", {item_id: itemid}, function(data){
            $('#all_items').html(data);
        });
    });
	


});