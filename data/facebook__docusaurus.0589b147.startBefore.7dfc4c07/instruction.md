# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing where the tokenizer gets stuck in an infinite loop. When processing fenced code blocks in MDX content, the parser hangs and never completes.

### Reproduction

```js
const mdxContent = `
\`\`\`javascript
const example = 'test';
\`\`\`
`;

// Parser hangs when processing this content
const result = compile(mdxContent);
```

### Expected behavior

The parser should successfully tokenize the fenced code block and complete processing without hanging. The code fence should be properly opened and closed.

### Additional context

This seems to happen specifically with the line ending handling in the fence tokenizer. The process becomes unresponsive when it encounters the closing fence of a code block.

---
Repository: /testbed
