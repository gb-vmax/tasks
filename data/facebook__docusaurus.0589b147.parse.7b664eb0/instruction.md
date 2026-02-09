# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to be initializing incorrectly. The parsed output is either malformed or the parser throws errors when processing certain markdown constructs.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello

This is a test document with some **bold** text.

- Item 1
- Item 2
`;

const result = remark.parse(markdown);
console.log(result);
```

When running this code, the parser behavior is inconsistent. Sometimes it works, sometimes it fails to properly tokenize the content. The issue seems to be related to how the parser initializes its internal tokenizer.

### Expected behavior

The markdown should be parsed correctly and consistently, producing a valid AST structure for all standard markdown constructs (headings, lists, emphasis, etc.).

### Additional context

This started happening recently and I'm not sure what changed. The parser seems to have trouble with the initialization phase before it even starts processing the actual markdown content.

---
Repository: /testbed
