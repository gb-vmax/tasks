# Bug Report

### Describe the bug

I'm experiencing a stack overflow error when parsing MDX content. The application crashes with a "Maximum call stack size exceeded" error during the MDX compilation process.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<CustomComponent>
  Some content here
</CustomComponent>
`

// This causes a stack overflow
await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without throwing a stack overflow error. The parser should handle JSX tags within the MDX content normally.

### Additional context

This seems to happen specifically when processing JSX tags in the MDX content. The error occurs during the parsing phase and makes it impossible to compile any MDX files that contain JSX components.

Error message:
```
RangeError: Maximum call stack size exceeded
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
