# Bug Report

### Describe the bug

I'm experiencing an issue with branch schema generation where the `modified` timestamp is no longer consistent. Previously, all branches would have the same initial `modified` date (`new Date(0)`), but now each branch gets a different timestamp that increments automatically.

This is causing problems in our application because we rely on deterministic timestamps for branch creation, especially during testing and when comparing branch states.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Create multiple branches
const branch1 = { 
  ...someData,
  modified: branchSchema.modified()
};

const branch2 = { 
  ...someData,
  modified: branchSchema.modified()
};

console.log(branch1.modified); // Expected: Thu Jan 01 1970 00:00:00 GMT+0000
console.log(branch2.modified); // Expected: Thu Jan 01 1970 00:00:00 GMT+0000

// But now they have different timestamps!
// branch1.modified: Thu Jan 01 1970 00:00:00 GMT+0000
// branch2.modified: Thu Jan 01 1970 01:00:00 GMT+0000
```

### Expected behavior

The `modified` field should return a consistent timestamp (epoch 0) for all branches, just like the `created` field does. This was the previous behavior and our code depends on it for deterministic schema generation.

### Additional context

This seems to have introduced some kind of counter that increments the timestamp on each call. While I can see there's an environment variable `BUILDER_DETERMINISTIC` that might help, the default behavior should remain consistent with what it was before.

---
Repository: /testbed
