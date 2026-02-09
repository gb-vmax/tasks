# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX compiler where the output is completely broken. Instead of getting the compiled JavaScript code, I'm only receiving the source map object. This makes the entire compilation process unusable.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test MDX file.
`

const result = await compile(mdxSource, {
  SourceMapGenerator: MySourceMapGenerator
})

console.log(result) // Expected: compiled JS code, Actual: source map object
```

### Expected behavior

The compiler should return the compiled JavaScript code as a string. The source map should be attached as a separate property (`file.map`), not returned as the main output.

Currently getting a source map object instead of the actual compiled code, which breaks any downstream processing that expects JavaScript source code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
