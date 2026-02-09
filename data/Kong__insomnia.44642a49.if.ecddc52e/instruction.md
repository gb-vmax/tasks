# Bug Report

### Describe the bug

When calling `generateStateMap` with a non-null state object, the function returns `undefined` instead of generating the expected state map. This causes downstream code that expects a map object to fail.

### Reproduction

```js
const state = {
  // some snapshot state data
  key: 'value'
};

const result = generateStateMap(state);
// result is undefined instead of a map object
console.log(result); // undefined
```

### Expected behavior

The function should return a properly constructed `SnapshotStateMap` object when given a valid state. It should only return an empty object `{}` when the state is null or undefined.

Currently it seems like the logic is inverted - passing a valid state returns undefined, which breaks any code trying to use the returned map.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
