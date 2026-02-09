# Bug Report

### Describe the bug

Getting a syntax error when trying to use the remark library. The code fails to parse/compile and throws an error about unexpected token. This appears to be affecting the entire markdown processing pipeline.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World')
console.log(result)
```

When running this code, it fails with a syntax error during module loading.

### Expected behavior

The remark processor should initialize successfully and be able to process markdown content without any syntax errors.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
