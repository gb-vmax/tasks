# Bug Report

### Describe the bug

When converting markdown AST back to markdown text, the output formatting is incorrect. Content that should be treated as phrasing content (inline elements like text, emphasis, links, etc.) is being handled as flow content (block-level elements), resulting in unexpected line breaks and formatting issues.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `Hello *world* and [link](url)`

const processor = remark()
const tree = processor.parse(markdown)
const output = processor.stringify(tree)

console.log(output)
// Expected: Hello *world* and [link](url)
// Actual: Content is formatted with incorrect spacing/breaks
```

Another example with mixed content:

```js
const markdown = `Some text with **bold** and _italic_`
const tree = processor.parse(markdown)
const result = processor.stringify(tree)

// The inline formatting gets treated as block-level content
```

### Expected behavior

Inline/phrasing content should remain inline when converting the AST back to markdown. The formatter should correctly identify when a document contains phrasing elements and handle them appropriately without adding unnecessary line breaks.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
