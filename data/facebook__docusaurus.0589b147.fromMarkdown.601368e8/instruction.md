# Bug Report

### Describe the bug
The markdown parser is not correctly processing input when converting markdown to AST. It seems like the preprocessing and postprocessing steps are being applied in the wrong order, which causes the parser to fail on certain markdown inputs.

### Reproduction
```js
import {fromMarkdown} from 'remark'

const markdown = `
# Hello World

This is a test with **bold** and *italic* text.
`

const result = fromMarkdown(markdown)
console.log(result)
```

When running this, the output is malformed or throws an error instead of returning a proper AST structure.

### Expected behavior
The `fromMarkdown` function should correctly parse the markdown input and return a valid AST that represents the document structure with all preprocessing and postprocessing applied in the correct sequence.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
