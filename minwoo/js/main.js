//js 코드
let memos = JSON.parse(localStorage.getItem("memos"));
memos = memos ?? [];

const date = new Date();

const year = date.getFullYear();
const month = date.getMonth() + 1;
const day = date.getDate();

document.getElementById("year").innerText = year;
document.getElementById("month").innerText = month;
document.getElementById("day").innerText = day;

window.onload = function () {
  const elements = document.getElementById("content-list");
  if (elements === null) {
    console.error("content-list element not found");
    return;
  }

  elements.innerHTML = ""; // 기존의 메모들을 초기화

  if (!memos || memos.length === 0) {
    console.log("No memos found");
    return;
  }

  for (let i = memos.length - 1; i >= 0; i--) {
    // white-box
    let whiteBox = document.createElement("div");
    whiteBox.classList.add("white-box");

    // box1 or box2 or box3
    let box = document.createElement("div");
    box.classList.add("box");
    // h2 : date
    let date = document.createElement("div");
    date.textContent = memos[i].date;
    date.classList.add("totalDate");

    // div : line
    let line = document.createElement("div");
    line.classList.add("line");

    // div : content
    let content = document.createElement("div");
    content.setAttribute("id", "content" + (i + 1));
    content.textContent = memos[i].content;
    content.classList.add("cont");

    box.append(date, line, content);
    whiteBox.append(box);
    elements.append(whiteBox);
  }

  const whiteBoxes = document.querySelectorAll(".white-box");
  whiteBoxes.forEach(function (whiteBox) {
    whiteBox.addEventListener("click", onWhiteBoxClick);
  });

  function onWhiteBoxClick() {
    console.log("whitebox");

    //이부분 실행 안됨
    const whiteBoxId = this.dataset.id;
    //console.log("whiteBoxId: ", whiteBoxId);

    const whiteBoxDate = this.querySelector(".totalDate").textContent;
    //const whiteBoxContent = this.dataset.content;
    const whiteBoxContent = this.querySelector(".cont").textContent;

    window.location.href =
      "/mungTeam/minwoo/pages/check.html?id=" +
      encodeURIComponent(whiteBoxId) +
      "&date=" +
      encodeURIComponent(whiteBoxDate) +
      "&content=" +
      encodeURIComponent(whiteBoxContent);
  }
};

const logOut = document.getElementById("log-out");

function goLogOutPage() {
  window.location.href = "login.html";
}

logOut.addEventListener("click", goLogOutPage);

const ListBtn = document.getElementById("list-icon");

function changeIntoList() {
  console.log("리스트 클릭");
  window.location.href = "list-main.html";
}

ListBtn.addEventListener("click", changeIntoList);
