# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in remark-directive. When parsing markdown that contains leaf directives (like `::directive`), the parser throws an error or produces incorrect output.

### Reproduction

```js
import {remark} from 'remark'
import remarkDirective from 'remark-directive'

const markdown = `
::note
This is a leaf directive
`

const result = remark()
  .use(remarkDirective)
  .processSync(markdown)

console.log(result)
```

When running this code, the leaf directive is not parsed correctly. The parser seems to fail when trying to handle the leaf directive token.

### Expected behavior

Leaf directives should be parsed correctly and the AST should contain a proper `leafDirective` node with the expected structure.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
