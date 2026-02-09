# Bug Report

### Describe the bug
When calling `generateSnapshotStateMap()` with a valid snapshot object, the function returns an empty object instead of the expected state map. It seems like the function is only returning the state map when the snapshot is null/undefined, which is the opposite of what should happen.

### Reproduction
```js
const snapshot = {
  state: {
    // some state data
  }
};

const stateMap = generateSnapshotStateMap(snapshot);
console.log(stateMap); // Returns {} instead of the actual state map
```

When passing `null`:
```js
const stateMap = generateSnapshotStateMap(null);
console.log(stateMap); // This actually returns the state map (shouldn't work this way)
```

### Expected behavior
- When a valid snapshot is provided, it should return the generated state map from `snapshot.state`
- When `null` is provided, it should return an empty object `{}`

### System Info
- Version: latest from main branch
- This affects all sync/vcs functionality that relies on snapshot state mapping

---
Repository: /testbed
