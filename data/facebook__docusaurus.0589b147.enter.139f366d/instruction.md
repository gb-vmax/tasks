# Bug Report

### Describe the bug

I'm encountering an issue with text directives in remark where the directive nodes are missing their `type` property. This causes problems when processing the AST as the node type information is lost.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = ':directive[content]'
const ast = processor.parse(markdown)
processor.runSync(ast)

// The textDirective node is missing its type property
// Expected: { type: 'textDirective', name: 'directive', ... }
// Actual: { name: 'directive', attributes: {...}, children: [...] }
```

### Expected behavior

Text directive nodes should include a `type` property set to `"textDirective"` so they can be properly identified and processed in the AST. The node structure should match the expected mdast format.

### Additional context

This seems to affect text directives specifically. The node structure is incomplete without the type information, making it difficult to traverse and transform the syntax tree correctly.

---
Repository: /testbed
