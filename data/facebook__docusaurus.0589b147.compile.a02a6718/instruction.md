# Bug Report

### Describe the bug

After a recent update, MDX compilation is completely broken. When trying to compile MDX files, I'm getting errors about `resolveFileAndOptions(...).process is not a function`. The compilation process fails immediately and nothing renders.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test MDX file.
`

// This throws an error
const result = await compile(mdxSource, {
  /* options */
})
```

### Expected behavior

The MDX source should compile successfully and return the compiled result. This was working fine before the latest changes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
