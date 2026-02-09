# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in remark-directive where the parser seems to be handling the closing of container directives incorrectly. The content and container exit events appear to be firing in the wrong order, which is causing parsing issues with nested directives.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note
This is a container directive with content
:::
`

const ast = processor.parse(markdown)
// The AST structure shows incorrect nesting/exit order
```

### Expected behavior

The parser should properly exit the directive container content before exiting the container itself. The events should fire in the correct order to maintain proper AST structure for nested directives.

### Additional context

This seems to affect how directive containers are tokenized and could lead to malformed AST output when working with complex nested directive structures. The exit order matters for proper tree construction.

---
Repository: /testbed
