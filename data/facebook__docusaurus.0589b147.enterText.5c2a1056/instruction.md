# Bug Report

### Describe the bug

Text directives are not being parsed correctly in markdown. When using inline text directives (`:directive[content]`), they appear to be processed as regular text nodes instead of being recognized as `textDirective` nodes in the AST.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const result = processor.parse(':myDirective[some text]')

// The AST should contain a textDirective node
// but instead contains a text node
console.log(result)
```

### Expected behavior

The parser should create a `textDirective` node with type `'textDirective'` for inline directives. Instead, it's creating nodes with type `'text'`.

This affects any markdown content that uses inline text directives - they're no longer being processed as directives at all.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
