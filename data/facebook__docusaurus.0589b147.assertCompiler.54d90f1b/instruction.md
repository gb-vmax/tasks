# Bug Report

### Describe the bug

After a recent update, the remark processor is throwing incorrect type errors when trying to use a compiler function. The error message says "Cannot `[operation]` with invalid `compiler`" even when a valid compiler function is provided.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkStringify = require('remark-stringify');

const processor = unified()
  .use(remarkParse)
  .use(remarkStringify);

// This throws an error about invalid compiler
const result = processor.processSync('# Hello World');
```

### Expected behavior

The processor should accept a function as a compiler and process the markdown content without throwing a type error. The compiler validation should check for `typeof value === "function"` rather than rejecting valid function compilers.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
