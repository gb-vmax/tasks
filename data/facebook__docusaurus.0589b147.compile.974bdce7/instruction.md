# Bug Report

### Describe the bug

The `compile()` function is not returning the expected result anymore. Instead of returning a Promise that resolves to the compiled output, it appears to be returning the processor instance itself.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = '# Hello World'

// This used to work but now returns something unexpected
const result = await compile(mdxSource)

// Expected: result should contain the compiled MDX output
// Actual: result is a processor instance instead of the compilation result
console.log(result)
```

### Expected behavior

The `compile()` function should return a Promise that resolves to a VFile containing the compiled MDX output, not the processor instance.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
