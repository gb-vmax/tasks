# Bug Report

### Describe the bug

When parsing fenced code blocks with metadata, the parser enters an infinite loop or produces incorrect output. The issue appears when processing the metadata section after the language identifier in code fences.

### Reproduction

```js
const markdown = `
\`\`\`javascript some metadata here
console.log('test');
\`\`\`
`;

// Parser hangs or produces unexpected results
const result = processor.processSync(markdown);
```

### Expected behavior

The parser should correctly handle code fence metadata and complete processing without hanging. The metadata should be properly tokenized and the code block should be parsed normally.

### Additional context

This seems to affect code blocks that have additional metadata/parameters after the language identifier. Regular code blocks without metadata work fine.

---
Repository: /testbed
