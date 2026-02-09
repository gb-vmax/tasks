# Bug Report

### Describe the bug

I'm experiencing an issue with container directive labels in remark-directive. When parsing container directives with labels, the label content is not being properly recognized as a paragraph element. Instead, it appears to be treated as a generic container type.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note[Important Note]
This is the content
:::
`

const ast = processor.parse(markdown)
const result = processor.runSync(ast)

// The label node should be a paragraph but it's showing as container
console.log(result.children[0].children[0].type) // Expected: 'paragraph', Actual: 'container'
```

### Expected behavior

The label portion of a container directive (the text in square brackets) should be parsed as a `paragraph` node with `directiveLabel: true` in its data property. This is important for proper rendering and styling of directive labels.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This seems like it might be a regression as I didn't notice this behavior in earlier versions. The label metadata flag also appears to be set incorrectly.

---
Repository: /testbed
