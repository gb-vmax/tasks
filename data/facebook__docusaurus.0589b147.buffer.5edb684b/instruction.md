# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the buffer function is being called with an incorrect context. This causes the parser to fail when processing certain MDX content.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<CustomComponent>
  Some content here
</CustomComponent>
`

// This fails during parsing
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without errors. The buffer function should maintain the correct context when called internally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
