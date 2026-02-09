# Bug Report

### Describe the bug

I'm getting a `TypeError` when trying to use the MDX compiler with a valid compiler function. The error message says "Cannot `[operation]` without `compiler`" even though I'm definitely passing a compiler function.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = '# Hello World'

// This throws an error even though we're passing a valid compiler
await compile(mdxContent, {
  compiler: myValidCompilerFunction
})
```

The error thrown is:
```
TypeError: Cannot `compile` without `compiler`
```

But I'm clearly providing a compiler function! This worked fine in previous versions.

### Expected behavior

The compilation should proceed normally when a valid compiler function is provided. The error should only be thrown when the compiler is missing or not a function.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
