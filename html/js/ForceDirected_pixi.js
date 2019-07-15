var nodes = [];
var links = [];
var stroke_width = 1;
var force_width = 760;
var force_height = 705;
// var circle_Color = 0x4D5061;
var circle_Color = 0x3A435E;
var line_Color = 0xc6c6c6;
d3.csv("/data/oregonf.csv",function(error,csvdata){
    if(error){
        console.log(error);
    };

    for(var i=0;i<csvdata.length;i++){
        var data = {}
        var a1 = csvdata[i].source;
        var a2 = parseInt(csvdata[i].target);
        data["source"] = a1;
        data["target"] = a2;
        links.push(data);
    }
    d3.csv("../data/oregonf_TSNE_id_x_y.csv",function(error,nodesdata){
        for(var i=0;i<nodesdata.length;i++){
            var node = {}
            node.id = parseInt(nodesdata[i].id);
            nodes.push(node);      
        }
        let app = new PIXI.Application({
            width:force_width,
            height:force_height,
            // backgroundCo
            lor: 0xffffff,
            antialias: true,
            resolution : 1,
        });

        document.querySelector('#Centre_2').appendChild(app.view);
        app.renderer.backgroundColor = 0xffffff;
        var simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(function(d){
                    return d.id;
                    // console.log(d.id);
                }))
                .force("charge",d3.forceManyBody())//创建多体力
                .force("center",d3.forceCenter(width/2, height/2))
                .on("end",()=>{
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
                        
                    
                    for(var i = 0 ; i < nodes.length; i++){
                        nodes[i].x = parseInt(xScale(nodes[i].x));
                        nodes[i].y = parseInt(yScale(nodes[i].y));
                    }


                    const lines = new PIXI.Graphics();
                    for(var i = 0 ; i < links.length ; i++){
                        lines.lineStyle(0.4,line_Color,1);
                        lines.moveTo(links[i].source.x,links[i].source.y);
                        lines.lineTo(links[i].target.x,links[i].target.y);
                    }
                    app.stage.addChild(lines);

                    const circles = new PIXI.Graphics();
                    for(var i = 0 ; i < nodes.length ; i++){
                        circles.beginFill(circle_Color);
                        circles.drawCircle(nodes[i].x,nodes[i].y,1.5);
                        circles.endFill();
                    }
                    app.stage.addChild(circles);
                    console.log("end");
                })
    })
});