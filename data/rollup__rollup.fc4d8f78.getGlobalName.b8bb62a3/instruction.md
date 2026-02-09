# Bug Report

### Describe the bug

When generating bundles without exports, the global name warning is being triggered incorrectly. I'm getting a warning about missing global names for chunks that don't have any exports, which doesn't make sense since they shouldn't need a global name in the first place.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyLib',
    globals: {
      'some-dependency': 'SomeDep'
    }
  }
}

// src/index.js - a module with no exports
import 'some-dependency'
// just side effects, no exports
```

### Expected behavior

Chunks without exports shouldn't trigger warnings about missing global names. The warning should only appear for chunks that actually have exports and need to be accessible globally.

Currently getting warnings like:
```
(!) Missing global variable name
Use output.globals to specify browser global variable names corresponding to external modules
```

But this doesn't make sense for modules that don't export anything.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
