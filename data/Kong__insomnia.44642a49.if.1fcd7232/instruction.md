# Bug Report

### Describe the bug
When passing `null` as a snapshot to `generateSnapshotStateMap()`, the function returns `null` instead of an empty object. This causes issues when the returned value is used in contexts expecting an object/map.

### Reproduction
```js
import { generateSnapshotStateMap } from './sync/vcs/util';

// This now returns null instead of {}
const result = generateSnapshotStateMap(null);

// Trying to use the result as an object fails
console.log(Object.keys(result)); // TypeError: Cannot convert undefined or null to object
```

### Expected behavior
The function should return an empty object `{}` when the snapshot is `null` or falsy, allowing it to be safely used in operations that expect an object.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
