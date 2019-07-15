var bt = document.querySelector('input[id="tsne_heat"]');
function jsFun(){
    if(bt.value=="Tsne"){
        bt.value="Heat";
        document.getElementById("dataviz-container").style.display="none";
        document.getElementById("heatmap").style.display="";
    }
    else if(bt.value=="Heat"){
        bt.value="Tsne";
        document.getElementById("dataviz-container").style.display="";
        document.getElementById("heatmap").style.display="none";
    }
}
