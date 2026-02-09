# Bug Report

### Describe the bug

I'm experiencing an issue where the parser validation is failing unexpectedly. When trying to use a parser function with the unified processor, I'm getting a TypeError saying "Cannot `[operation]` without `parser`" even though I've provided a valid parser function.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');

// This throws an error even though remarkParse is a valid parser function
const processor = unified()
  .use(remarkParse)
  .parse('# Hello world');
```

The error message indicates that no parser was provided, but I'm clearly passing a parser function to `.use()`.

### Expected behavior

The processor should accept the parser function and successfully parse the markdown content without throwing a TypeError about missing parser.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The same code was working fine before.

---
Repository: /testbed
