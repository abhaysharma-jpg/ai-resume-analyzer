// ===== DRAG & DROP =====
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('resumeFile');

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file) setFile(file);
});
dropZone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', () => {
  if (fileInput.files[0]) setFile(fileInput.files[0]);
});

function setFile(file) {
  document.getElementById('fileName').textContent = file.name;
  document.getElementById('fileChip').classList.remove('hidden');
  document.getElementById('resumeText').value = '';
}

function removeFile() {
  fileInput.value = '';
  document.getElementById('fileChip').classList.add('hidden');
}

// ===== FORM SUBMIT =====
document.getElementById('analyzeForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  hideError();

  const btn = document.getElementById('analyzeBtn');
  const btnText = document.getElementById('btnText');
  const btnLoader = document.getElementById('btnLoader');

  btn.disabled = true;
  btnText.textContent = 'Analyzing…';
  btnLoader.classList.remove('hidden');

  const formData = new FormData(e.target);

  try {
    const res = await fetch('/analyze', { method: 'POST', body: formData });
    const json = await res.json();
    if (!json.success) {
      showError(json.error || 'Something went wrong.');
    } else {
      renderResults(json.data);
    }
  } catch (err) {
    showError('Network error. Please try again.');
  } finally {
    btn.disabled = false;
    btnText.textContent = '✦ Analyze My Resume';
    btnLoader.classList.add('hidden');
  }
});

// ===== RENDER RESULTS =====
function renderResults(data) {
  document.getElementById('results').classList.remove('hidden');
  document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'start' });

  document.getElementById('overallScore').textContent = data.overall_score + '%';

  const fitBadge = document.getElementById('fitBadge');
  const fit = data.experience_level_match || 'Partial Match';
  fitBadge.textContent = fit;
  fitBadge.className = 'fit-badge';
  if (fit.includes('Strong')) fitBadge.classList.add('strong');
  else if (fit.includes('Weak')) fitBadge.classList.add('weak');
  else fitBadge.classList.add('partial');

  document.getElementById('summaryText').textContent = data.summary || '';
  const topMissing = document.getElementById('topMissing');
  if (data.top_missing_skill) {
    topMissing.textContent = '⚠ Top missing skill: ' + data.top_missing_skill;
    topMissing.style.display = 'block';
  }

  setBar('skillsVal', 'skillsBar', data.skills_score);
  setBar('expVal', 'expBar', data.experience_score);
  setBar('kwVal', 'kwBar', data.keyword_score);
  setBar('atsVal', 'atsBar', data.ats_score);

  document.getElementById('matchedTags').innerHTML = (data.matched_keywords || [])
    .map(k => `<span class="tag match">✔ ${k}</span>`).join('');
  document.getElementById('missingTags').innerHTML = (data.missing_keywords || [])
    .map(k => `<span class="tag miss">✗ ${k}</span>`).join('');
  document.getElementById('strengthsList').innerHTML = (data.strengths || [])
    .map(s => `<li>${s}</li>`).join('');
  document.getElementById('suggestionsList').innerHTML = (data.suggestions || [])
    .map(s => `<li>${s}</li>`).join('');
}

function setBar(valId, barId, score) {
  document.getElementById(valId).textContent = score + '%';
  const bar = document.getElementById(barId);
  bar.style.background = score >= 75 ? '#22C55E' : score >= 50 ? '#F59E0B' : '#EF4444';
  setTimeout(() => { bar.style.width = score + '%'; }, 100);
}

function resetForm() {
  document.getElementById('results').classList.add('hidden');
  document.getElementById('analyzeForm').reset();
  document.getElementById('fileChip').classList.add('hidden');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showError(msg) {
  const el = document.getElementById('errorMsg');
  document.getElementById('errorText').textContent = msg;
  el.classList.remove('hidden');
}
function hideError() {
  document.getElementById('errorMsg').classList.add('hidden');
}
