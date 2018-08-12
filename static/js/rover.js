document.onkeydown = function(e) {
    console.log(typeof(e))
    if(e.keyCode == 37){
        $.getJSON('/left',
        function() {
        //do nothing
    });
    }
    if(e.keyCode == 38){
        $.getJSON('/forward',
        function() {
        //do nothing
    });
    }

    if(e.keyCode == 39){
        $.getJSON('/right',
        function() {
        //do nothing
    });
    }

    if(e.keyCode == 40){
        $.getJSON('/back',
        function() {
        //do nothing
    });
    }

    if(e.keyCode == 32){
        $.getJSON('/wait',
        function(){

        });
    }
};
