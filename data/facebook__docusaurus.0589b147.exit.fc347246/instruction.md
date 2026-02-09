# Bug Report

### Describe the bug

I'm experiencing an issue where directives are not being processed correctly in markdown content. When parsing markdown with directives, the parser seems to hang or fail silently without throwing any errors.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note
This is a note directive
:::
`

// Parser doesn't complete or produces unexpected output
const result = processor.processSync(markdown)
```

### Expected behavior

The directive should be parsed correctly and the processor should complete successfully, generating the appropriate AST nodes for the directive.

### System Info

- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
