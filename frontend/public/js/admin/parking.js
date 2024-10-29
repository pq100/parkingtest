// 이용가능한 차량 수
let carCount = 0;
// 총 주차 자리 수
let totalSpots = 0;

window.addEventListener('DOMContentLoaded', async () => {
    try {
        await remainCar();
    } catch (e) {
        console.log(e);
        alert('남은 주차 자리수 조회 실패!');
    }
});

// 남은 주차자리 수
const remainCar = async () => {

    let url = 'http://127.0.0.1:8002/available-spots'
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json();
        // const remainCars = document.querySelector('#remainCars');
        // // const remainBarrier = document.querySelector('#remainBarrier');
        //
        // if (data) {
        //
        //     let html = `${data.total_available_spots || 0}/100`;
        //     // let html1 = `50/100`;
        //     remainCars.innerHTML = html;
        // }else{
        //     console.log('no')
        // }
        if (data) {
            // 임시 데이터 설정
            totalSpots = data.total_available_spots || 0;
            carCount = totalSpots-data.non_disabled_spots_left || 0;
        } else {
            alert('주차 데이터가 없습니다.');
        }}


    const usedSpots = carCount;
    const usedIndices = new Set();

    // 랜덤한 인덱스 생성 (중복되지 않도록)
    while (usedIndices.size < usedSpots) {
        const randomIndex = Math.floor(Math.random() * totalSpots);
        usedIndices.add(randomIndex);
    }

    // 장애인 주차 공간 사용 중인 자리 수
    const disabledUsedCount = 2; // 사용 중인 장애인 주차 자리 수
    const totalDisabledSpots = 3; // 총 장애인 주차 자리 수

    // 구역당 20개 공간을 생성
    const areas = ['A', 'B', 'C', 'D', 'E'];
    let index = 0;

    for (const area of areas) {
        const parkingSpotsContainer = document.getElementById(`${area}-parking-spots`);

        // 일반 주차 공간 생성
        for (let i = 0; i < 20; i++) {
            const spot = document.createElement("div");
            spot.className = "parking-spot";

            // 사용된 자리일 경우 색상 변경
            if (usedIndices.has(index)) {
                spot.style.backgroundColor = "#ff6347"; // 사용 중 (예: 빨간색)
            } else {
                spot.style.backgroundColor = "#32cd32"; // 사용 가능 (예: 초록색)
            }

            parkingSpotsContainer.appendChild(spot);
            index++;
        }
    }

    // F구역에 장애인 주차 공간 생성
    const disabledParkingSpotsContainer = document.getElementById("F-disabled-parking-spots");
    for (let j = 0; j < totalDisabledSpots; j++) {
        const disabledSpot = document.createElement("div");
        disabledSpot.className = "disabled-parking-spot";

        // 사용된 자리일 경우 색상 변경
        if (j < disabledUsedCount) {
            disabledSpot.style.backgroundColor = "#ff6347"; // 사용 중
        } else {
            disabledSpot.style.backgroundColor = "#0000ff"; // 사용 가능
        }

        disabledParkingSpotsContainer.appendChild(disabledSpot);
    }
};