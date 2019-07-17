const d3 = require("d3");
const fs = require("fs");
// console.log(d3)
var Alledges=[];
var Allnodes=[];
var file="oregon2";
function drawforce(nodeArr, edgeArr) {
    var nodesid = [];
    for (var i = 0; i < nodeArr.length; i++) {
        nodesid.push({
            id: parseInt(nodeArr[i])
        })
    }
    var links = []

    for (var i = 0; i < edgeArr.length; i++) {
        links.push({
            source: parseInt(edgeArr[i][0]),
            target: parseInt(edgeArr[i][1])
        })
    }

    const width = 760;
    const height = 710;




    var simulation = d3.forceSimulation(nodesid)
        .force("link", d3.forceLink(links).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        .on('tick', function () {
            //console.log("waiting...");
        })
        
        .on("end",()=>{
            var x_max = d3.max(nodesid,function(d){
                return d.x;
            })
            var x_min = d3.min(nodesid,function(d){
                return d.x;
            })
            var y_max = d3.max(nodesid,function(d){
                return d.y;
            })
            var y_min = d3.min(nodesid,function(d){
                return d.y;
            })
        
            var xScale = d3.scaleLinear()
                .domain([x_min,x_max])
                .range([10,width]);
            var yScale = d3.scaleLinear()
                .domain([y_min,y_max])
                .range([10,height]);
        
            for(var i = 0 ; i < nodesid.length; i++){
                    nodesid[i].x = parseInt(xScale(nodesid[i].x));
                    nodesid[i].y = parseInt(yScale(nodesid[i].y));
            }
            console.log(nodesid)
            fs.writeFile("force_data.json",JSON.stringify(nodesid),function(err){
                if(err){
                    console.log("写入失败！！！");
                }
                else{
                    console.log("写入成功！！！");
                }
            })
        })
    
};

function getData(fileName) {
    Alledges = [];
    Allnodes = [];
    fs.readFile("E:\\暑期任务\\Python\\data\\oregonf_nodes_edges.json", function (err,data) {
        data = JSON.parse(data)
        console.log(data)
        Allnodes = data["nodes"];
        Alledges = data["edges"];
        console.log(Allnodes);
        console.log(Alledges);
        drawforce(Allnodes,Alledges);
    }) 
    
}
getData(file);
