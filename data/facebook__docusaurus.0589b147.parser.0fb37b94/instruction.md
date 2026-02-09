# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where plugin-provided extensions are being overridden by user settings. It seems like the order of precedence for configuration options has changed, causing micromark extensions and mdast extensions to not be applied correctly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import remarkGfm from 'remark-gfm'

const mdxSource = `
# Test

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |
`

// Compile with GFM plugin
const result = await compile(mdxSource, {
  remarkPlugins: [remarkGfm]
})
```

When compiling MDX with plugins that register micromark or mdast extensions (like `remark-gfm`), the extensions don't seem to be processed correctly. The table syntax should be parsed as a table, but it's being treated as plain text instead.

### Expected behavior

Plugin-registered extensions should take precedence and be properly applied during parsing. Tables and other GFM syntax should be parsed correctly when using the appropriate remark plugins.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
