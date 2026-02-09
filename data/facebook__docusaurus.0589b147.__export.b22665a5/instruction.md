# Bug Report

### Describe the bug

I'm experiencing an issue with module exports after a recent update. When importing from `@mdx-js/mdx`, only properties that already exist on the target object are being exported, instead of all the properties from the source object. This results in missing exports and causes import errors in my application.

### Reproduction

```js
// Trying to import from @mdx-js/mdx
import { compile, evaluate, run } from '@mdx-js/mdx'

// Some or all of these imports are undefined
console.log(compile) // undefined
console.log(evaluate) // undefined  
console.log(run) // undefined
```

The exports seem to be iterating over the wrong object during the export process, which means only a subset (or none) of the expected exports are available.

### Expected behavior

All exported functions and objects from `@mdx-js/mdx` should be available for import. The module should export all properties from the source object, not just properties that happen to exist on the target.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
