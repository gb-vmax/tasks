# Bug Report

### Describe the bug

When processing markdown with line breaks, the text following a break is not being trimmed correctly. It seems like the whitespace trimming logic is off by one, causing leading whitespace to remain in the output when it should be removed.

### Reproduction

```js
// Example markdown input with a break
const markdown = `
First line  
Second line with leading space
`;

// After processing through remark-rehype
// Expected: "Second line with leading space" (trimmed)
// Actual: " Second line with leading space" (not trimmed)
```

The issue appears when converting markdown to HTML - text nodes that come after break elements are not having their leading whitespace properly trimmed.

### Expected behavior

Text following a line break should have leading markdown whitespace trimmed, just like it did in previous versions. The output should be clean without unexpected leading spaces.

### Additional context

This seems to have started happening recently. The whitespace handling after breaks was working fine before but now leaves extra spaces in the rendered output.

---
Repository: /testbed
