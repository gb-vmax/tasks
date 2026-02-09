# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM blocks where the `data.estree` property is being set incorrectly. When parsing MDX files with ESM imports/exports, the estree data is being attached even when it shouldn't be, or it's being attached to the wrong node in the AST.

### Reproduction

```js
// Example MDX content with ESM block
import { something } from 'somewhere'

export const foo = 'bar'

# My Content
```

When parsing this, the estree data structure seems to be getting assigned to the wrong node or under incorrect conditions. The parsed AST doesn't match what's expected - either the estree property appears when it shouldn't, or it's missing when it should be present.

### Expected behavior

The `data.estree` property should only be set on the mdxjsEsm node when the estree is actually present/valid, and it should be attached to the correct node in the stack.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
