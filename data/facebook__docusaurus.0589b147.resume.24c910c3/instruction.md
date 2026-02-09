# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown lists where the output is getting corrupted. When processing ordered or unordered lists, the generated content appears to be missing or incorrectly structured.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
1. First item
2. Second item
3. Third item
`;

const result = processor.processSync(markdown);
console.log(result.toString());
```

### Expected behavior

The markdown list should be parsed and converted correctly, preserving all list items in the output. Instead, some list items appear to be missing or the structure is malformed.

This seems to have started happening recently - the same code was working fine before. The issue occurs with both ordered and unordered lists.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
