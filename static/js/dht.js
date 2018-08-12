function timed(){
    $.getJSON('/dhtdata', (data)=>{
    gauge.set(data["Temperature"]); // set actual value
    gauge.setTextField(document.getElementById("preview-textfield"));
    gauge1.set(data["Humidity"]); // set actual value
    gauge1.setTextField(document.getElementById("preview-textfield1"));
    })
}

setInterval(timed, 20000);