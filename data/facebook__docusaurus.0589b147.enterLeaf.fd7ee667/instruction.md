# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in remark-directive. When processing markdown with leaf directives (like `::note`), the parser seems to be crashing or producing incorrect output. The text and container directives work fine, but specifically leaf directives are broken.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
::note
This is a leaf directive
`

const result = processor.processSync(markdown)
// Error occurs when processing leaf directives
```

### Expected behavior

Leaf directives should be parsed correctly just like text directives and container directives. The AST should contain a proper `leafDirective` node with the correct structure.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This seems to have started recently. Container and text directives are working as expected, but leaf directives specifically are failing.

---
Repository: /testbed
