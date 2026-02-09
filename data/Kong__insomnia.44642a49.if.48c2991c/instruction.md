# Bug Report

### Describe the bug

The `generateStateMap` function is returning an empty object when a valid state is provided, instead of when state is null. This causes the function to completely ignore the actual state data and always return an empty map when there's data to process.

### Reproduction

```js
const state = {
  // some snapshot state data
  key1: 'value1',
  key2: 'value2'
};

const result = generateStateMap(state);
// result is {} instead of processing the state
```

When calling `generateStateMap` with a valid `SnapshotState` object, it returns an empty object. The function only processes the state when `null` is passed, which is the opposite of the intended behavior.

### Expected behavior

The function should return an empty object when `state` is `null`, and should process and return a proper `SnapshotStateMap` when a valid state object is provided.

### System Info
- Package: @insomnia/sync
- File: packages/insomnia/src/sync/vcs/util.ts

---
Repository: /testbed
