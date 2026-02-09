# Bug Report

### Describe the bug

I'm experiencing an issue with text processing in MDX where newline characters are being included incorrectly when trimming lines. It appears that the line slicing logic is off by one character, causing newlines to be duplicated or improperly handled in the output.

### Reproduction

```js
const input = `
  Line 1
  Line 2
  Line 3
`;

// Process the input through MDX
const result = compile(input);

// Expected: properly trimmed lines without extra newlines
// Actual: newlines are duplicated or positioned incorrectly
```

When processing multi-line MDX content with whitespace, the output contains extra newline characters or has them in the wrong positions. This affects the rendered output formatting.

### Expected behavior

Lines should be trimmed correctly without including extra newline characters from the regex match boundaries. The output should maintain proper line breaks without duplication.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
