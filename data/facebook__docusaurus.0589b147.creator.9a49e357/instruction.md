# Bug Report

### Describe the bug

The remark parser is causing a stack overflow error when trying to parse markdown content. The application crashes immediately when attempting to process any markdown input.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()

// This causes a stack overflow
const result = processor.processSync('# Hello World')
```

### Expected behavior

The markdown should be parsed successfully without any errors. The processor should return the parsed AST structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
