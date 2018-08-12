const forcedb = function (){
    $.getJSON('/forcedb',(data)=>{
            console.log(data);
    });
}

setInterval('forcedb', 10000);