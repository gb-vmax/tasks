# Bug Report

### Describe the bug

When using remark-mdx with custom acorn options, I'm getting an error about missing `parse` and `parseExpressionAt` methods even though I'm passing a valid acorn instance. The parser seems to be checking for these methods when acorn is NOT provided instead of when it IS provided.

### Reproduction

```js
import {remarkMdx} from 'remark-mdx'
import * as acorn from 'acorn'

// This throws an error unexpectedly
const processor = unified()
  .use(remarkMdx, {
    acorn: acorn
  })
```

The error message says:
```
Expected a proper `acorn` instance passed in as `options.acorn`
```

But I AM passing a proper acorn instance. The validation logic appears to be backwards - it's validating when acorn is falsy instead of when it's truthy.

### Expected behavior

When passing a valid acorn instance via `options.acorn`, the parser should accept it without throwing an error. The validation should only run when an acorn instance is actually provided.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
