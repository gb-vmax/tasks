# Bug Report

### Describe the bug

After a recent update, MDX parsing is completely broken. When trying to parse MDX content, I'm getting errors or unexpected behavior. It seems like something changed in the tokenizer creation logic.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This now fails or produces incorrect output
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should parse correctly and compile without errors, just like it did in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
