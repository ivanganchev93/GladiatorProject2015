$(document).ready(function() {

    //Called if equip id is clicked, equipping the item with particular id
    $('.equip').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/equip_item/", {item_id: itemid}, function(data){
            $('#all_items').html(data);
        });
    });

    //Called if unequip id is clicked, unequipping the item with particular id
    $('.unequip').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/unequip_item/", {item_id: itemid}, function(data){
            $('#all_items').html(data);
        });
    });

    //Called if unequip id is clicked, unequipping the item with particular id in the market template
    $('.unequip_market').click(function(){
        var itemid = $(this).attr("data-itemid");
        $.get("/Spartacus/unequip_item_market/", {item_id: itemid}, function(data) {
            $('#all_items_market').html(data);

        });
    });

    //Called if sell id is clicked, sell the item with particular id
    $('.sell').click(function(){
        var itemid = $(this).attr("data-itemid");

        $.get("/Spartacus/sell_item/", {item_id: itemid}, function(data){
            $('#all_items_market').html(data);
            console.log("sell ITEM");
            $.get("/Spartacus/gold/",{item_id: itemid}, function(data){
                $('#gold').html(data);
            });
        });
    });




});