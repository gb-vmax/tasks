# Bug Report

### Describe the bug

After a recent update, MDX parsing is completely broken. When trying to parse MDX content, I'm getting errors or the parser fails to initialize properly. It seems like something internal changed that broke the tokenizer creation.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This fails to parse correctly
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should parse successfully and return the compiled output without errors. This was working fine before the latest changes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
