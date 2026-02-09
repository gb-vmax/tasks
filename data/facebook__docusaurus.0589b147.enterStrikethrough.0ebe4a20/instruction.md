# Bug Report

### Describe the bug
When using strikethrough syntax in markdown (e.g., `~~text~~`), the text is being rendered as bold/strong instead of with strikethrough formatting. The markdown parser seems to be incorrectly converting strikethrough tokens to strong elements.

### Reproduction
```markdown
This is ~~strikethrough text~~ but it renders as bold.
```

Expected output should show the text with a line through it, but instead it appears as bold text.

### Steps to reproduce
1. Write markdown with strikethrough syntax using `~~` delimiters
2. Parse the markdown using remark-gfm
3. Observe that the strikethrough text is rendered as bold instead

### Expected behavior
Text wrapped in `~~` should be rendered with strikethrough styling (like `<del>` or `text-decoration: line-through`), not as bold/strong text.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
