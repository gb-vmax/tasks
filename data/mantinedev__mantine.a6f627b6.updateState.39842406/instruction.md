# Bug Report

### Describe the bug

The `updateState` method in the store is not working correctly when passing either a function or a direct value. When I try to update the state using a function that receives the current state, it seems to break completely.

### Reproduction

```js
const store = createStore({ count: 0 });

// This should update based on current state
store.updateState((currentState) => ({
  count: currentState.count + 1
}));

// Or even a direct value update
store.updateState({ count: 5 });
```

### Expected behavior

- When passing a function to `updateState`, it should receive the current state as an argument and use the returned value as the new state
- When passing a direct value, it should set that value as the new state
- The store state should be properly updated in both cases

### System Info
- @mantine/store version: latest
- Node: 18.x

---
Repository: /testbed
