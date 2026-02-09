# Bug Report

### Describe the bug

I'm experiencing an issue with directive attributes when parsing markdown with remark-directive. It seems like the attributes are not being properly initialized or collected during parsing, causing the directive to lose its attribute information.

### Reproduction

```js
const unified = require('unified')
const markdown = require('remark-parse')
const directive = require('remark-directive')

const processor = unified()
  .use(markdown)
  .use(directive)

const input = `
:::note{#my-id .my-class key="value"}
Content here
:::
`

const tree = processor.parse(input)
const result = processor.runSync(tree)

// Attributes are not being captured correctly
console.log(result.children[0].attributes)
// Expected: { id: 'my-id', class: 'my-class', key: 'value' }
// Actual: undefined or null
```

### Expected behavior

The directive should properly capture and store all attributes (ID, classes, and key-value pairs) that are specified in the directive syntax. The attributes should be accessible on the resulting AST node.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This seems to have broken recently. The attributes object is not being populated even though the directive syntax is correctly formatted.

---
Repository: /testbed
