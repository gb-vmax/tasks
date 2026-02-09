# Bug Report

### Describe the bug

The application freezes and becomes unresponsive when processing markdown documents with directives. After some investigation, it appears that the parser enters an infinite loop during the exit phase of directive parsing.

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
This is a directive
:::
`

// This hangs indefinitely
processor.process(markdown)
```

### Expected behavior

The markdown should be parsed successfully without hanging. The processor should complete and return the AST for the directive.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
