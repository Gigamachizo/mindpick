
let current = 1;
let answers = [];

window.startTest = async function () {
  document.querySelector("button").style.display = "none";
  document.getElementById("test-box").style.display = "block";
  loadQuestion();
};

async function loadQuestion() {
  const res = await fetch(`/api/questions/${current}`);
  if (!res.ok) return showResult("Error");
  const q = await res.json();

  document.getElementById("question-title").innerText = q.title;
  document.getElementById("btn-a").innerText = q.choices[0].content;
  document.getElementById("btn-b").innerText = q.choices[1].content;
  document.getElementById("progress-text").innerText = `${current + 1} / ${q.total}`;
}


window.submitAnswer = async function (choice) {
  answers.push(choice);
  current++;
  const res = await fetch(`/api/questions/count`);
  const { count } = await res.json();

  if (current >= count) {
    const result = await fetch(`/api/result`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers })
    });
    const data = await result.json();
    showResult(data.result);
  } else {
    loadQuestion();
  }
};

function showResult(result) {
  document.getElementById("test-box").style.display = "none";
  document.getElementById("result-box").style.display = "block";
  document.getElementById("mbti-result").innerText = result;
}
