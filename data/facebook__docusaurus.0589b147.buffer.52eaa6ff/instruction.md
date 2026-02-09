# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the buffer function seems to be broken. When processing MDX content with JSX tags, I'm getting errors related to the buffer not being properly initialized or called.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<CustomComponent>
  Some content here
</CustomComponent>
`

const result = await compile(mdxContent)
```

When running this code, the MDX compiler fails to properly handle the JSX tags. It seems like the internal buffering mechanism isn't working as expected.

### Expected behavior

The MDX content should compile successfully without any buffering errors. The JSX tags should be parsed and the buffer should be called/managed correctly during the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
