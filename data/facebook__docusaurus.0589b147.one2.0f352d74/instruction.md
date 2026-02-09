# Bug Report

### Describe the bug

I'm experiencing an issue where markdown parsing seems to fail silently. When trying to parse markdown content, the parser doesn't process the content at all and returns nothing instead of the expected AST.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World\n\nThis is a test.')

console.log(result)
// Expected: AST with heading and paragraph nodes
// Actual: undefined or no output
```

### Expected behavior

The markdown parser should process the input and return a proper AST structure with the heading and paragraph nodes. Instead, it appears to be returning early without processing anything.

### Additional context

This seems to have started happening recently. The parser was working fine before, but now it's like the processing logic is being skipped entirely. It's affecting all markdown parsing operations in my project.

---
Repository: /testbed
