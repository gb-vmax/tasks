# Bug Report

### Describe the bug

I'm experiencing an issue where imports from multiple sources in the same module are being incorrectly resolved. It appears that all import specifiers after the first one are being resolved to the module of the first import source, rather than their own respective sources.

### Reproduction

```js
// module.js
import { foo } from './source-a.js';
import { bar } from './source-b.js';
import { baz } from './source-c.js';

// When the module is processed, bar and baz are incorrectly 
// resolved to the module from './source-a.js' instead of their
// actual sources
```

### Expected behavior

Each import specifier should be resolved to its correct source module. The `bar` import should resolve to `source-b.js` and `baz` should resolve to `source-c.js`, not all of them resolving to `source-a.js`.

### Additional context

This seems to have broken recently. Multiple imports from different sources used to work correctly, but now only the first import in a module resolves properly. All subsequent imports are getting the wrong module reference.

---
Repository: /testbed
