# Bug Report

### Describe the bug

I'm experiencing a crash when using container directives in remark. The parser throws an error when it tries to process container directive syntax.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note
This is a container directive
:::
`

// This throws an error
processor.processSync(markdown)
```

### Expected behavior

The container directive should be parsed correctly without throwing an error. The processor should handle `:::` syntax properly and create the appropriate AST nodes.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
