# Bug Report

### Describe the bug

I'm experiencing a stack overflow error when parsing MDX content with JSX tags. The application crashes with a "Maximum call stack size exceeded" error when processing certain MDX files.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<MyComponent>
  Some content here
</MyComponent>
`

// This causes a stack overflow
await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without throwing a stack overflow error. The JSX tags should be parsed and transformed correctly.

### Additional context

This seems to happen specifically when processing JSX tags in MDX content. The error occurs during the markdown-to-MDX transformation phase. It was working fine before, but now consistently crashes with any MDX file containing JSX elements.

---
Repository: /testbed
