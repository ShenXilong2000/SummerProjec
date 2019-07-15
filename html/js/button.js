var bs = document.querySelector('input[id="button-sample"]');
{//数据
    dataconst = 1000;
    var data_5 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.07804998794735474 * dataconst,
              0.051315719402242485 * dataconst,
              0.06193911614193387 * dataconst,
              0.07815066412970847 * dataconst,
              0.07008171305227431 * dataconst,
              0.09218388335478131 * dataconst,
              0.07170914139826061 * dataconst,
              0.08650432224791785 * dataconst]
        ]
     };
     var data_10 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.07751444405033886 * dataconst,
              0.06475198116084226 * dataconst,
              0.05489935676361536 * dataconst,
              0.07181993619994143 * dataconst,
              0.08122590936546883 * dataconst,
              0.07980770920877772 * dataconst,
              0.07016705916472356 * dataconst,
              0.08798537528780445 * dataconst]
        ]
     };
     var data_15 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.08300480747219634 * dataconst,
              0.05927815209464797 * dataconst,
              0.05840568153182214 * dataconst,
              0.07599039366051824 * dataconst,
              0.07754456657813621 * dataconst,
              0.0741749098926448 * dataconst,
              0.0547946079192265 * dataconst,
              0.07872704264446788 * dataconst]
        ]
     };
     var data_20 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.08650432224791785 * dataconst,
              0.07008171305227431 * dataconst,
              0.06193911614193387 * dataconst,
              0.051315719402242485 * dataconst,
              0.07804998794735474 * dataconst,
              0.07815066412970847 * dataconst,
              0.09218388335478131 * dataconst,
              0.07170914139826061 * dataconst]
        ]
     };
     var data_25 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.082659912945247 * dataconst,
              0.06730058276739141 * dataconst,
              0.062165157693053134 * dataconst,
              0.07107566509557756 * dataconst,
              0.07645870783978687 * dataconst,
              0.07335977629945767 * dataconst,
              0.06344549744900864 * dataconst,
              0.08071882106441436 * dataconst]
        ]
     };
     var data_30 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.08432437014670684 * dataconst,
              0.06256835636493795 * dataconst,
              0.06501227246888476 * dataconst,
              0.07584746609429403 * dataconst,
              0.07543323374103729 * dataconst,
              0.06785190209712716 * dataconst,
              0.060802446931975965 * dataconst,
              0.08190955670720974 * dataconst]
        ]
     };
     var data_35 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.07815771870651843 * dataconst,
              0.06557860628574932 * dataconst,
              0.06908642170655367 * dataconst,
              0.07220570304108556 * dataconst,
              0.07363845201117289 * dataconst,
              0.0716600241825136 * dataconst,
              0.05324563891385155 * dataconst,
              0.08259878007307711 * dataconst]
        ]
     };
     var data_40 = {
        fielaNames:['RE','RJ','RN','ISRW','RW','DFS','BFS','TIES'],
        values:[
           [0.08119365235612636 * dataconst,
              0.0673090476358627 * dataconst,
              0.07026681024008176 * dataconst,
              0.07174573977904616 * dataconst,
              0.0712026039469732 * dataconst,
              0.07006002226238398 * dataconst,
              0.05990944603867329 * dataconst,
              0.07765626268173184 * dataconst]
        ]
     };
}
function sampling_func(){
    var elem1 = document.querySelector('input[id="range1"]');
    var nodes = 11174*elem1.value*0.01;
    var edges = 23410*elem1.value*0.01;
    document.getElementById("sampling-nodes").innerText= parseInt(nodes);
    document.getElementById("sampling-edges").innerText= parseInt(edges);
    d3.select("#dataviz-container svg").remove();
    var c = document.getElementsByClassName("heatmap-canvas");
   for(var i=0;i<c.length;i++)
   {
      var cxt=c[i].getContext("2d");  
      c[i].height=c[i].height;       
   }
   var c =document.getElementById("canvas_");
   c.remove();


   //  for(var i in x){
   //    //  i.remove();
   //     console.log(i);
   //    //  i.clearRect(0,0,400,400);
   //  }
   // canvas.heatmap-canvas.clearRect(0,0,400,400);
   // console.log(document.getElementsByClassName("heatmap-canvas"));
   //  d3.select("#heatmap-canvas").remove();


    if(elem1.value == 5)
    {
        drawlineChart(data_5);
        drawRadarChart(data_5);
        rate = "5";
      //   tsne_change(name,rate){
    }
    else if(elem1.value == 10)
    {
        drawlineChart(data_10);
        drawRadarChart(data_10);
        rate = "10";
    }
    else if(elem1.value == 15)
    {
        drawlineChart(data_15);
        drawRadarChart(data_15);
        rate = "15";
    }
    else if(elem1.value == 20)
    {
        drawlineChart(data_20);
        drawRadarChart(data_20);
        rate = "20";
    }
    else if(elem1.value == 25)
    {
        drawlineChart(data_25);
        drawRadarChart(data_25);
        rate = "25";
    }
    else if(elem1.value == 30)
    {
        drawlineChart(data_30);
        drawRadarChart(data_30);
        rate = "30";
    }
    else if(elem1.value == 35)
    {
        drawlineChart(data_35);
        drawRadarChart(data_35);
        rate = "35";
    }
    else if(elem1.value == 40)
    {
        drawlineChart(data_40);
        drawRadarChart(data_40);
        rate = "40";
    }
    else
    {
      drawRadarChart("null");
      drawlineChart("null");
    }
    var select_name = document.getElementById("Left-s");
    var index = select_name.selectedIndex;
    var select_n = select_name.options[index].value;
    if(select_n == "RJ")
    {
       tsne_change(select_n,rate,0);
       geomap_change(select_n,rate,0);
    }
    else if(select_n == "BFS")
    {
       tsne_change(select_n,rate,1);
       geomap_change(select_n,rate,1);
    }
    else if(select_n == "DFS")
    {
       tsne_change(select_n,rate,2);
       geomap_change(select_n,rate,2);
    }
    else if(select_n == "RN")
    {
       tsne_change(select_n,rate,3);
       geomap_change(select_n,rate,3);
    }
    else if(select_n == "RE")
    {
       tsne_change(select_n,rate,4);
       geomap_change(select_n,rate,4);
    }
    else if(select_n == "RW")
    {
       tsne_change(select_n,rate,5);
       geomap_change(select_n,rate,5);
    }
    else if(select_n == "ISRW")
    {
       tsne_change(select_n,rate,6);
       geomap_change(select_n,rate,6);
    }
    else if(select_n == "TIES")
    {
       tsne_change(select_n,rate,7);
       geomap_change(select_n,rate,7);
    }
    else
    {
       tsne_change("null");
       geomap_change("null");
    }

}