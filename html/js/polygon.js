//read csv
d3.csv("/data/oregonf_TSNE_id_x_y_5000.csv",function(error,csvdata){
    
        var datas = [];
        tsneData = csvdata;
        for(var i=0;i<csvdata.length;i++){
            var data ={}
            data["x"] = parseFloat(csvdata[i].x);
            data["y"] = parseFloat(csvdata[i].y);
            data["id"] = parseInt(csvdata[i].id);
            datas.push(data);
        }

        var x_max = d3.max(datas,function(d){
            return d.x;
        })
        var x_min = d3.min(datas,function(d){
            return d.x;
        })
        var y_max = d3.max(datas,function(d){
            return d.y;
        })
        var y_min = d3.min(datas,function(d){
            return d.y;
        })

        var xScale = d3.scaleLinear()
                        .domain([x_min,x_max])
                        .range([10,410]);
        var yScale = d3.scaleLinear()
                        .domain([y_min,y_max])
                        .range([10,340]);
        // var svg = d3.select("#dataviz-container")
        //         .append('svg')
        //         .attr('width', 410)
        //         .attr('height', 340);
        d3.json("/data/dbscan_id_x_y.json", function populate(dbscanData)
        {
            var points = []
            for (var key in dbscanData)
            {
                for(var id in dbscanData[key])
                {
                    var point = {"id":id, "x":dbscanData[key][id]["x"],"y":dbscanData[key][id]["y"]}
                    points.push([dbscanData[key][id]["x"], dbscanData[key][id]["y"]]);
                }
                var hull = d3.polygonHull(points);
                hull.push(
                    [hull[0][0],hull[0][1]]
                )
                var hullPath = d3.line()
                .x(function(value){
                    return xScale(value[0])
                })
                .y(function(value){
                    return yScale(value[1])
                });   
                points = [];    
                svg.append('path')
                .attr('id',function()
                {
                    return "svg_" + String(key)
                })
                .attr("d",hullPath(hull))
                .attr('stroke','#BABABA')
                .attr('stroke-width',2)
                .attr('fill','none');

                            
            }
        });

});