# Bug Report

### Describe the bug

Getting an error when processing MDX files with lists. The parser seems to be accessing array elements beyond the valid range, causing a runtime error when trying to read properties of undefined.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

- Item 1
- Item 2
- Item 3
`

const result = await compile(mdxContent)
// TypeError: Cannot read properties of undefined (reading 'type')
```

### Expected behavior

The MDX content should compile successfully without throwing errors. Lists should be parsed correctly.

### Additional context

This seems to happen specifically with list content (both ordered and unordered lists). Regular markdown without lists compiles fine. The error occurs during the compilation phase when the parser is processing the events array.

---
Repository: /testbed
