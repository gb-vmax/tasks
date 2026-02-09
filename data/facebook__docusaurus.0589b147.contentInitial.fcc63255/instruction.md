# Bug Report

### Describe the bug

After a recent update, the markdown parser is throwing an error when trying to process content. It appears that something in the content initialization is broken and causing the parser to fail completely.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World')
```

This code now throws an error instead of successfully parsing the markdown content.

### Expected behavior

The markdown should be parsed without errors and return the expected AST structure. This was working fine in previous versions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
