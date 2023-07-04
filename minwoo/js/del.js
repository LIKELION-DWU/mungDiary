//js 코드 _ 미완성(삭제부분)
const buttonElement = document.getElementById("trash-img");

// function delBtn() {
//   console.log("del");
//   document.getElementById("date").innerHTML = "";
//   document.getElementById("content").value = "";

//   const memoIdToDelete = this.parentNode.dataset.id;

//   // memos 배열에서 id가 memoIdToDelete인 항목을 찾기
//   const indexToDelete = memos.findIndex((memo) => memo.id === memoIdToDelete);

//   // indexToDelete가 유효한 값인 경우에만 삭제 수행
//   if (indexToDelete !== -1) {
//     // memos 배열에서 해당 항목 삭제
//     memos.splice(indexToDelete, 1);
//     localStorage.setItem("memos", JSON.stringify(memos));
//   }

//   // ..window.location.href = "main.html";
// }

function delBtn() {
  console.log("del");
  // const urlParams = new URLSearchParams(window.location.search);
  // const clickedId = urlParams.get("id");
  const clickedId = this.id;
  let memos = JSON.parse(localStorage.getItem("memos")) || [];
  // memos 배열 순회
  for (let i = 0; i < memos.length; i++) {
    const memo = memos[i];
    console.log(memo);
    // 클릭된 id와 memo의 id 비교
    if (memo.id === clickedId) {
      // 클릭된 메모를 배열에서 제거
      memos.splice(i, 1);

      // 변경된 memos 배열을 로컬 스토리지에 저장
      localStorage.setItem("memos", JSON.stringify(memos));

      // 수정된 메모를 화면에 표시하는 함수 호출
      //setMemo();

      // 반복문 종료
      break;
    }
  }
}

buttonElement.addEventListener("click", delBtn);
