var nodes = [];
var links = [];
d3.csv("../data/oregonf.csv",function(error,csvdata){
    if(error){
        console.log(error);
    }
    // console.log(csvdata);

    var stroke_width = 1; 

    for(var i=0;i<csvdata.length;i++){
        // console.log(csvdata[i].source)
        var data = {}
        var a1 = csvdata[i].source;
        var a2 = parseInt(csvdata[i].target);
        data["source"] = a1;
        data["target"] = a2;
        links.push(data);
        if(a1==NaN||a2==NaN){
            console.log("err")
        }
        console.log(a1)
    }

    d3.csv("../data/oregonf_TSNE_id_x_y.csv",function(error,nodesdata){
        for(var i=0;i<nodesdata.length;i++){
            var node = {}
            node.id = parseInt(nodesdata[i].id);
            // node.x = parseFloat(nodesdata[i].x);
            // node.y =parseFloat(nodesdata[i].y);
            nodes.push(node);
            if(node.id==NaN){
                console.log("err")
            }
            
        }
        console.log(links);
        console.log(nodes);

        var width = 750;
        var height = 700;
        var svg = d3.select("#Centre_2")
                    .append("svg")
                    .attr("width",width)
                    .attr("height",height);
        console.log(d3.forceManyBody());
        // 通过布局来转换数据，然后进行绘制
        var simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(function(d){
                    return d.id;
            }))
                .force("charge",d3.forceManyBody())//创建多体力
                .force("center",d3.forceCenter(width/2, height/2))
                .on("end",function(){
                    console.log("ends")
            })

        simulation
              .nodes(nodes)//设置力模拟的节点
              .on("tick", ticked)
              .force("link")//添加或移除力
              .links(links);//设置连接数组
        var color = d3.scaleOrdinal(d3.schemeCategory20); 
        // 绘制
        var svg_links = svg.selectAll("line")
                .data(links)
                .enter()
                .append("line")
                // .style("stroke","#ccc")
                .style("stroke-width",stroke_width)
                .call(d3.zoom()//创建缩放行为
                .scaleExtent([-5, 2])//设置缩放范围
            );

        var svg_nodes = svg.selectAll("circle")
            .data(nodes)
            .enter()
            .append("circle")
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; })
            .attr("r", '3')
            .attr("fill", function(d,i){
                return color("#c3c3c3");
            }).call(d3.drag().on("start", dragstarted)//d3.drag() 创建一个拖曳行为
                .on("drag", dragged)
                .on("end", dragended));
        function dragstarted(d) {
            if (!d3.event.active) simulation.alphaTarget(0.3).restart();//设置目标α
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(d) {
                d.fx = d3.event.x;
                d.fy = d3.event.y;
            }

            function dragended(d) {
                if (!d3.event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
            function ticked() {
                svg_links.attr("x1", function(d) { return d.source.x; })
                    .attr("y1", function(d) { return d.source.y; })
                    .attr("x2", function(d) { return d.target.x; })
                    .attr("y2", function(d) { return d.target.y; });

                svg_nodes.attr("cx", function(d) { return d.x; })
                    .attr("cy", function(d) { return d.y; });
                
                svg_texts.attr("x", function(d){ return d.x; })
                    .attr("y", function(d){ return d.y; });
        }
    });
});


