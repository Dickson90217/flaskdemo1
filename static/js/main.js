
const chart1 = echarts.init(document.querySelector('#main'));

$(document).ready(() => {
    drawPM25();
});

function drawPM25() {

    $.ajax(
        {
            url: "/pm25-data",
            type: "POST",
            dataType: "json",
            success: (data) => {
                console.log(data);
                var option = {
                    title: {
                        text: '全台pm2.5'
                    },
                    tooltip: {},
                    legend: {
                        data: ['pm2.5數值']
                    },
                    xAxis: {
                        data: data['site']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'PM2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };


                chart1.setOption(option);
            },
            error: () => alert('讀取失敗')
        }
    );
}