document.getElementById('study-plan-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const studyType = document.getElementById('study-type').value;
  const hoursPerDay = parseInt(document.getElementById('hours-per-day').value);
  const startTime = document.getElementById('start-time').value;
  const subject = document.getElementById('subject').value;
  const resources = document.getElementById('resources').value;

  const data = {
    user: "student1",
    studyType,
    hoursPerDay,
    startTime,
    subject,
    resources,
  };

  // Save data to localStorage
  localStorage.setItem('studyPlan', JSON.stringify(data));

  // Redirect to the draft plan page
  window.location.href = "draft_plan.html";
});