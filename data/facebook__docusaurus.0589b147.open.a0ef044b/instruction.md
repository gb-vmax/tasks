# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where the order of operations during token processing seems to have changed. When parsing markdown content, the `and` callback is now being invoked before the `enter` call, which is causing problems with the AST construction.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Heading

Some text with **bold** content.
`;

const result = remark().parse(markdown);
// The AST structure is incorrect - nodes are being processed in the wrong order
```

### Expected behavior

The `enter` call should happen first to establish the context before any additional callbacks (`and`) are executed. This ensures that the AST node is properly initialized before any follow-up operations are performed on it.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
