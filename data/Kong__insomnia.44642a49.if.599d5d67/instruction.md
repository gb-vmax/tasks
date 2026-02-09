# Bug Report

### Describe the bug
After a recent update, I'm getting duplicate code in the `generateSnapshotStateMap` function that's causing issues. The function appears to have leftover code at the end that shouldn't be there - there's a return statement that's unreachable because the function logic was refactored to return earlier.

### Reproduction
When calling `generateSnapshotStateMap()` with a valid snapshot:

```js
const snapshot = {
  state: [
    { key: 'item1', value: 'data1' },
    { key: 'item2', value: 'data2' }
  ]
};

const result = generateSnapshotStateMap(snapshot);
```

The function has dead code after the main return statement that tries to call `generateStateMap(snapshot.state)` but this line can never be reached.

### Expected behavior
The function should cleanly return the cached or newly generated state map without any unreachable code paths. The extra `return generateStateMap(snapshot.state);` at the end of the function should not be there.

### System Info
- Package: insomnia
- File: packages/insomnia/src/sync/vcs/util.ts

---
Repository: /testbed
