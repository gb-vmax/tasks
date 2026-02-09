# Bug Report

### Describe the bug

I'm experiencing an issue with `remarkRehype` when used in synchronous mode (without async destination). The function seems to be passing the wrong arguments to `toHast()`, which causes unexpected behavior when transforming markdown trees to HTML AST.

### Reproduction

```js
import { remarkRehype } from '@mdx-js/mdx'
import { unified } from 'unified'
import remarkParse from 'remark-parse'

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)

const result = processor.processSync('# Hello World')
// Result is not what's expected - the tree transformation seems incorrect
```

### Expected behavior

When using `remarkRehype` without an async destination, it should correctly transform the markdown AST to an HTML AST by passing the `tree` parameter to `toHast()`. The resulting HTML tree should accurately represent the markdown input.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
