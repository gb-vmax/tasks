# Bug Report

### Describe the bug

I'm experiencing an issue with module resolution when importing external modules. It seems like external modules that don't start with '.' or '/' are being resolved incorrectly when they should be skipped.

### Reproduction

```js
// In a file at /project/src/index.js
import something from 'external-package';
```

When trying to resolve this import, the resolver is attempting to process it as a local file instead of recognizing it as an external module and skipping resolution. This causes the build to fail or produce unexpected results.

### Expected behavior

External module imports (those that don't start with '.' or '/') should be skipped during the resolution phase when there's an importer present. The resolver should only process relative and absolute paths.

### Steps to reproduce
1. Create a project with an entry file
2. Import an external package (e.g., `import lodash from 'lodash'`)
3. The import is incorrectly resolved instead of being treated as external

This appears to be related to the logic that determines whether a module should be skipped during resolution. The condition for skipping external modules doesn't seem to be working as intended.

---
Repository: /testbed
