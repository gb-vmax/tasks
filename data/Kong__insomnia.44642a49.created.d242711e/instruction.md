# Bug Report

### Describe the bug

After a recent update, the schema initialization for branches is broken. When creating branch objects, I'm getting a syntax error that prevents the application from starting properly.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Try to initialize a branch object
const branch = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots()
};
```

The code fails to parse/execute and throws an error about invalid syntax in the schema definition.

### Expected behavior

The branch schema should initialize correctly with default values. The `created` field should return a Date object (either `new Date(0)` or a random date depending on configuration).

### Additional context

Looking at the schema file, it seems like there's a function definition (`getRandomDateInRange`) that's been placed in the wrong location within the object literal. This is causing the entire schema object to be malformed.

The application was working fine before this change, so this appears to be a regression introduced in a recent commit.

---
Repository: /testbed
