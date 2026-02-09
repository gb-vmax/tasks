# Bug Report

### Describe the bug

When processing MDX content, the `fromMarkdownExtensions` array is not being populated correctly. Instead of adding extensions to `fromMarkdownExtensions`, they're being added to `toMarkdownExtensions`, which causes parsing issues with MDX syntax elements.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<MyComponent />

export const meta = { title: 'Test' }
`

// Try to compile MDX content
const result = await compile(mdxContent)
// Parsing fails or produces incorrect output
```

### Expected behavior

MDX content should be parsed correctly with all MDX-specific syntax (JSX components, exports, imports) being recognized and processed properly. The `fromMarkdownExtensions` should contain the necessary extensions for parsing MDX from markdown.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
