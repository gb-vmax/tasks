# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where it crashes with a "Maximum call stack size exceeded" error when processing markdown documents. This appears to be happening during the flow parsing stage.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Heading

Some paragraph text here.

- List item 1
- List item 2
`

const processor = remark()
const result = processor.parse(markdown) // RangeError: Maximum call stack size exceeded
```

### Expected behavior

The markdown should be parsed successfully without any stack overflow errors. This was working fine in previous versions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
