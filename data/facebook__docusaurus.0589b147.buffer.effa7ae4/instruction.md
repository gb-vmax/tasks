# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the fragment handling seems to be broken. When processing MDX content with nested components or fragments, the compiler appears to be placing items in the wrong order or losing track of the children structure.

### Reproduction

```jsx
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<div>
  <p>Nested content</p>
</div>
`

const result = await compile(mdxContent)
// The compiled output has incorrect structure
```

### Expected behavior

The compiler should correctly maintain the hierarchy of fragments and their children when processing MDX content. Nested elements should be properly organized in the AST.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
