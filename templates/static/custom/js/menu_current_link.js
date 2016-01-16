//This script iterates through all the menu items and toggles the 'active' class to
//the item having the current link. This should work even if the link becomes more complex
$( document ).ready(function() {
    $("#menu li").each( function() {
        var a_children = $(this).children('a');
        var link = a_children.attr('href');
        console.log(link);
        console.log(window.location.pathname);
        if(window.location.pathname.indexOf(link) > -1) {
            $(this).toggleClass('active');
        }
    });
});