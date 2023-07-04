//js 코드
document.addEventListener("DOMContentLoaded", function () {
  const urlParams = new URLSearchParams(window.location.search);
  const memoId = urlParams.get("id");
  console.log("memoId: ", memoId);

  const memoDate = urlParams.get("date");
  console.log(date);
  const memoContent = urlParams.get("content");

  document.getElementById("date").innerHTML = memoDate;
  document.getElementById("content").innerHTML = memoContent;
});
