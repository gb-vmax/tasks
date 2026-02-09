# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing where the initial prefix calculation seems to be incorrect. When parsing fenced code blocks, the prefix length is being computed in a way that doesn't match the expected behavior, which affects how the code blocks are being tokenized.

### Reproduction

```js
// When parsing markdown with fenced code blocks like:
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// The tokenizer calculates the initialPrefix incorrectly
// when the previous event type is "linePrefix"
```

The issue appears to be in the `beforeSequenceOpen` function where the `initialPrefix` is calculated based on the tail event. The condition for checking the event type seems backwards - it's checking for inequality (`!==`) when it should probably be checking for equality (`===`).

### Expected behavior

The `initialPrefix` should correctly reflect the length of the line prefix when present, and should be 0 when there is no line prefix. This affects the proper parsing and indentation handling of fenced code blocks.

### Additional context

This is affecting the rendering of code blocks in markdown documents, particularly when dealing with indented code fences or code blocks that follow other content with specific indentation.

---
Repository: /testbed
