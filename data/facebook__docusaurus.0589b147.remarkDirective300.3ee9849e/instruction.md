# Bug Report

### Describe the bug

I'm experiencing issues with remark-directive where markdown directives aren't being parsed or rendered correctly. It seems like the directive syntax is not being recognized properly, and the output is malformed or missing directive content entirely.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'
import remarkStringify from 'remark-stringify'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)
  .use(remarkStringify)

const markdown = `
::note
This is a note directive
::
`

const result = processor.processSync(markdown)
console.log(result.toString())
```

### Expected behavior

The directive should be properly parsed and converted. The extensions should be correctly registered to handle both parsing from markdown and converting back to markdown.

### Actual behavior

Directives are not being processed correctly - either failing to parse or producing incorrect output when stringifying.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
