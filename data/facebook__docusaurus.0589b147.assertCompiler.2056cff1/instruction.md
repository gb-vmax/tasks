# Bug Report

### Describe the bug

I'm getting an unexpected error when trying to compile MDX content. The error message says "Cannot `compile` with `compiler`" which doesn't make sense - I'm providing the compiler function as required, but it's throwing an error saying I can't use it WITH a compiler.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

const mdxSource = '# Hello World'

// This throws an error even though compiler is provided correctly
const result = await compile(mdxSource, {
  // ... other options
})
```

The error I'm seeing is:
```
TypeError: Cannot `compile` with `compiler`
```

### Expected behavior

The compilation should work when a valid compiler function is provided. The error message also seems backwards - it should complain when a compiler is NOT provided, not when it IS provided.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
