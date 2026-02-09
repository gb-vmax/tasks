# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When processing code blocks, the content appears to be duplicated or processed incorrectly, leading to unexpected behavior in the rendered output.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parse the markdown with fenced code block
const result = remark().parse(markdown);
// The code block content is not handled correctly
```

### Expected behavior

Fenced code blocks should be parsed correctly with their content appearing once in the output. The tokenizer should properly handle the code flow value without duplication or incorrect processing.

### Additional context

This seems to be related to how the `beforeContentChunk` function handles code blocks. The issue appears when the code block has content that needs to be tokenized - the content processing logic doesn't seem to be working as expected.

---
Repository: /testbed
