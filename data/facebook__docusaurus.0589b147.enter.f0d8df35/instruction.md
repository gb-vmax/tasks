# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where the `type` property is missing from directive nodes. After parsing markdown with directives (text, leaf, or container directives), the resulting AST nodes don't have the expected `type` field set correctly.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const result = processor.parse(':directive[content]')

// The directive node is missing its type property
console.log(result)
// Expected: node with type: 'textDirective'
// Actual: node without type field or incorrect type
```

### Expected behavior

Directive nodes should have their `type` property properly set to `'textDirective'`, `'leafDirective'`, or `'containerDirective'` depending on the directive syntax used. The AST structure should include this type information for proper node identification.

### Additional context

This affects all three directive types:
- Text directives: `:name[content]`
- Leaf directives: `::name[content]`
- Container directives: `:::name[content]`

The parsed nodes are missing the type discriminator which makes it impossible to distinguish between different directive types in the AST.

---
Repository: /testbed
