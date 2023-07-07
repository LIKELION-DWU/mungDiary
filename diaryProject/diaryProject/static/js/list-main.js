//js 코드
let memos = JSON.parse(localStorage.getItem("memos"));
memos = memos ?? [];

const date = new Date();

const year = date.getFullYear();
const month = date.getMonth() + 1;
const day = date.getDate();
//위에 오늘 날짜 보이기
document.getElementById("year").innerText = year;
document.getElementById("month").innerText = month;
document.getElementById("day").innerText = day;

