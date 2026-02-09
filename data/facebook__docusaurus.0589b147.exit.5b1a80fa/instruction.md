# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the parser seems to hang or fail to properly exit when processing certain directive syntax. The application becomes unresponsive when trying to parse markdown content with directives.

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
This is a container directive
:::
`

// Parser hangs or doesn't complete properly
const result = processor.processSync(markdown)
```

### Expected behavior

The parser should successfully process directives and complete the parsing without hanging. The AST should be generated correctly with the directive nodes properly closed.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
