# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser when using multiple extensions together. When I pass an array of extensions, they don't seem to be applied correctly and the parsing behavior is completely broken.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkGfm = require('remark-gfm');

const processor = unified()
  .use(remarkParse)
  .use([[remarkGfm, otherExtension]]);

const result = processor.processSync('# Hello');
// Extensions are not being applied properly
```

When I try to use nested arrays of extensions (which should be supported based on the docs), the parser fails to process the markdown correctly. It seems like the extensions aren't being configured in the right order or at all.

### Expected behavior

The parser should correctly apply all extensions in the array, regardless of nesting level. The configuration should recursively process nested arrays and apply each extension properly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
