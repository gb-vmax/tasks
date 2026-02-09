# Bug Report

### Describe the bug
Source maps are not being generated correctly when using the MDX compiler. The source map is always `undefined` even when `SourceMapGenerator` is provided in the options.

### Reproduction
```js
import { compile } from '@mdx-js/mdx'
import { SourceMapGenerator } from 'source-map'

const result = await compile('# Hello', {
  SourceMapGenerator,
  filePath: 'example.mdx'
})

console.log(result.map) // Expected: source map object, Actual: undefined
```

### Expected behavior
When `SourceMapGenerator` is passed in the options, the compiled result should include a valid source map in the `map` property. The source map should contain mappings for the transformed code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
