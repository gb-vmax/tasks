# Bug Report

### Describe the bug

I'm experiencing an issue with the active doc detection in the docs plugin. When navigating to a page, the wrong document is being marked as active, particularly when dealing with nested routes or paths that are substrings of other paths.

### Reproduction

Let's say I have the following doc structure:
- `/docs/api` 
- `/docs/api/advanced`

When I navigate to `/docs/api`, both `/docs/api` and `/docs/api/advanced` are being matched as active documents. This causes the wrong sidebar items to be highlighted and incorrect version information to be displayed.

Steps to reproduce:
1. Create two docs where one path is a prefix of another (e.g., `api.md` and `api/advanced.md`)
2. Navigate to the shorter path (`/docs/api`)
3. Observe that the active doc context is incorrectly identifying multiple matches

### Expected behavior

Only the exact matching document should be marked as active. When I'm on `/docs/api`, only that specific doc should be in the active context, not `/docs/api/advanced`.

### Additional context

This seems to have started happening recently. The sidebar highlighting is now unreliable when you have nested documentation structures. It's particularly noticeable when switching between different versions of the docs.

---
Repository: /testbed
