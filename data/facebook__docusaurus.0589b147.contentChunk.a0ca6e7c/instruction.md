# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When parsing code blocks with content, the parser seems to be consuming characters in the wrong order, which causes the `codeFlowValue` token to be exited at incorrect positions.

### Reproduction

```js
const markdown = `\`\`\`js
console.log('test');
\`\`\``;

// Parse the markdown
const result = remark().parse(markdown);
```

When parsing fenced code blocks, the tokenizer appears to exit the `codeFlowValue` state before properly processing all the content characters. This leads to malformed AST nodes or incorrect token boundaries.

### Expected behavior

The parser should:
1. Consume each character in the code block content
2. Check for line endings or null termination
3. Exit the `codeFlowValue` token only after all content is properly consumed
4. Maintain correct token boundaries throughout the parsing process

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to be affecting the order of operations in the `contentChunk` function within the code fence tokenizer. The token exit is happening at the wrong point in the flow.

---
Repository: /testbed
