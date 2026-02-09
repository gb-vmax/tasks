# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where custom micromark extensions are not being applied correctly. When I configure micromark extensions through the unified data system, they're being ignored during the markdown parsing phase.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import { gfmTable } from 'micromark-extension-gfm-table'

const processor = unified()
  .use(remarkParse)
  .data('micromarkExtensions', [gfmTable()])

const result = processor.processSync('| a | b |\n| - | - |')
// Extensions are not being applied - table is not parsed correctly
```

### Expected behavior

The micromark extensions registered via `.data('micromarkExtensions', ...)` should be passed through to the `fromMarkdown` function and applied during parsing. Tables and other syntax extensions should be recognized and parsed properly.

### Additional context

This seems to affect any custom micromark extensions configured through the data system. The extensions array appears to be getting replaced with an empty array instead of using the registered extensions.

---
Repository: /testbed
