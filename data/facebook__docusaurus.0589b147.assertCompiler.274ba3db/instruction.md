# Bug Report

### Describe the bug

When passing a valid compiler function to MDX, I'm getting an error saying "Cannot `compiler` without `compiler`". This doesn't make sense since I'm definitely providing a compiler function.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = '# Hello World'

const result = await compile(mdxSource, {
  compiler: (tree) => {
    // custom compiler logic
    return tree
  }
})
```

This throws: `TypeError: Cannot 'compiler' without 'compiler'`

### Expected behavior

The compilation should succeed when a valid compiler function is provided. The error message also seems wrong - it says "Cannot `compiler` without `compiler`" which is confusing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
