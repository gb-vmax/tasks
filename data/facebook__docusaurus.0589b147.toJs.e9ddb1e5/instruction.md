# Bug Report

### Describe the bug

I'm encountering an issue with source map generation in the MDX compiler. When `SourceMapGenerator` is provided in the options, the source map is not being created properly, and when it's not provided, the code attempts to use it anyway which causes errors.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import { SourceMapGenerator } from 'source-map'

// Case 1: With SourceMapGenerator provided
const result1 = await compile('# Hello', {
  SourceMapGenerator: SourceMapGenerator,
  filePath: 'test.mdx'
})

// Expected: result1.map should contain the source map
// Actual: result1.map is undefined

// Case 2: Without SourceMapGenerator
const result2 = await compile('# Hello', {
  filePath: 'test.mdx'
})

// Expected: result2.map should be undefined
// Actual: Throws an error trying to call toJSON() on undefined
```

### Expected behavior

- When `SourceMapGenerator` is provided, a source map should be generated and included in the result
- When `SourceMapGenerator` is not provided, the map should be undefined without throwing errors

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
