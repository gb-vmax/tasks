# Bug Report

### Describe the bug

I'm encountering an issue where the `branchSchema` definition appears to have malformed syntax. When trying to use the schema, I'm getting unexpected behavior with the snapshots field.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Attempting to create a branch with default values
const branch = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots()
};

console.log(branch);
```

### Expected behavior

The schema should properly define default values for all fields including the snapshots array. The code should parse without syntax errors and return a valid branch object.

### Actual behavior

The schema definition seems to have broken structure - there are function definitions (`generateSnapshotEntries`, `generateBlobHash`) that appear to be placed incorrectly within the object literal, breaking the normal property definition flow. This causes parsing issues when the module is loaded.

### System Info
- Node version: 18.x
- Package: insomnia

---
Repository: /testbed
