# Bug Report

### Describe the bug

I'm experiencing issues with the markdown parser after a recent update. When trying to parse markdown content, the parser seems to be initializing incorrectly and fails to process the input properly.

### Reproduction

```js
const remark = require('remark');

const processor = remark();
const result = processor.processSync('# Hello World\n\nThis is a test.');

console.log(result);
```

The parser doesn't seem to be handling the markdown input correctly. It looks like there might be an issue with how the tokenizer is being created or initialized - the arguments seem to be getting passed in the wrong order or something similar.

### Expected behavior

The markdown should be parsed correctly and converted to an AST representation. The processor should handle standard markdown syntax without errors.

### System Info
- remark version: 15.0.1
- Node version: 18.x

Has anyone else run into this? It was working fine before the latest changes.

---
Repository: /testbed
