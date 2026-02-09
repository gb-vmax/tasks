# Bug Report

### Describe the bug

When processing markdown files with remark, the processor seems to be returning `undefined` or incorrect results instead of the transformed tree. The transformation appears to complete without errors, but the output is not what's expected.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const file = '# Hello World\n\nThis is a test.'

// Process the markdown
const result = await processor.process(file)

// Expected: result should contain the transformed tree
// Actual: result is undefined or not the expected tree structure
console.log(result) // undefined or incorrect output
```

### Expected behavior

The processor should return the properly transformed syntax tree after processing. When using async/await with `process()`, the result should contain the full transformed tree structure.

### Additional context

This seems to affect both callback-based and promise-based usage of the processor. The transformation runs without throwing errors, but the resulting output is not correct.

---
Repository: /testbed
