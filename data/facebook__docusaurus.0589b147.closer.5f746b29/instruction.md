# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain nested structures are not being processed correctly. When parsing markdown with specific token patterns, the parser seems to fail silently or produce malformed output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Header

Some text with **bold** and *italic* formatting.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result);
```

After parsing, the AST structure appears corrupted or incomplete. Nested formatting elements within list items or other block-level structures don't seem to be closed properly.

### Expected behavior

The markdown should be parsed into a valid AST with all tokens properly opened and closed. Nested structures should maintain their hierarchy correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Not sure if this is related to any recent changes but wanted to report it.

---
Repository: /testbed
