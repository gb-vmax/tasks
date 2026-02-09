# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where it crashes when processing certain document structures. The error occurs when trying to close flow content in nested containers.

### Reproduction

```js
const remark = require('remark');

const markdown = `
> Block quote
> with multiple lines
`;

// This triggers the crash
remark.parse(markdown);
```

The parser throws an error because it's trying to call a method on an undefined object. This happens specifically when closing flow content in container blocks like blockquotes or list items.

### Expected behavior

The markdown should parse successfully without throwing errors. The parser should properly handle closing flow content even in nested container structures.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
