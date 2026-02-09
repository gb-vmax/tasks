# Bug Report

### Describe the bug

Getting an error when trying to use MDX with a custom compiler function. The error message says "Cannot `[operation]` without `compiler`" but I'm definitely passing a compiler function.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const result = await compile('# Hello', {
  compiler: (tree) => {
    // custom compiler logic
    return transformedTree
  }
})
```

This throws an error even though `compiler` is clearly a function. It seems like the type checking for the compiler option is incorrect.

### Expected behavior

Should accept a function as the `compiler` option and use it to compile the MDX content without throwing an error.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
