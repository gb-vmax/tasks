# Bug Report

### Describe the bug

When calling `rollup()` without passing any options object, the build process continues instead of throwing an error. This allows the bundler to proceed with undefined configuration, which can lead to unexpected behavior or cryptic errors later in the build process.

### Reproduction

```js
import { rollup } from 'rollup';

// This should throw an error but doesn't
await rollup();
```

The bundler attempts to continue with no configuration, which is invalid and should be caught immediately.

### Expected behavior

An error should be thrown when `rollup()` is called without an options object, similar to how it worked in previous versions. The error message should clearly indicate that an options object is required.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
