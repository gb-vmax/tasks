# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser seems to hang or enter an infinite loop when processing certain markdown documents. The parsing never completes and the process becomes unresponsive.

### Reproduction

```js
const markdown = `
# Test Document

Some content here.
`;

const result = remark().parse(markdown);
// Parser hangs and never returns
```

This seems to happen specifically when the markdown ends with a newline character. The parser gets stuck in what appears to be an infinite loop during the flow continuation phase.

### Expected behavior

The parser should complete successfully and return the parsed AST without hanging, regardless of how the document ends.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
