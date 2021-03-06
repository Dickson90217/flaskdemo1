
const chart1 = echarts.init(document.querySelector('#main'));
const chart2 = echarts.init(document.querySelector('#six'));
const chart3 = echarts.init(document.querySelector('#county'));
const county_btn = document.querySelector('#county_btn');


window.onresize = function () {
    chart1.resize()
    chart2.resize()
    chart3.resize()
};

$(document).ready(() => {
    drawPM25();
    getSixData();
    getCountyData('高雄市');
});

county_btn.addEventListener('click', () => {
    console.log('click')
    const county = document.querySelector('#select_county').value;
    getCountyData(county);
});

function getCountyData(county) {

    $.ajax(
        {
            url: `/county-pm25/${county}`,
            type: "GET",
            dataType: "json",
            success: (data) => {
                console.log(data);
                var option = {
                    title: {
                        text: data['title']
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {},
                    legend: {
                        data: ['pm2.5']
                    },
                    xAxis: {
                        data: data['county']
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

                chart3.setOption(option);
            },
            error: () => alert('讀取失敗')
        }
    );

};



function getSixData() {

    $.ajax(
        {
            url: "/six-pm25",
            type: "POST",
            dataType: "json",
            success: (data) => {
                console.log(data);
                var option = {
                    title: {
                        text: '六都平均數值'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {},
                    legend: {
                        data: ['pm2.5數值']
                    },
                    xAxis: {
                        data: data['city']
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

                chart2.setOption(option);
            },
            error: () => alert('讀取失敗')
        }
    );

};
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
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
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

                document.querySelector('#pm25_high_site').innerText = data['hightest'][0];
                document.querySelector('#pm25_high_value').innerText = data['hightest'][1];
                $('#pm25_low_site').text(data['lowest'][0]);
                $('#pm25_low_value').text(data['lowest'][1]);
                document.querySelector('#date').innerText = data['date'];




                chart1.setOption(option);
            },
            error: () => alert('讀取失敗')
        }
    );


}