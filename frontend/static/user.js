const ratingInput = document.getElementById("rating");
const ratingStars = document.getElementById("rating-stars");
const reviewInput = document.getElementById("review");
const charCount = document.getElementById("char-count");
const messageBox = document.getElementById("message");
const submitBtn = document.getElementById("submit-btn");
const form = document.getElementById("review-form");
const aiSection = document.getElementById("ai-response-section");
const aiText = document.getElementById("ai-response-text");

let selectedRating = 0;

function setMessage(type, text) {
  messageBox.classList.remove("hidden", "error", "success", "info");
  messageBox.textContent = text;
  if (type) {
    messageBox.classList.add(type);
  }
}

function clearMessage() {
  messageBox.classList.add("hidden");
  messageBox.textContent = "";
  messageBox.classList.remove("error", "success", "info");
}

// Rating selection
ratingStars.addEventListener("click", (event) => {
  if (event.target.matches(".star")) {
    const value = Number(event.target.dataset.value || "0");
    selectedRating = value;
    ratingInput.value = String(value);

    document.querySelectorAll(".star").forEach((star) => {
      const v = Number(star.dataset.value || "0");
      star.classList.toggle("selected", v <= value);
    });
  }
});

// Character count
reviewInput.addEventListener("input", () => {
  charCount.textContent = String(reviewInput.value.length);
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!selectedRating) {
    setMessage("error", "Please select a rating between 1 and 5.");
    return;
  }

  clearMessage();
  aiSection.classList.add("hidden");
  aiText.textContent = "";

  submitBtn.disabled = true;
  submitBtn.textContent = "Submitting...";

  const payload = {
    rating: selectedRating,
    review: reviewInput.value.trim(),
  };

  try {
    const res = await fetch("/api/reviews", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await res.json();

    if (!res.ok || !data.success) {
      throw new Error(data.error || "Failed to submit review.");
    }

    setMessage("success", "Thank you! Your review has been submitted.");

    if (data.data && data.data.ai_response) {
      aiText.textContent = data.data.ai_response;
      aiSection.classList.remove("hidden");
    }

    // Reset form
    selectedRating = 0;
    ratingInput.value = "";
    document.querySelectorAll(".star").forEach((star) => {
      star.classList.remove("selected");
    });
    reviewInput.value = "";
    charCount.textContent = "0";
  } catch (err) {
    console.error(err);
    setMessage(
      "error",
      err instanceof Error
        ? err.message
        : "Something went wrong. Please try again."
    );
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Submit Review";
  }
});

