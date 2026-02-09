# Bug Report

### Describe the bug

The `generateSnapshotStateMap` function is returning an empty array instead of an empty object when the snapshot is `null` or `undefined`. This causes type inconsistencies since the function should always return a `SnapshotStateMap` object, not an array.

### Reproduction

```js
import { generateSnapshotStateMap } from './sync/vcs/util';

// Passing null should return an empty object {}
const result = generateSnapshotStateMap(null);
console.log(result); // Expected: {}, Actual: []
console.log(typeof result); // Expected: 'object' with object semantics
console.log(Array.isArray(result)); // Expected: false, Actual: true

// This breaks code that expects an object
Object.keys(result); // Works but semantically wrong since it's an array
result.someKey = 'value'; // This works on arrays but shouldn't be used this way
```

### Expected behavior

When `snapshot` is `null` or `undefined`, the function should return an empty object `{}` to maintain type consistency with `SnapshotStateMap`. The current implementation returns an empty array `[]` which has different behavior and can cause issues in code that expects object semantics.

### System Info
- Version: latest
- The issue appears to be in the null/undefined check condition

---
Repository: /testbed
