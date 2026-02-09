# Bug Report

### Describe the bug

The broken link error messages are showing incorrect information. When a broken link is detected, the message displays the resolved link instead of the original link, and the condition for showing the resolved link seems inverted.

### Reproduction

When Docusaurus detects a broken link, the error message format appears to be backwards:

1. Create a broken link in your documentation (e.g., `[test](/nonexistent-page)`)
2. Build the site with broken link detection enabled
3. Observe the error message

### Expected behavior

The error message should display:
- The **original link** as the primary message (e.g., `/nonexistent-page`)
- The resolved link in parentheses when it differs from the original (e.g., `(resolved as: /nonexistent-page.html)`)

### Current behavior

Instead, the message appears to show:
- The resolved link as the primary message
- The original link shown when they are the same (which doesn't make sense)
- The condition seems backwards - it shows additional info when the links match instead of when they differ

This makes debugging broken links confusing because you see the resolved path instead of what you actually wrote in your markdown files.

---
Repository: /testbed
