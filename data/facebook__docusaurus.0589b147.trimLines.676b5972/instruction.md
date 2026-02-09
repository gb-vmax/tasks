# Bug Report

### Describe the bug

I'm experiencing an issue with line trimming in code blocks. When processing markdown content with code blocks, the first line is being incorrectly trimmed even when it shouldn't be.

### Reproduction

```js
const markdown = `
\`\`\`
  first line with leading spaces
  second line
\`\`\`
`;

// After processing, the leading spaces on the first line are removed
// but they should be preserved
```

When the code block is processed, the leading whitespace on the first line gets stripped away, but subsequent lines maintain their indentation correctly. This makes the formatted code block look inconsistent.

### Expected behavior

All lines in the code block should have their leading/trailing whitespace handled consistently. The first line should preserve its leading spaces just like the other lines do.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
