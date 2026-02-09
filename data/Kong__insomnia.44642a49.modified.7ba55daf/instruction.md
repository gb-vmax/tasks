# Bug Report

### Describe the bug

Branch modified dates are being generated inconsistently - sometimes they're set to random dates within the past 2 years instead of a consistent epoch value. This is causing issues when creating or syncing branches, as the modified timestamp can vary unpredictably between different instances or calls.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Create multiple branch objects
const branch1 = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots(),
};

const branch2 = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots(),
};

console.log(branch1.modified); // Random date within past 2 years
console.log(branch2.modified); // Different random date
console.log(branch1.created);  // Date(0) - epoch
```

### Expected behavior

The `modified` field should consistently return the same deterministic value (like epoch `new Date(0)`) just like the `created` field does. Branch objects created at the same time should have identical default timestamps for predictability and consistency.

### Additional context

This seems to have introduced non-deterministic behavior where branch modified dates are randomized. The logic also tries to ensure modified is after created, but this adds unnecessary complexity for default schema values. The previous behavior of simply returning `new Date(0)` was more predictable.

---
Repository: /testbed
