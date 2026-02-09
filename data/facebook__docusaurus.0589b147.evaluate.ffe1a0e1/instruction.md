# Bug Report

### Describe the bug

The `evaluate` function from `@mdx-js/mdx` is returning `undefined` instead of actually evaluating MDX content. This breaks any code that relies on the evaluate function to process and return MDX compilation results.

### Reproduction

```js
import { evaluate } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test.
`

const result = await evaluate(mdxContent)
console.log(result) // prints: undefined
```

### Expected behavior

The `evaluate` function should return the compiled MDX result object containing the default export and any other exports from the MDX file. Instead, it's returning `undefined` which makes it impossible to use the evaluated content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
