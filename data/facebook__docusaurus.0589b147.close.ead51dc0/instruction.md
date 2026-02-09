# Bug Report

### Describe the bug

I'm encountering an issue with MDX compilation where certain closing tokens are not being processed correctly. It seems like the exit handler is being skipped in some cases, which causes the compiler to not properly close elements.

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

When compiling MDX with custom components that have closing tags, the closing logic doesn't execute properly. The stack doesn't get popped correctly and nested elements remain unclosed.

### Expected behavior

All opening tags should be properly matched with their closing tags, and the exit handlers should be called to pop elements from the stack correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
