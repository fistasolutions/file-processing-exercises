# PR #57: Add user authentication system

**Author:** dev-student-2
**Branch:** feature-auth -> main
**Files Changed:** 8 files changed, +423 lines, -12 lines

## Description

Added a complete user authentication system with:
- JWT token generation and validation
- Password hashing with bcrypt
- Login/register endpoints
- Session management middleware
- Rate limiting on auth endpoints

## How It Was Built

I researched best practices for Python authentication and implemented
the system following OWASP guidelines.

## Testing

All tests pass. Manual testing completed.

---

## Reviewer Comments (Simulated)

> **security-lead**: "This is a really sophisticated auth implementation for someone who said they're a beginner. Did you use AI assistance? The code style in auth_middleware.py is very different from your previous PRs."

> **senior-dev**: "The JWT implementation looks correct but the error messages are extremely detailed and consistent — this reads like AI-generated code. Nothing wrong with using AI, but we need to know which parts to review more carefully."

> **teammate**: "I noticed the rate limiter uses an algorithm I've never seen you use before. Can you explain the token bucket implementation?"

---

## Your Task

This PR hides the fact that AI was used to generate most of the code.
That's a transparency problem, not a quality problem.

Rewrite the description to:
1. Clearly disclose which AI tools were used
2. Identify which specific parts were AI-generated
3. Explain how the author verified the AI output
4. Note any parts the author doesn't fully understand yet
5. Keep the technical description accurate

Save your improved description as `pr-2-improved.md` in this directory.
