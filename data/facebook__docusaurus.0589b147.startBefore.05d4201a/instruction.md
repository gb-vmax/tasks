# Bug Report

### Describe the bug

I'm experiencing an issue with parsing fenced code blocks in markdown. When processing code blocks with closing fences, the parser seems to get stuck in an infinite loop or doesn't properly exit the line ending state.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`
`;

// Parse the markdown with fenced code blocks
// The parser hangs or doesn't complete properly
```

### Expected behavior

The parser should correctly handle the closing fence of code blocks and properly transition through the tokenization states. The line ending should be consumed and the parser should move to the next state to continue processing the closing fence.

### Additional context

This seems to affect any markdown content with fenced code blocks. The issue appears to be related to how the tokenizer handles line endings before closing code fences.

---
Repository: /testbed
