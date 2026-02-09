# Bug Report

### Describe the bug

The `all()` function in workspace-meta is returning incorrect data. When trying to retrieve all workspace metadata, it only returns a single item instead of an array of all workspace meta objects.

### Reproduction

```js
import * as workspaceMeta from './models/workspace-meta';

// Create multiple workspace metas
await workspaceMeta.create({ parentId: 'workspace1' });
await workspaceMeta.create({ parentId: 'workspace2' });
await workspaceMeta.create({ parentId: 'workspace3' });

// Try to get all workspace metas
const allMetas = await workspaceMeta.all();

console.log('Expected: array with 3+ items');
console.log('Actual:', allMetas); // Returns single object instead of array
```

### Expected behavior

The `all()` function should return an array containing all workspace metadata objects, not just a single item.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently - the function used to return all workspace metas correctly but now only returns one.

---
Repository: /testbed
