# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM blocks where the `estree` data is being assigned incorrectly. When processing MDX files with ESM imports/exports, the AST node's data property is getting set even when there's no estree available, which seems backwards.

### Reproduction

```js
// MDX file with ESM block
import { something } from 'somewhere'

export const config = { value: 'test' }

# My Content
```

When this gets parsed, the resulting AST node for the ESM block has unexpected data attached to it. The `estree` property should only be set when the estree actually exists, but currently it seems to be doing the opposite.

### Expected behavior

The `data.estree` property should only be added to the MDX ESM node when an estree is actually present in the token. If there's no estree, the data property shouldn't be set at all.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
