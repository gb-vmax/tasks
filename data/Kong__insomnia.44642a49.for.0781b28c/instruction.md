# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error in the `util.ts` file. The `combinedMapKeys` function appears to have malformed code - there's a duplicate function declaration inside the original function body, and the closing braces don't match up properly.

### Reproduction

The issue occurs in `packages/insomnia/src/sync/vcs/util.ts` in the `combinedMapKeys` function. When trying to use any functionality that depends on this utility function, the application fails to compile/run.

```js
// Attempting to call combinedMapKeys results in compilation errors
const keys = combinedMapKeys(map1, map2);
```

### Expected behavior

The `combinedMapKeys` function should compile and execute without syntax errors. It should accept multiple maps and return their combined keys.

### System Info
- Insomnia version: latest
- The error appears to be introduced in the sync/vcs utility module

The code structure looks broken with nested function declarations and mismatched braces. This is blocking any sync-related operations from working.

---
Repository: /testbed
