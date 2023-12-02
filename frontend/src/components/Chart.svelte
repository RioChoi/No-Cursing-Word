<canvas id="myChart"></canvas>

<script>
    import Chart from 'chart.js/auto'
    import {afterUpdate} from 'svelte'

    export let result;
    console.log(result)

    let ctx;
    let myChart;

    afterUpdate(async (promise) => {
        let tmp;
        let data = [];
        tmp = String(result).split(',');
        for (let i = 1; i <= 20; i += 2) {
            data.push(tmp[i] * 100);
        }
        ctx = document.getElementById('myChart');
        if (myChart) myChart.destroy()
        myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', '문제없음'],
                datasets: [{
                label: '# of Votes',
                data: data,
                borderWidth: 1
                }]
            },
            options: {
                scales: {
                y: {
                    beginAtZero: true
                }
                }
            }
        });
    });

</script>
   