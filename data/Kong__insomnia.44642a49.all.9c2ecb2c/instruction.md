# Bug Report

### Describe the bug

I'm experiencing an issue with proto directory operations where duplicate function exports are causing the application to fail. After a recent update, the code seems to have redefined exports for `create`, `remove`, and `batchRemoveIds` functions, which breaks the module.

### Reproduction

```js
import { create, remove, batchRemoveIds } from './proto-directory';

// Try to create a new proto directory
const newDir = create({ name: 'test' });

// Application throws an error about duplicate exports
```

### Expected behavior

The functions should be exported once and work correctly without any duplicate export errors. Creating, removing, and batch removing proto directories should work as before.

### Additional context

It looks like the module is trying to wrap the original functions but then re-exports them with the same names, causing conflicts. The `create`, `remove`, and `batchRemoveIds` functions appear to be defined twice in the same file.

---
Repository: /testbed
