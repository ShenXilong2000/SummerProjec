function geomap_change(name,rate,num){
  var heatmapInstance = h337.create({
    container: document.querySelector("#heatmap"),
    radius: 10,
    opacity: [0.1, 0.8],
    blur: 0.75,
    color: {
      1: '#f0f9e8',
      0.8: '#bae4bc',
      0.6: '#7bccc4',
      0.4: '#43a2ca',
      0.2: '#0868ac',
    }
  });
  var points = [];
  var max = 0;
  var width =410;
  var height = 338;
  d3.json("/data/sampling_kde_kl_gai.json",function populate(jsondata){
    d3.csv("/data/kde/oregonf_TSNE_exponential_id_x_y_kde.csv",function(error, kdedata){
      var kdes = [];
      console.log(kdedata);
      for(var i = 0;i<kdedata.length;i++){
        var kde = {}
        kde.id = parseInt(kdedata[i].id);
        kde.x = parseFloat(kdedata[i].x);
        kde.y = parseFloat(kdedata[i].y);
        kde.kde = parseFloat(kdedata[i].kde);
        kdes.push(kde);
      }
      var x_max= d3.max(kdes,function(d){
        return d.x;
      })
      var y_max = d3.max(kdes,function(d){
        return d.y;
      })
      var x_min = d3.min(kdes,function(d){
        return d.x;
      })
      var y_min = d3.min(kdes,function(d){
        return d.y;
      })


      var xScale = d3.scaleLinear()
                      .domain([x_min,x_max])
                      .range([10,width])
      var yScale = d3.scaleLinear()
                      .domain([y_min,y_max])
                      .range([10,height])
      for(var i = 0;i<kdes.length;i++){
        kdes[i].x = parseInt(xScale(kdes[i].x));
        kdes[i].y = parseInt(yScale(kdes[i].y));
        var val = kdedata[i].kde * 250;
        max = Math.max(max,val);
        var point = {
          id:kdes[i].id,
          x: kdes[i].x,
          y: kdes[i].y,
          value : val,
        };
        points.push(point);
      }

      var data_sampling = []

      if(name=="null")data_sampling = points;
      else{
          var nodes =jsondata[num][name][rate]["node"];
          // console.log(points);
          for(var i in points){
              if(nodes.indexOf(points[i]["id"])!=-1)
                  // console.log(points[i]["id"]);
                  data_sampling.push({"id":points[i]["id"],"x":points[i]["x"],"y":points[i]["y"],"value":points[i]["val"]});
          }
          // console.log(data_sampling);
      }
      heatmapInstance.addData(data_sampling);
    });  
  });
}
geomap_change("null");