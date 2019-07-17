var nodes = [];
var links = [];
var stroke_width = 1;
var force_width = 760;
var force_height = 705;
// var circle_Color = 0x4D5061;
var circle_Color = 0x3A435E;
var line_Color = 0xc6c6c6;
d3.json("/data/force_data_gai.json", function populate(datas){ 

    // datas = d3.json.parse(data);
    for(var key in datas){
        var node = {};
        node["id"] = key;
        node["X"] = datas[key]["x"];
        node["y"] = datas[key]["y"];
        nodes.push(node);
    }
    // for(var i = 0; i<data.length;i++){
    //     var node = {};
    //     node["id"] = 
    //     node["x"] = datas[i]["x"];
    //     node["y"] = datas[i]["y"];
    //     nodes.push(node);
    // }


    d3.csv("/data/oregonf.csv",function(error,csvdata){
        if(error){
            console.log(error);
        };

        for(var i=0;i<csvdata.length;i++){
            var data = {};
            var a1 = csvdata[i].source;
            var a2 = csvdata[i].target;
            // data["source"] = a1;
            // data["source"].x = datas[a1].x;
            // data["source"].y = datas[a1].y;
            data["source"] = {"id": a1, "x" : datas[a1].x, "y":datas[a1].y}
            data["target"] = {"id": a2, "x" : datas[a2].x, "y":datas[a2].y}
            // data["target"] = a2;
            // data["target"].x = datas[a2].x;
            // data["target"].y = datas[a2].y;
            links.push(data);
        }

        let app = new PIXI.Application({
            width:force_width,
            height:force_height,
            // backgroundCo
            // lor: 0xffffff,
            antialias: true,
            resolution : 1,
        });
        document.querySelector('#Centre_2').appendChild(app.view);
        app.renderer.backgroundColor = 0xffffff;



        var x_max = d3.max(nodes,function(d){
            return d.x;
        })
        var x_min = d3.min(nodes,function(d){
            return d.x;
        })
        var y_max = d3.max(nodes,function(d){
            return d.y;
        })
        var y_min = d3.min(nodes,function(d){
            return d.y;
        })

        var xScale = d3.scaleLinear()
            .domain([x_min,x_max])
            .range([10,force_width]);
        var yScale = d3.scaleLinear()
            .domain([y_min,y_max])
            .range([10,force_height]);
// =======================
        // for(var key in datas){
        //     datas[key].x = parseInt(xScale(datas[key].x));
        //     datas[key].y = parseInt(yScale(datas[key].y));
        // }
//==================
        // for(var i = 0 ; i < nodes.length; i++){
        //     nodes[i].x = parseInt(xScale(nodes[i].x));
        //     nodes[i].y = parseInt(yScale(nodes[i].y));
        // }

        // for(var i = 0;i < links.length;i++){
        //     links[i]["source"].x = parseInt(xScale(links[i]["source"].x));
        //     links[i]["source"].y = parseInt(yScale(links[i]["source"].y));
        //     links[i]["target"].x = parseInt(xScale(links[i]["target"].x));
        //     links[i]["target"].y = parseInt(yScale(links[i]["target"].y));
        // }



        // const lines = new PIXI.Graphics();
        // for(var i = 0 ; i < links.length ; i++){
        //     lines.lineStyle(0.4,line_Color,1);
        //     lines.moveTo(links[i].source.x,links[i].source.y);
        //     lines.lineTo(links[i].target.x,links[i].target.y);
        // }
        // // for(var i = 0 ; i < links.length ; i++){
        // //     lines.lineStyle(0.4,line_Color,1);
        // //     // console.log(datas[links[i].source])
        // //     lines.moveTo(parseInt(xScale(datas[links[i].source].x)),parseInt(yScale(datas[links[i].source].y)));
        // //     lines.lineTo(parseInt(yScale(datas[links[i].target].x)),parseInt(yScale(datas[links[i].target].y)));
        // // }
        // app.stage.addChild(lines);

        const circles = new PIXI.Graphics();
        // for(var key in datas){
        //     circles.beginFill(circle_Color);
        //     circles.drawCircle(parseInt(xScale(datas[key].x)),parseInt(yScale(datas[key].y)),5);
        //     circles.endFill();
        // }
        for(var i = 0; i< nodes.length; i++){
            circles.beginFill(circle_Color);
            circles.drawCircle(nodes[i].x,nodes[i].y,1.5);
            circles.endFill();
        }
        app.stage.addChild(circles);
        console.log("end");
    });
})

