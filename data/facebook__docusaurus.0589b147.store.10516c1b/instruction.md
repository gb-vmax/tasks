# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer's state restoration is not working correctly. When the parser backtracks and needs to restore a previous state, the events array appears to be corrupted, causing parsing errors or unexpected behavior.

### Reproduction

```js
// Parse MDX content that requires backtracking
const mdxContent = `
# Heading

Some text with **bold** and *italic* formatting.

\`\`\`js
code block
\`\`\`
`;

// The parser should handle this correctly, but instead
// the events array gets into an inconsistent state
const result = compile(mdxContent);
```

### Expected behavior

The parser should correctly restore its state when backtracking during tokenization. The events array should be properly reset to its previous state without any corruption or off-by-one errors.

### Additional context

This seems to happen specifically when the tokenizer needs to restore state after attempting a construct that doesn't match. The restoration process appears to leave the events array in an incorrect state, which cascades into further parsing issues.

---
Repository: /testbed
