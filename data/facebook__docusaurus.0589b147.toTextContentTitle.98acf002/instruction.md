# Bug Report

### Describe the bug

When using inline code blocks in markdown content titles, the backticks are being removed but the text inside is not being preserved correctly. Instead of showing the actual code text, the title shows a literal `<text>` placeholder.

### Reproduction

```markdown
---
title: Using `useState` hook
---

# Using `useState` hook
```

When this markdown is processed, the title becomes "Using <text> hook" instead of "Using useState hook".

### Expected behavior

The inline code formatting (backticks) should be stripped from the title, but the actual text content inside the backticks should be preserved. For example:
- Input: `Using \`useState\` hook`
- Expected output: `Using useState hook`
- Actual output: `Using <text> hook`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
