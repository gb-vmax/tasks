# Bug Report

### Describe the bug

I'm experiencing a crash when using MDX with certain markdown constructs. The error occurs during compilation and appears to be related to how tokens are being processed internally.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const content = `
# My Document

Some content here with specific markdown structures
`;

// This causes an error during compilation
const result = await mdx.compile(content);
```

The compilation fails with a TypeError about calling undefined as a function. This seems to happen when the compiler tries to process certain token types where an optional callback handler isn't provided.

### Expected behavior

The MDX compiler should handle cases where optional callback handlers are not defined, rather than attempting to call undefined functions. The compilation should complete successfully.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
