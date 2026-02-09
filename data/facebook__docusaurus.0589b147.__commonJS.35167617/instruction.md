# Bug Report

### Describe the bug

After a recent update, MDX compilation is failing completely. When trying to compile any MDX file, I'm getting errors about modules not being properly initialized or exported. The compiled output seems broken and nothing renders.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a simple MDX document.
`

const result = await compile(mdxSource)
// Error: Module initialization fails
```

### Expected behavior

MDX files should compile successfully and the resulting JavaScript should execute without errors. The module should be properly initialized with all exports available.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
