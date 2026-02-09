# Bug Report

### Describe the bug

I'm encountering an issue with branch schema initialization where the `modified` field is not being set correctly. It appears that the `modified` property is now returning a function instead of a Date object, which causes problems when trying to access or compare modification timestamps.

### Reproduction

```js
import { branchSchema } from './type-schemas';

const branch = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots()
};

// This now fails because modified is a function, not a Date
console.log(branch.modified.getTime()); // TypeError: branch.modified.getTime is not a function
```

### Expected behavior

The `modified` field should return a `Date` object directly, just like the `created` field does. Both should be consistent in their return types.

### System Info
- Insomnia version: latest
- Platform: N/A

---
Repository: /testbed
