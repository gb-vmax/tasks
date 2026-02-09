# Bug Report

### Describe the bug
There's a syntax error in the branch schema definition that's breaking the application. The `snapshots` property definition appears to have malformed code with a function declaration (`generateMockSnapshot`) inserted in the middle of the object literal, which is invalid JavaScript syntax.

### Reproduction
```js
// Attempting to use the branchSchema will fail
import { branchSchema } from './type-schemas';

// This will throw a syntax error when the module is loaded
const branch = createMockBranch();
```

### Expected behavior
The schema should be properly defined with valid JavaScript syntax. The object literal should not contain function declarations between its properties.

### System Info
- Node version: Latest
- Package: @insomnia/sync

The code is currently not parseable and will cause the entire module to fail to load. This looks like an incomplete refactoring or merge conflict that wasn't properly resolved.

---
Repository: /testbed
