# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-directive plugin where directives are not being parsed correctly from markdown. When I try to use directives in my markdown content, they either don't get recognized or produce unexpected output.

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

The directive should be properly parsed and converted. Instead, the output doesn't match what's expected - it seems like the directive parsing and serialization are not working in sync.

### System Info

- remark-directive version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The directives worked fine before but now the parsing/stringification cycle produces incorrect results.

---
Repository: /testbed
