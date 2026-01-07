import os
from typing import Dict

import httpx


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


async def generate_ai_content(rating: int, review: str) -> Dict[str, str]:
    """
    Call OpenRouter to generate:
    - user-facing response
    - internal summary
    - recommended actions

    Falls back to sensible defaults if API or key is unavailable.
    """

    # Fallbacks when no key is configured (e.g., local dev without AI)
    if not OPENROUTER_API_KEY:
        base_summary = (
            f"{rating}-star review"
            + (f": {review[:100]}..." if review else " without written feedback.")
        )
        if rating >= 4:
            actions = (
                "• Celebrate positive feedback\n"
                "• Share with the team\n"
                "• Consider featuring this in testimonials"
            )
        else:
            actions = (
                "• Review the feedback in detail\n"
                "• Follow up with the user if possible\n"
                "• Identify and track improvement actions"
            )

        return {
            "user_response": (
                "Thank you for your feedback! We truly appreciate you taking the time "
                "to share your experience with us."
            ),
            "summary": base_summary,
            "recommended_actions": actions,
        }

    user_prompt = (
        f"A user submitted a {rating}-star review"
        f"{f': \"{review}\"' if review else ' without written feedback'}.\n"
        "Write a brief, warm, professional response (2–3 sentences) that:\n"
        "- Thanks them for their feedback\n"
        "- Acknowledges their rating\n"
        "- Shows appreciation and openness to improvement.\n"
        "Respond as the business speaking to the customer."
    )

    summary_prompt = (
        f"Summarize this {rating}-star review in 1–2 concise sentences. "
        f"Review text: \"{review}\""
        if review
        else f"Summarize a {rating}-star review where the user did not leave written feedback."
    )

    actions_prompt = (
        f"Based on this {rating}-star review"
        f"{f': \"{review}\"' if review else ' (no written feedback)'}\n"
        "suggest 2–3 specific, actionable next steps for the business.\n"
        "Return them as a short bulleted list."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            # User-facing response
            user_res = await client.post(
                OPENROUTER_URL,
                headers=headers,
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": user_prompt}],
                },
            )
            user_res.raise_for_status()
            user_msg = (
                user_res.json()
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
                .strip()
            )

            # Summary
            summary_res = await client.post(
                OPENROUTER_URL,
                headers=headers,
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": summary_prompt}],
                },
            )
            summary_res.raise_for_status()
            summary_msg = (
                summary_res.json()
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
                .strip()
            )

            # Recommended actions
            actions_res = await client.post(
                OPENROUTER_URL,
                headers=headers,
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": actions_prompt}],
                },
            )
            actions_res.raise_for_status()
            actions_msg = (
                actions_res.json()
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
                .strip()
            )

        except Exception as exc:  # noqa: BLE001
            # Log and fall back
            print(f"[AI ERROR] {exc}")
            base_summary = (
                f"{rating}-star review"
                + (f": {review[:100]}..." if review else " without written feedback.")
            )
            if rating >= 4:
                actions_msg = (
                    "• Celebrate positive feedback\n"
                    "• Share with the team\n"
                    "• Consider featuring this in testimonials"
                )
            else:
                actions_msg = (
                    "• Review the feedback in detail\n"
                    "• Follow up with the user if possible\n"
                    "• Identify and track improvement actions"
                )

            return {
                "user_response": (
                    "Thank you for your feedback! We truly appreciate you taking the "
                    "time to share your experience with us."
                ),
                "summary": base_summary,
                "recommended_actions": actions_msg,
            }

    return {
        "user_response": (
            user_msg
            or "Thank you for your feedback! We appreciate you sharing your experience."
        ),
        "summary": (
            summary_msg
            or (
                f"{rating}-star review"
                + (f": {review[:100]}..." if review else " without written feedback.")
            )
        ),
        "recommended_actions": (
            actions_msg
            or "• Review feedback\n• Share with the team\n• Plan concrete improvements"
        ),
    }

