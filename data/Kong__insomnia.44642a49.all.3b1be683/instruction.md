# Bug Report

### Describe the bug

The `all()` function in workspace-meta is returning incorrect results. Instead of returning all workspace metadata entries, it appears to be returning only a single entry or behaving unexpectedly.

### Reproduction

```js
import * as workspaceMeta from './models/workspace-meta';

// Create multiple workspace metadata entries
await workspaceMeta.create({ parentId: 'workspace1' });
await workspaceMeta.create({ parentId: 'workspace2' });
await workspaceMeta.create({ parentId: 'workspace3' });

// Try to get all workspace metadata
const allMeta = await workspaceMeta.all();

// Expected: Array with 3 entries
// Actual: Single entry or unexpected result
console.log('Count:', allMeta.length); // Not returning all entries
```

### Expected behavior

The `all()` function should return an array containing all workspace metadata entries in the database, similar to how other model `all()` functions work throughout the codebase.

### System Info
- Version: Latest
- Platform: All

---
Repository: /testbed
