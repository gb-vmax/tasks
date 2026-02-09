# Bug Report

### MDX parsing broken after recent changes

I'm experiencing issues with MDX parsing that seems to have been introduced recently. The parser is not correctly handling MDX content and appears to be processing syntax extensions in the wrong order.

### Reproduction

When trying to parse MDX content that includes JSX components and ESM imports, the parser fails or produces incorrect output:

```js
const mdxContent = `
import { Component } from './component'

# Hello

<Component />
`

// Parser fails to correctly process this content
const result = compile(mdxContent)
```

### Expected behavior

The MDX parser should correctly handle:
1. ESM imports at the top of the file
2. JSX components mixed with markdown
3. MDX expressions

All of these should be parsed in the correct order and produce valid output.

### Additional context

This appears to affect the `mdxFromMarkdown()` function. The syntax extensions don't seem to be applied in the right sequence, which causes the parser to misinterpret the MDX content structure.

---
Repository: /testbed
