const databaseQuery = function (){
    let data;
    let innerDataDate = '';
    let innerDataTemp = '';
    let innerDataHumidity = '';
    $.getJSON('/dhtreadings', (res)=>{
        data = res;
        for (let i = 0; i<data.length; i++){
                innerDataDate += '<li class="list-group-item">'+ data[i].Date + '</li>'+'\n';
                innerDataTemp += '<li class="list-group-item">'+ data[i].Temperature + '</li>'+'\n';
                innerDataHumidity += '<li class="list-group-item">'+ data[i].Humidity + '</li>'+'\n';
        }
        document.getElementById("datefield").innerHTML=innerDataDate;
        document.getElementById("tempfield").innerHTML=innerDataTemp;
        document.getElementById("humidityfield").innerHTML=innerDataHumidity;
    });

    
}

