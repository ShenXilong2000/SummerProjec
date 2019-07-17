function drawforce(data){
    var nodes = [];
    var links = [];
    var stroke_width = 1;
    var force_width = 760;
    var force_height = 705;
    var circle_Color = 0x3A435E;
    var line_Color = 0xc6c6c6;
    d3.json("/data/force_data_2_gai.json", function populate(datas){
        for(var key in datas){
            var node = {};
            node["id"] = key;
            node["x"] = datas[key]["x"];
            node["y"] = datas[key]["y"];
            nodes.push(node);
        }
        console.log(nodes);
        d3.csv("/data/oregonf.csv",function(error,csvdata){
            for(var i=0;i<csvdata.length;i++){
                var data = {};
                var a1 = csvdata[i].source;
                var a2 = csvdata[i].target;
                data["source"] = a1;
                data["target"] = a2;
                links.push(data);
            }
            let app = new PIXI.Application({
                width:force_width,
                height:force_height,
                antialias: true,
                resolution : 1,
            });

            console.log(nodes);

            document.querySelector('#Centre_2').appendChild(app.view);
            app.renderer.backgroundColor = 0xffffff;
            const lines = new PIXI.Graphics();
            for(var i = 0 ; i < links.length ; i++){
                lines.lineStyle(0.4,line_Color,1);
                lines.moveTo(datas[links[i].source].x,datas[links[i].source].y);
                lines.lineTo(datas[links[i].target].x,datas[links[i].target].y);
            }
            app.stage.addChild(lines);
            console.log(nodes);
            const circles = new PIXI.Graphics();
            for(var key in datas){
                circles.beginFill(circle_Color);
                circles.drawCircle(datas[key].x,datas[key].y,1.5);
                // circles.drawCircle(nodes[i].x,nodes[i].y,1.5);
                circles.endFill();
            }
        
            app.stage.addChild(circles);
        });
    })
}
drawforce();