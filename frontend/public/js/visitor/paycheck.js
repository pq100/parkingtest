// 현재 URL의 경로 가져오기
const path = window.location.pathname;

// 경로를 슬래시로 분리
const pathSegments = path.split('/');

// 마지막 값을 가져오기 (배열의 마지막 요소)
const lastSegment = pathSegments[pathSegments.length - 1];

// 마지막 값을 디코딩
const carnum = decodeURIComponent(lastSegment);

// console.log(`마지막 값: ${carnum}`);

window.addEventListener('DOMContentLoaded', async () => {
    try {
        const payment = await paylist();
        displayPayment(payment);

        // 버튼 클릭 이벤트 리스너 등록
        document.getElementById('confirmPaymentButton').addEventListener('click', function (event) {
            event.preventDefault();
            processPayment();
        });

    } catch(e) {
        console.log(e);
        alert('정산내역 조회 실패!');
    }
})

const paylist = async () => {
    let url = `http://127.0.0.1:8001/payment/${carnum}`;
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json();
        return data;
    } else {
        throw new Error('차량 목록 조회 실패!!');
    }
    // const dummyData = [
    //     {
    //         carnum: '12 가 1234',
    //         intime: '2024-10-01 10:00',
    //         outtime: '2024-10-01 12:00',
    //         paydate: '2시간',
    //         payment: '5,000원'
    //     }
    // ];
    // return dummyData;
}

const displayPayment = (payment) => {
    const paytbody = document.querySelector('#paytbody');

    let html = `
        <tr>
            <th>차량 번호</th>
            <td id="carLicense">${carnum}</td>
        </tr>
        <tr>
            <th>입차 시간</th>
            <td id="entryTime">${payment[0].intime}</td>
        </tr>
        <tr>
            <th>출차 시간</th>
            <td id="exitTime">${payment[0].outtime}</td>
        </tr>
        <tr>
            <th>주차 시간</th>
            <td id="parkingDuration">${payment[0].paydate}</td>
        </tr>
        <tr>
            <th>요금 확인</th>
            <td id="fee">${payment[0].payment}</td>
        </tr>
    `
    paytbody.innerHTML = html;
}

// 아임포트 결제 api
// document.getElementById('confirmPaymentButton').addEventListener('click', function (event) {
//     event.preventDefault();
//
//     // 아임포트 결제 시작
//     var IMP = window.IMP;
//     IMP.init('imp77608186'); // 본인의 가맹점 식별코드로 변경
//
//     // 결제 금액 가져오기
//     var amount = parseInt(document.getElementById('fee').innerText.replace(/[^0-9]/g, ''), 10);
//
//     // 결제 요청
//     IMP.request_pay({
//         pg: 'html5_inicis',
//         pay_method: 'card',
//         merchant_uid: 'merchant_' + new Date().getTime(), // 주문 번호
//         name: '주차 요금 결제', // 주문명
//         amount: amount, // 결제 금액
//         buyer_email: 'test@example.com', // 예약자 이메일
//         buyer_name: '홍길동', // 예약자 이름
//         buyer_tel: '010-1234-5678' // 예약자 연락처
//     }, function (rsp) {
//         if (rsp.success) {
//             // 결제 성공 시 서버로 데이터 전송
//             fetch('/pay/complete', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify({ imp_uid: rsp.imp_uid, success: true })
//             })
//                 .then(response => response.json())
//                 .then(data => {
//                     alert('결제가 완료되었습니다.');
//                     window.location.href = '/rental';
//                 })
//                 .catch(error => {
//                     alert('서버와의 통신 중 오류가 발생했습니다.');
//                 });
//         } else {
//             alert('결제가 실패했습니다.');
//         }
//     });
// });

const processPayment = () => {
    // 아임포트 결제 시작
    var IMP = window.IMP;
    IMP.init('imp77608186'); // 본인의 가맹점 식별코드로 변경

    // 결제 금액 가져오기
    var feeElement = document.getElementById('fee');
    if (!feeElement) {
        alert('요금 정보가 없습니다.');
        return;
    }

    var amount = parseInt(feeElement.innerText.replace(/[^0-9]/g, ''), 10);

    // 결제 요청
    IMP.request_pay({
        pg: 'html5_inicis',
        pay_method: 'card',
        merchant_uid: 'merchant_' + new Date().getTime(), // 주문 번호
        name: '주차 요금 결제', // 주문명
        amount: amount, // 결제 금액
        buyer_email: 'test@example.com', // 예약자 이메일
        buyer_name: '홍길동', // 예약자 이름
        buyer_tel: '010-1234-5678' // 예약자 연락처
    }, function (rsp) {
        if (rsp.success) {
            // 결제 성공 시 서버로 데이터 전송
            fetch('/pay/complete', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ imp_uid: rsp.imp_uid, success: true })
            })
                .then(response => response.json())
                .then(data => {
                    alert('결제가 완료되었습니다.');
                    window.location.href = '/rental';
                })
                .catch(error => {
                    alert('서버와의 통신 중 오류가 발생했습니다.');
                });
        } else {
            alert('결제가 실패했습니다.');
        }
    });
};