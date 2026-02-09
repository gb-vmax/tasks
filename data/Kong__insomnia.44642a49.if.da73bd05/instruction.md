# Bug Report

### Describe the bug

After a recent update, the `generateStateMap` function appears to have duplicate code that's causing issues. When generating a state map from snapshot state entries, the function seems to process entries twice - once with validation and duplicate tracking logic, and then again with the old implementation. This results in the map being overwritten and losing the metadata about duplicates.

### Reproduction

```js
const state = [
  { key: 'item1', blob: 'data1', name: 'Item 1' },
  { key: 'item2', blob: 'data2', name: 'Item 2' },
  { key: 'item1', blob: 'data3', name: 'Item 1 Duplicate' }
];

const stateMap = generateStateMap(state);

// Expected: stateMap should have metadata about the duplicate 'item1' key
// Actual: metadata is lost because the function runs twice
const metadata = getStateMapMetadata(stateMap);
console.log(metadata); // Should show duplicate info but doesn't work correctly
```

### Expected behavior

The function should:
1. Validate each state entry properly
2. Track duplicate keys
3. Attach metadata about duplicates to the returned map
4. Not process the entries multiple times

Currently it looks like there's leftover code from the old implementation that runs after the new logic, causing the map to be rebuilt without the validation and metadata tracking.

### System Info
- Package: @insomnia/sync
- File: packages/insomnia/src/sync/vcs/util.ts

---
Repository: /testbed
