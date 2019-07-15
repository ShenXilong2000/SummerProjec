// 声明所需变量
var canvas,ctx;
// 图表属性
var cWidth, cHeight, cMargin, cSpace;
var originX, originY;
// 折线图属性
var tobalDots, dotSpace, maxValue;
var totalYNomber;
// 运动相关变量
var ctr, numctr, speed;
function goChart(dataArr, flag){
    // 获得canvas上下文
    canvas = document.getElementById("chart");
    if(canvas && canvas.getContext){
        ctx = canvas.getContext("2d");
    }
    if(flag == true){
        initChart(); // 图表初始化
        drawLineLabelMarkers(); // 绘制图表轴、标签和标记
    }
    drawLineAnimate(); // 绘制折线图的动画

    // 图表初始化
    function initChart(){
        // 图表信息
        cMargin = 60;
        cSpace = 60;
        canvas.width = 600;
        canvas.height = 400;
        canvas.style.height = canvas.height/2 + "px";
        canvas.style.width = canvas.width/2 + "px";
        cHeight = canvas.height - cMargin - cSpace;
        cWidth = canvas.width - cMargin - cSpace;
        originX = cMargin + cSpace;
        originY = cMargin + cHeight;

        // 折线图信息
        tobalDots = dataArr.length;
        dotSpace = parseInt( cWidth/tobalDots );
        maxValue = 0;
        for(var i=0; i<dataArr.length; i++){
            var dotVal = parseInt( dataArr[i][1] );
            if( dotVal > maxValue ){
                maxValue = dotVal;
            }
        }
        maxValue += 50;
        totalYNomber = 10;
        // 运动相关
        ctr = 100;
        numctr = 100;
        speed = 1;

        ctx.translate(0.5,0.5);  // 当只绘制1像素的线的时候，坐标点需要偏移，这样才能画出1像素实线
    }

    // 绘制图表轴、标签和标记
    function drawLineLabelMarkers(){
        ctx.font = "24px Arial";
        ctx.lineWidth = 2;
        ctx.fillStyle = "#566a80";
        ctx.strokeStyle = "#566a80";
        // y轴
        drawLine(originX, originY, originX, cMargin);
        // x轴
        drawLine(originX, originY, originX+cWidth, originY);

        // 绘制标记
        drawMarkers();
    }

    // 画线的方法
    function drawLine(x, y, X, Y){
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(X, Y);
        ctx.stroke();
        ctx.closePath();
    }

    // 绘制标记
    function drawMarkers(){
        ctx.strokeStyle = "#E0E0E0";
        // 绘制 y 轴 及中间横线
        var oneVal = parseInt(maxValue/totalYNomber);
        ctx.textAlign = "right";
        for(var i=0; i<=totalYNomber; i++){
            var markerVal =  i*oneVal;
            var xMarker = originX-5;
            var yMarker = parseInt( cHeight*(1-markerVal/maxValue) ) + cMargin;
            if(i>0){
                drawLine(originX+2, yMarker, originX+cWidth, yMarker);
            }
        }
        // 绘制 x 轴 及中间竖线
        ctx.textAlign = "center";
        for(var i=0; i<tobalDots; i++){
            var markerVal = dataArr[i][0];
            var xMarker = originX+i*dotSpace;
            var yMarker = originY+30;
            ctx.fillText(markerVal, xMarker, yMarker, cSpace); // 文字
            if(i>0){
                drawLine(xMarker, originY-2, xMarker, cMargin);
            }
        }
        // 绘制标题 y
        ctx.save();
        ctx.rotate(-Math.PI/2);
        ctx.fillText("采样率", -canvas.height/2, cSpace+30);
        ctx.restore();
    };

    //绘制折线图
    function drawLineAnimate(){
        ctx.strokeStyle = "#566a80";  //"#49FE79";
        //连线
        ctx.beginPath();
        for(var i=0; i<tobalDots; i++){
            var dotVal = dataArr[i][1];
            var barH = parseInt( cHeight*dotVal/maxValue* ctr/numctr );
            var y = originY - barH;
            var x = originX + dotSpace*i;
            if(i==0){
                ctx.moveTo( x, y );
            }else{
                ctx.lineTo( x, y );
            }
        }
        ctx.stroke();

        //背景
        ctx.lineTo( originX+dotSpace*(tobalDots-1), originY);
        ctx.lineTo( originX, originY);

        //绘制点
        for(var i=0; i<tobalDots; i++){
            var dotVal = dataArr[i][1];
            var barH = parseInt( cHeight*dotVal/maxValue * ctr/numctr );
            var y = originY - barH;
            var x = originX + dotSpace*i;
            drawArc( x, y );  //绘制点
            ctx.fillText(parseInt(dotVal*ctr/numctr), x+15, y-8); // 文字
        }
    }

    //绘制圆点
    function drawArc( x, y, X, Y ){
        ctx.beginPath();
        ctx.arc( x, y, 5, 0, Math.PI*2 );
        ctx.fill();
        ctx.closePath();
    }
}

var dataconst = 1000;
var chartData = [["RW", 0.0712026039469732 * dataconst], ["TIES", 0.07765626268173184 * dataconst], ["BFS", 0.05990944603867329 * dataconst], ["DFS",0.07006002226238398 * dataconst], ["ISRW",0.07174573977904616 * dataconst], ["RE",0.08119365235612636 * dataconst], ["RJ",  0.0673090476358627 * dataconst], ["RN",0.07026681024008176 * dataconst]];
goChart(chartData, true);
function drawlineChart(data)
{
    ctx.clearRect(0,0,400,400);
    var dataconst = 1000;
    var chartData = [["RW", 0.0712026039469732 * dataconst], ["TIES", 0.07765626268173184 * dataconst], ["BFS", 0.05990944603867329 * dataconst], ["DFS",0.07006002226238398 * dataconst], ["ISRW",0.07174573977904616 * dataconst], ["RE",0.08119365235612636 * dataconst], ["RJ",  0.0673090476358627 * dataconst], ["RN",0.07026681024008176 * dataconst]];
    goChart(chartData, true);
    if(data!="null")
    {
        var chartData2 = [["RW", data.values[0][4]], 
                        ["TIES", data.values[0][7]], 
                        ["BFS", data.values[0][6]], 
                        ["DFS",data.values[0][5]], 
                        ["ISRW",data.values[0][3]],
                        ["RE",data.values[0][0]], 
                        ["RJ", data.values[0][1]], 
                        ["RN",data.values[0][2]]];
        goChart(chartData2, false);        
    }

    // console.log(data);
    // console.log(data.values[0][0]);
}
