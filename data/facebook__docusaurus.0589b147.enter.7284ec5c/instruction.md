# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark-directive. When processing text directives, the parser appears to be passing incorrect arguments to the `enter` method, which causes the directive nodes to be malformed.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = ':textdirective[content]'
const ast = processor.parse(markdown)
const result = processor.runSync(ast)

console.log(result)
// Expected: proper directive node with type, name, attributes, children
// Actual: malformed node structure
```

### Expected behavior

The directive should be parsed into a proper AST node with the correct structure:
- `type` should be a string (e.g., 'textDirective')
- The node should have `name`, `attributes`, and `children` properties at the correct level
- Token information should be properly attached

### Actual behavior

The directive node structure appears incorrect, with properties not being set at the expected levels in the AST.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
