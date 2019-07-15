
// //read csv
// d3.csv("/data/oregonf_TSNE_id_x_y_5000.csv",function(error,csvdata){
//     d3.json("/data/sampling_kde_kl_gai.json",function populate(jsondata){
//         var datas = [];
//         tsneData = csvdata;
//         for(var i=0;i<csvdata.length;i++){
//             var data ={}
//             data["x"] = parseFloat(csvdata[i].x);
//             data["y"] = parseFloat(csvdata[i].y);
//             data["id"] = parseInt(csvdata[i].id);
//             datas.push(data);
//         }
        
//         json = {};


//         var x_max = d3.max(datas,function(d){
//             return d.x;
//         })
//         var x_min = d3.min(datas,function(d){
//             return d.x;
//         })
//         var y_max = d3.max(datas,function(d){
//             return d.y;
//         })
//         var y_min = d3.min(datas,function(d){
//             return d.y;
//         })

//         var xScale = d3.scaleLinear()
//                         .domain([x_min,x_max])
//                         .range([10,410]);
//         var yScale = d3.scaleLinear()
//                         .domain([y_min,y_max])
//                         .range([10,340]);
//         for(var i = 0 ; i < datas.length; i++){
//             datas[i].x = parseInt(xScale(datas[i].x));
//             datas[i].y = parseInt(yScale(datas[i].y));
//         }

//         var data_sampling = []
//         function tsne_change(name,rate){
                


//             // .remove();
//             console.log(d3.select("#dataviz-container").select("g").selectAll("circle"));

//             if(name=="null")data_sampling = datas;
//             else{
//                 var nodes =jsondata[name][rate]["node"];
//                 for(var node in nodes){
//                     data_sampling.push(datas[datas.indexOf(node)]);
//                 }
//             }
//             var svg = d3.select("#dataviz-container")
//                     .append('svg')
//                     .attr('width', 410)
//                     .attr('height', 340);
//             svg.append("g")
//                 .selectAll('.circle')
//                 .data( data_sampling )
//                 .enter()
//                     .append('circle')
//                     .attr('r', 1)
//                     .attr('fill', '#26963c')
//                     .attr('cx', function(d){ return d["x"]; })
//                     .attr('cy', function(d){ return d["y"]; })

//         }
//         tsne_change("null","2");

//         // console.log();
//         // generate the dataviz

//     })

// });
//===============================================================
function tsne_change(name,rate,num){
    //read csv
    d3.csv("/data/oregonf_TSNE_id_x_y_5000.csv",function(error,csvdata){
        d3.json("/data/sampling_kde_kl_gai.json",function populate(jsondata){
            var datas = [];
            tsneData = csvdata;
            for(var i=0;i<csvdata.length;i++){
                var data ={}
                data["x"] = parseFloat(csvdata[i].x);
                data["y"] = parseFloat(csvdata[i].y);
                data["id"] = parseInt(csvdata[i].id);
                datas.push(data);
            }
            
            json = {};

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
            for(var i = 0 ; i < datas.length; i++){
                datas[i].x = parseInt(xScale(datas[i].x));
                datas[i].y = parseInt(yScale(datas[i].y));
            }

            var data_sampling = []
            // d3.select("#dataviz-container").remove();

            if(name=="null")data_sampling = datas;
            else{
                // console.log(jsondata);
                var nodes =jsondata[num][name][rate]["node"];
                // console.log(nodes);
                for(var i in datas){
                    if(nodes.indexOf(datas[i]["id"])!=-1)
                        // console.log(datas[i]["id"]);
                        data_sampling.push(datas[i]);
                        // console.log((nodes.indexOf(datas[i]["id"])));
                }

                // for(var node in nodes){
                //     console.log(datas.indexOf(node));
                //     data_sampling.push();
                // }
                // console.log(datas);
                console.log(data_sampling);
            }
            var svg = d3.select("#dataviz-container")
                    .append('svg')
                    .attr('width', 410)
                    .attr('height', 340);
            svg.append("g")
                .selectAll('.circle')
                .data( data_sampling )
                .enter()
                    .append('circle')
                    .attr('r', 1)
                    .attr('fill', '#26963c')
                    .attr('cx', function(d){ return d["x"]; })
                    .attr('cy', function(d){ return d["y"]; })

            // console.log();
            // generate the dataviz

        })

    });

}
tsne_change("null","2");
