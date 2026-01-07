const statsLoading = document.getElementById("stats-loading");
const statsContent = document.getElementById("stats-content");
const totalReviewsEl = document.getElementById("total-reviews");
const averageRatingEl = document.getElementById("average-rating");
const ratingBreakdownEl = document.getElementById("rating-breakdown");

const adminMessage = document.getElementById("admin-message");
const reviewsLoading = document.getElementById("reviews-loading");
const reviewsList = document.getElementById("reviews-list");

const filterButtons = document.querySelectorAll(".filter-btn");

let refreshIntervalId = null;
let allReviews = [];
let currentFilter = "all";

function setAdminMessage(type, text) {
  adminMessage.classList.remove("hidden", "error", "success", "info");
  adminMessage.textContent = text;
  if (type) {
    adminMessage.classList.add(type);
  }
}

function clearAdminMessage() {
  adminMessage.classList.add("hidden");
  adminMessage.textContent = "";
  adminMessage.classList.remove("error", "success", "info");
}

function formatDate(dateStr) {
  const d = new Date(dateStr);
  if (Number.isNaN(d.getTime())) return dateStr;
  return d.toLocaleString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function renderStats(stats) {
  statsLoading.classList.add("hidden");
  statsContent.classList.remove("hidden");

  totalReviewsEl.textContent = String(stats.total);
  averageRatingEl.textContent = stats.average_rating.toFixed(1);

  ratingBreakdownEl.innerHTML = "";
  const total = stats.total || 0;

  for (const row of stats.by_rating) {
    const container = document.createElement("div");
    container.className = "rating-row";

    const label = document.createElement("div");
    label.className = "rating-label";
    label.textContent = `${row.rating}★`;

    const bar = document.createElement("div");
    bar.className = "rating-bar";
    const fill = document.createElement("div");
    fill.className = "rating-fill";
    const pct = total ? (row.count / total) * 100 : 0;
    fill.style.width = `${pct}%`;
    bar.appendChild(fill);

    const count = document.createElement("div");
    count.className = "rating-count";
    count.textContent = String(row.count);

    container.appendChild(label);
    container.appendChild(bar);
    container.appendChild(count);
    ratingBreakdownEl.appendChild(container);
  }
}

function renderReviews() {
  const ratingFilter =
    currentFilter === "all" ? null : Number.parseInt(currentFilter, 10);
  const data =
    ratingFilter == null
      ? allReviews
      : allReviews.filter((r) => r.rating === ratingFilter);

  reviewsLoading.classList.add("hidden");
  reviewsList.classList.remove("hidden");
  reviewsList.innerHTML = "";

  if (!data.length) {
    setAdminMessage("info", "No reviews found for the selected filter.");
    return;
  }

  clearAdminMessage();

  for (const review of data) {
    const item = document.createElement("div");
    item.className = "review-item";

    const header = document.createElement("div");
    header.className = "review-header";

    const rating = document.createElement("div");
    rating.className = "review-rating";
    rating.textContent = "★".repeat(review.rating);

    const date = document.createElement("div");
    date.className = "review-date";
    date.textContent = formatDate(review.created_at);

    header.appendChild(rating);
    header.appendChild(date);
    item.appendChild(header);

    const text = document.createElement("div");
    text.className = "review-text";
    if (review.review && review.review.trim()) {
      text.textContent = review.review;
    } else {
      text.textContent = "No written review provided.";
      text.classList.add("empty");
    }
    item.appendChild(text);

    const aiSummary = document.createElement("div");
    aiSummary.className = "ai-block";
    aiSummary.innerHTML = `<h4>AI Summary</h4><p>${review.ai_summary}</p>`;

    const aiActions = document.createElement("div");
    aiActions.className = "ai-block";
    aiActions.innerHTML = `<h4>AI Recommended Actions</h4><p>${review.ai_recommended_actions}</p>`;

    const aiResponse = document.createElement("div");
    aiResponse.className = "ai-block";
    aiResponse.innerHTML = `<h4>AI Response Shown to User</h4><p>${review.ai_response}</p>`;

    item.appendChild(aiSummary);
    item.appendChild(aiActions);
    item.appendChild(aiResponse);

    reviewsList.appendChild(item);
  }
}

async function loadStats() {
  try {
    const res = await fetch("/api/stats");
    const data = await res.json();
    if (!res.ok || !data.success) {
      throw new Error(data.error || "Failed to load stats.");
    }
    if (data.data) {
      renderStats(data.data);
    }
  } catch (err) {
    console.error(err);
    statsLoading.textContent =
      err instanceof Error ? err.message : "Failed to load stats.";
  }
}

async function loadReviews() {
  try {
    const res = await fetch("/api/reviews");
    const data = await res.json();
    if (!res.ok || !data.success) {
      throw new Error(data.error || "Failed to load reviews.");
    }
    allReviews = data.data || [];
    renderReviews();
  } catch (err) {
    console.error(err);
    reviewsLoading.textContent =
      err instanceof Error ? err.message : "Failed to load reviews.";
  }
}

async function refreshAll() {
  await Promise.all([loadStats(), loadReviews()]);
}

filterButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    filterButtons.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentFilter = btn.dataset.rating || "all";
    renderReviews();
  });
});

// Initial load
refreshAll();
refreshIntervalId = setInterval(refreshAll, 5000);

