let vData = [];
let fData = [];

window.addEventListener('DOMContentLoaded', async () => {
    let url = `http://127.0.0.1:8003/statistics`;
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json();
        console.log(data);
        vData = data.visitordata;
        fData = data.paymentdata;
    } else {
        throw new Error('차량 목록 조회 실패!!');
    }
})

// 방문자 수 그래프
const visitorCtx = document.getElementById('visitorChart').getContext('2d');
const visitorData = {
    labels: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    datasets: [{
        label: '방문자 수',
        // data: [120, 150, 170, 200, 180, 220, 300, 350, 400, 380, 420, 450],
        data: vData,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
    }]
};

const visitorChart = new Chart(visitorCtx, {
    type: 'bar',
    data: visitorData,
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
            },
            title: {
                display: true,
                text: '월별 방문자 수',
            }
        },
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    },
});

// 요금 그래프
const feeCtx = document.getElementById('feeChart').getContext('2d');
const feeData = {
    labels: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    datasets: [{
        label: '요금 (만원)',
        data: [10, 15, 17, 20, 18, 22, 30, 35, 40, 38, 42, 45],
        // data: fData,
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1,
    }]
};

const feeChart = new Chart(feeCtx, {
    type: 'bar',
    data: feeData,
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
            },
            title: {
                display: true,
                text: '월별 요금',
            }
        },
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    },
});