# Bug Report

### Describe the bug

After a recent update, the MDX module seems to have a syntax error or malformed export that's preventing it from loading correctly. The module appears to be broken and I'm getting errors when trying to use it.

### Reproduction

```js
import { runSync } from '@mdx-js/mdx'

// Trying to use runSync results in errors
const result = runSync(tree, file)
```

The module doesn't seem to export `runSync` properly anymore. Looking at the vendor file, it seems like there's a malformed export statement where `runSync` should be defined.

### Expected behavior

The `runSync` function should be exported correctly and be usable like the other exported functions (`run`, `compile`, `evaluate`, etc.).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
