# Bug Report

### Describe the bug

The `all()` function in `workspace-meta.ts` is returning unexpected results. When trying to retrieve all workspace metadata, the function returns an empty result or doesn't filter by the correct type.

### Reproduction

```js
import * as workspaceMeta from './models/workspace-meta';

// Try to get all workspace metadata
const allMeta = await workspaceMeta.all();

// Expected: Array of WorkspaceMeta objects
// Actual: Returns all database records regardless of type
```

### Expected behavior

The `all()` function should return only `WorkspaceMeta` records, filtered by the correct type. Currently it seems to be returning all records from the database without any type filtering.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
