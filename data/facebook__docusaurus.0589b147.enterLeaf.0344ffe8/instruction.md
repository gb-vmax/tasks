# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in remark-directive. When parsing markdown with leaf directives, the parser seems to fail or produce incorrect AST nodes. The directive syntax is being recognized but the resulting node type appears to be wrong.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
::my-directive[content]
`

const ast = processor.parse(markdown)
// The AST node type for the leaf directive is incorrect
console.log(ast)
```

### Expected behavior

Leaf directives should be parsed correctly and create proper AST nodes with type `leafDirective`. The parser should handle the syntax `::directive[content]` without issues.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
