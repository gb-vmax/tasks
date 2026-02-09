# Bug Report

### Describe the bug

I'm experiencing issues with remark-directive processing in my markdown pipeline. After a recent update, the directive parsing seems to be completely broken. When I try to process markdown content with directives, they're either not being recognized at all or causing the parser to fail silently.

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

const result = await processor.process(markdown)
console.log(result.toString())
```

### Expected behavior

The directives should be properly parsed and available in the AST. The markdown should be processed correctly with directive nodes being created and handled appropriately.

### Actual behavior

Directives are not being parsed correctly. The extensions don't seem to be registered properly in the processing pipeline, causing the directive syntax to either be ignored or processed as regular text.

### System Info

- remark-directive: 3.0.0
- unified: latest
- Node: 18.x

This was working fine before, so I suspect something changed in how the extensions are being registered. Any help would be appreciated!

---
Repository: /testbed
