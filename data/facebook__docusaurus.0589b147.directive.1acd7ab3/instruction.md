# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark. After a recent update, text directives (using `:directive` syntax) are no longer being recognized or processed correctly. The parser seems to be ignoring them completely.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = 'This is a :textDirective[with content]'
const result = processor.parse(markdown)

// Text directive is not parsed as a directive node
console.log(result)
```

### Expected behavior

Text directives should be parsed and appear as directive nodes in the AST. Previously this was working fine, but now the directive syntax is being treated as plain text.

Container and leaf directives (using `::` and `:::`) still seem to work, but single colon text directives are broken.

### System Info
- remark-directive: 3.0.0
- Node: 18.x

---
Repository: /testbed
