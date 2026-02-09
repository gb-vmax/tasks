# Bug Report

### Describe the bug

I'm encountering an issue with container directive labels in remark-directive. When parsing container directives with labels, the label content isn't being properly processed or associated with the directive node.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note[Important Information]
This is a note with a label
:::
`

const ast = processor.parse(markdown)
const result = processor.runSync(ast)

// The label "Important Information" is not correctly attached to the container directive node
console.log(result)
```

### Expected behavior

The container directive should have its label properly parsed and included in the AST. The label text should be accessible as part of the directive node structure.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
