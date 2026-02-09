# Bug Report

### Describe the bug

I'm encountering an issue with footnote handling in MDX. After a recent change, footnote definitions are not being processed correctly. On the first call, the behavior seems different from subsequent calls, which is causing inconsistent rendering of footnotes in my MDX documents.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`

const result = await compile(mdxContent)
// Footnotes are not being ignored consistently
// First footnote behaves differently than subsequent ones
```

### Expected behavior

Footnote definitions should be handled consistently regardless of how many times they appear or in what order they're processed. The ignore handler should return the same type of value every time it's called.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
