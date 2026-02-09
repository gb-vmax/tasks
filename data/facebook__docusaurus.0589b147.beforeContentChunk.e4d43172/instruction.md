# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I have a fenced code block with content, the parser seems to be handling the content incorrectly, causing unexpected behavior in how the code block is processed.

### Reproduction

```markdown
```js
const example = 'test';
console.log(example);
```
```

When parsing this markdown, the code block content is not being recognized properly. The parser appears to be treating line endings and content chunks in the wrong order.

### Expected behavior

The parser should correctly identify and process the content within fenced code blocks, properly handling both the content lines and line endings to maintain the structure of the code block.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started recently and is affecting how code blocks are rendered in my documentation. Any help would be appreciated!

---
Repository: /testbed
