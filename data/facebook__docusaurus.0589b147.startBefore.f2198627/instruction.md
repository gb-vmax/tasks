# Bug Report

### Describe the bug

I'm encountering an infinite loop when parsing fenced code blocks with the remark parser. The parser seems to get stuck and never completes when processing certain markdown documents containing code fences.

### Reproduction

```js
const remark = require('remark');

const markdown = `
\`\`\`js
console.log('test');
\`\`\`
`;

// This hangs indefinitely
const result = remark.parse(markdown);
```

### Expected behavior

The parser should successfully parse the fenced code block and return the AST without hanging. The code fence closing should be properly detected and processing should complete normally.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The parser just hangs when it encounters the closing fence of a code block and never returns control.

---
Repository: /testbed
