function drawagain(data){
    //初始化
    var mW = 300;
    var mH = 600;
    var wz_x = 0;
    var wz_y = 0;
    var mCtx = null;
    var mData = data;
    var mCount = mData.length; //边数 
    var mCenter_x = 150;
    var mCenter_y = 630;
    // var mCenter_y = 695;
    // var mCenter = mW /2 - 20; //中心点
    var mRadius =  90; //半径(减去的值用于给绘制的文本留空间)
    var mAngle = Math.PI * 2 / mCount; //角度
    var mColorPolygon = '#B8B8B8'; //多边形颜色
    var mColorLines = '#B8B8B8'; //顶点连线颜色
    var mColorText = '#000000';
    (function(){
        var canvas = document.createElement('canvas');
        canvas.id="canvas_"
        document.body.appendChild(canvas);
        canvas.height = 800;
        canvas.width = 800;
        mCtx = canvas.getContext('2d');
        // canvas.height = canvas.height;

        drawPolygon(mCtx);
        drawLines(mCtx);
        drawText(mCtx);
        drawRegion(mCtx);
    //   drawCircle(mCtx);
    })();

        // 绘制多边形边
        function drawPolygon(ctx){
        ctx.save();

        ctx.strokeStyle = mColorPolygon;
        var r = mRadius/ mCount; //单位半径
        //画6个圈
        for(var i = -1 ; i < mCount; i= i+2){
            ctx.beginPath();        
            var currR = r * ( i + 1); //当前半径
            //画6条边
            for(var j = 0; j < mCount; j ++){
                var x = mCenter_x + currR * Math.cos(mAngle * j) + wz_x;
                var y = mCenter_y + currR * Math.sin(mAngle * j) + wz_y;

                ctx.lineTo(x, y);
            }
            ctx.closePath();
            ctx.stroke();
        }

        ctx.restore();
        }

    //顶点连线
    function drawLines(ctx){
        ctx.save();

        ctx.beginPath();
        ctx.strokeStyle = mColorLines;

        for(var i = 0; i < mCount; i ++){
            var x = mCenter_x + mRadius * Math.cos(mAngle * i) + wz_x;
            var y = mCenter_y + mRadius * Math.sin(mAngle * i) + wz_y;

            ctx.moveTo(mCenter_x, mCenter_y);
            ctx.lineTo(x, y);
        }

        ctx.stroke();

        ctx.restore();
    }

    //绘制文本
    function drawText(ctx){
        ctx.save();

        var fontSize = 15;
        ctx.font = fontSize + 'px Microsoft Yahei';
        ctx.fillStyle = mColorText;

        for(var i = 0; i < mCount; i ++){
            var x = mCenter_x + mRadius * Math.cos(mAngle * i) + wz_x;
            var y = mCenter_y + mRadius * Math.sin(mAngle * i) + wz_y;

            if( mAngle * i >= 0 && mAngle * i <= Math.PI / 2 ){
                ctx.fillText(mData[i][0], x, y + fontSize); 
            }else if(mAngle * i > Math.PI / 2 && mAngle * i <= Math.PI){
                ctx.fillText(mData[i][0], x - ctx.measureText(mData[i][0]).width, y + fontSize);    
            }else if(mAngle * i > Math.PI && mAngle * i <= Math.PI * 3 / 2){
                ctx.fillText(mData[i][0], x - ctx.measureText(mData[i][0]).width, y);   
            }else{
                ctx.fillText(mData[i][0], x, y);
            }

        }

        ctx.restore();
    }

    //绘制数据区域
    function drawRegion(ctx){
        ctx.save();
        ctx.beginPath();
        for(var i = 0; i < mCount; i ++){
            var x = mCenter_x + mRadius * Math.cos(mAngle * i) * mData[i][1] / 100 + wz_x;
            var y = mCenter_y + mRadius * Math.sin(mAngle * i) * mData[i][1] / 100 + wz_y;
            ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.fillStyle = 'rgba(35, 181, 211, 0.4)';
        ctx.fill();

        ctx.restore();
    }
}
var dataconst = 1000;
var data = [['BFS', 0.05990944603867329 * dataconst],
            ['DFS', 0.07006002226238398 * dataconst],
            ['ISRW', 0.07174573977904616 * dataconst],
            ['RE', 0.08119365235612636 * dataconst],
            ['RJ', 0.0673090476358627 * dataconst],
            ['RN',0.07026681024008176 * dataconst],
            ['RW',0.0712026039469732 * dataconst],
            ['TIES',0.07765626268173184 * dataconst]];
var mCtx = null;
drawagain(data);
// console.log(data);

var mCtx = null;
function drawRadarChart(data){
    // mCtx.clearRect(0,0,800,800);
    // d3.select('')
    if(data!="null")
    {
        var data_X = [['BFS', data.values[0][6]],
                    ['DFS', data.values[0][5]],
                    ['ISRW', data.values[0][3]],
                    ['RE', data.values[0][0]],
                    ['RJ', data.values[0][1]],
                    ['RN',data.values[0][2]],
                    ['RW',data.values[0][4]],
                    ['TIES',data.values[0][7]]];
        drawagain(data_X);        
    }
    else
    {
        var dataconst = 1000;
        var data = [['BFS', 0.05990944603867329 * dataconst],
                    ['DFS', 0.07006002226238398 * dataconst],
                    ['ISRW', 0.07174573977904616 * dataconst],
                    ['RE', 0.08119365235612636 * dataconst],
                    ['RJ', 0.0673090476358627 * dataconst],
                    ['RN',0.07026681024008176 * dataconst],
                    ['RW',0.0712026039469732 * dataconst],
                    ['TIES',0.07765626268173184 * dataconst]];
        var mCtx = null;
        drawagain(data);
    }
    // console.log(data_X);
}

//画点
// function drawCircle(ctx){
//     ctx.save();

//     var r = mCenter / 60;
//     for(var i = 0; i < mCount; i ++){
//         var x = mCenter + mRadius * Math.cos(mAngle * i) * mData[i][1] / 100;
//         var y = mCenter + mRadius * Math.sin(mAngle * i) * mData[i][1] / 100;

//         ctx.beginPath();            
//         ctx.arc(x, y, r, 0, Math.PI * 2);
//         ctx.fillStyle = '#23B5D3';
//         ctx.fill();
//     }       

//     ctx.restore();
// }