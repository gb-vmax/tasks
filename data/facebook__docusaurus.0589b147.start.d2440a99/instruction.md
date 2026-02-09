# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark-directive where the token sequence appears to be incorrect. When parsing leaf directives (like `:directive[content]`), the tokenizer seems to be creating tokens in the wrong order, which causes problems with the AST structure.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const result = processor.parse(':test[content]')
console.log(result)
```

When inspecting the token stream, the `directiveLeaf` and `directiveLeafSequence` tokens appear in an unexpected order, which breaks downstream processing that relies on the correct token hierarchy.

### Expected behavior

The tokenizer should emit tokens in the proper sequence where `directiveLeaf` is the parent token and `directiveLeafSequence` is nested within it. This is how other similar constructs in the parser work and what consumers of the token stream expect.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
