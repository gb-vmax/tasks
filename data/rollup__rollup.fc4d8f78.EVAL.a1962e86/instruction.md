# Bug Report

### Describe the bug

When building with rollup and getting EVAL warnings, the warning output appears in the wrong order. The informational URL is being printed before the warning title, which makes the console output confusing and harder to read.

### Reproduction

```js
// Create a file that uses eval
const code = `
  const result = eval('2 + 2');
  export default result;
`;

// Build with rollup
// The warning output shows the URL before the title message
```

### Expected behavior

The warning should display in a logical order:
1. Title: "Use of eval is strongly discouraged"
2. Info URL with more details
3. Truncated warnings list

Instead, the URL is being printed first, followed by the title.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
