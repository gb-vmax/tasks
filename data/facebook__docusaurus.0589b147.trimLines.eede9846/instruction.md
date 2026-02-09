# Bug Report

### Describe the bug

I'm encountering an issue with line trimming in code blocks. When processing markdown content that starts at the very beginning (position 0), the first line is not being trimmed correctly. It seems like the trimming logic is skipping the initial line when it should be processing it.

### Reproduction

```js
// Markdown content that starts immediately without any preceding content
const markdown = `code line 1
code line 2
code line 3`;

// Process this through remark-rehype
// Expected: all lines should be trimmed consistently
// Actual: the first line doesn't get trimmed properly
```

The issue appears when the content begins at index 0. Lines that come after work fine, but that very first line at position 0 doesn't get the same trimming treatment.

### Expected behavior

All lines should be trimmed consistently regardless of their position in the source. The first line starting at index 0 should be treated the same way as subsequent lines.

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest

---
Repository: /testbed
