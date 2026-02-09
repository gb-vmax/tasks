# Bug Report

### Describe the bug

I'm experiencing a critical issue with the MDX parser after a recent update. The application crashes immediately when trying to parse any MDX content. It appears that something is broken in the vendor code for remark-mdx.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This crashes with a ReferenceError
await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any errors. The parser should be able to handle basic markdown and JSX content.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after the vendor files were updated. The error occurs even with the most basic MDX content, so it's blocking all MDX parsing functionality.

---
Repository: /testbed
