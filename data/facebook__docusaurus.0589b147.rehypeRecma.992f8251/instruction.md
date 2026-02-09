# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the `rehypeRecma` plugin is not working correctly. When processing MDX files, I'm getting errors or unexpected behavior during the compilation process.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

const result = await compile(mdxContent, {
  // ... options
})
```

When running the above code, the compilation fails or produces incorrect output. It seems like the options are not being passed through correctly to the `toEstree` function in the `rehypeRecma` plugin.

### Expected behavior

The MDX content should compile successfully and the options should be properly propagated through the compilation pipeline. The `rehypeRecma` plugin should correctly transform the rehype tree to an estree.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
