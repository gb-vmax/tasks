# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser seems to hang or behave incorrectly when processing documents that end with certain flow content. The problem appears to be related to how null code points are handled during flow parsing.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// This causes unexpected behavior
const markdown = `
# Heading

Some content here
`;

const result = processor.processSync(markdown);
```

When parsing documents with flow content at the end, the parser doesn't properly clean up or exit containers. This leads to either the parser getting stuck or producing incorrect output.

### Expected behavior

The parser should correctly handle the end of flow content and properly exit all containers before finishing. Documents with trailing flow content should parse successfully without hanging or producing malformed AST output.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
