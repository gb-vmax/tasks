# Bug Report

### Describe the bug

I'm experiencing an issue with the `strong` function in remark-rehype where it seems to be applying data incorrectly. When processing markdown with bold/strong text that has custom data attributes, the data isn't being properly transferred to the resulting HTML AST node.

### Reproduction

```js
const unified = require('unified')
const markdown = require('remark-parse')
const remark2rehype = require('remark-rehype')

const processor = unified()
  .use(markdown)
  .use(remark2rehype)

// Process markdown with strong/bold text
const mdast = processor.parse('**bold text**')

// Add custom data to the strong node
mdast.children[0].children[0].data = {
  hProperties: {
    className: ['custom-bold']
  }
}

const hast = processor.runSync(mdast)

// The resulting HTML node doesn't have the expected properties
console.log(hast.children[0].children[0])
// Expected: properties should include className: ['custom-bold']
// Actual: properties are missing or incorrect
```

### Expected behavior

Custom data attributes attached to strong/bold markdown nodes should be properly transferred to the resulting HTML strong elements. The `data.hProperties` should be applied to the final node's properties.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
