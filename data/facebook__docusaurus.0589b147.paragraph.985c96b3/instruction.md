# Bug Report

### Describe the bug

I'm experiencing an issue with paragraph rendering in remark-rehype where the `applyData` function appears to be receiving arguments in the wrong order. When processing markdown paragraphs with custom data attributes, the transformation is not applying the data correctly to the resulting HTML elements.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkRehype = require('remark-rehype')

const markdown = `
This is a paragraph with custom data.
`

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)

const result = processor.processSync(markdown)
```

When the paragraph node has custom data properties, they don't get applied to the resulting `<p>` element as expected. The data seems to be getting lost or applied incorrectly during the transformation.

### Expected behavior

Custom data attributes from the markdown AST node should be properly transferred to the HTML AST element. The `applyData` function should receive the target element first, then the source node, so that data can be correctly copied over.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
