# Bug Report

### Describe the bug

I'm encountering an issue with how Rollup handles unresolved imports. When I have a relative import that cannot be resolved, Rollup is treating it as an external dependency and issuing a warning instead of throwing an error. This is causing my build to succeed when it should actually fail.

### Reproduction

```js
// main.js
import something from './non-existent-module.js';

console.log(something);
```

When bundling this with Rollup, I expect it to fail with an error about the unresolved import, but instead it:
1. Treats `./non-existent-module.js` as external
2. Logs a warning about treating it as external
3. Continues with the build

This seems backwards - relative imports that can't be resolved should error, while absolute/bare imports (like `import x from 'lodash'`) should be treated as external with a warning.

### Expected behavior

Rollup should throw an error when a relative import path cannot be resolved, as these typically indicate a mistake in the code (typo, missing file, etc.). Only non-relative imports should be treated as external dependencies.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
