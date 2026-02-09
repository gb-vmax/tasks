# Bug Report

### Describe the bug

I'm encountering an issue with container directive label parsing in remark-directive. When using container directives with labels, the parser seems to be exiting the token incorrectly, which may cause issues with the AST structure or subsequent processing.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note[This is a label]
Content here
:::
`

const ast = processor.parse(markdown)
// The label node structure appears malformed
```

### Expected behavior

Container directive labels should be properly parsed and the AST should maintain correct parent-child relationships. The exit handler should properly close the label token context.

### Additional context

This seems to affect any container directive that uses the label syntax (e.g., `:::directive[label]`). The issue might be related to how the token exit is being handled in the label processing.

---
Repository: /testbed
