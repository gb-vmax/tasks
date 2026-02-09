# Bug Report

### Describe the bug

When creating a new ProtoDirectory without a `parentId`, the creation process fails unexpectedly. The function appears to be passing incorrect arguments to `db.docCreate()`, causing the directory creation to not work as intended.

### Reproduction

```js
import { create } from './proto-directory';

// Try to create a ProtoDirectory with various properties
const result = create({
  name: 'my-proto-directory',
  protoFileIds: []
});

// The result is not what's expected - the patch object properties are not being used
```

### Expected behavior

The `create` function should properly pass the patch object to `db.docCreate()` so that all properties (name, protoFileIds, etc.) are included in the created ProtoDirectory. Currently it seems like only the parentId is being passed instead of the full patch object.

### Additional context

This appears to have broken after a recent change. Previously, the function would throw an error if `parentId` was missing, but now it sets it to `undefined` and then passes only that value to `docCreate` instead of the entire patch object.

---
Repository: /testbed
