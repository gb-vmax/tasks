# Bug Report

### Describe the bug

I'm experiencing an issue with container directive labels in remark-directive. When parsing a container directive with a label, the label content is being wrapped in an incorrect node type, which breaks the expected AST structure.

### Reproduction

```js
import {fromMarkdown} from 'mdast-util-from-markdown'
import {directiveFromMarkdown} from 'mdast-util-directive'
import {directive} from 'micromark-extension-directive'

const doc = `
:::note[This is a label]
Content here
:::
`

const tree = fromMarkdown(doc, {
  extensions: [directive()],
  mdastExtensions: [directiveFromMarkdown()]
})

console.log(tree.children[0].children[0])
// Expected: { type: 'paragraph', ... }
// Actual: { type: 'container', ... }
```

### Expected behavior

The label of a container directive should be parsed as a `paragraph` node with `data.directiveLabel` set to `true`, maintaining consistency with how directive labels are typically structured in the AST.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This seems to affect how downstream processors handle container directive labels, as they expect a paragraph node but receive a container node instead.

---
Repository: /testbed
