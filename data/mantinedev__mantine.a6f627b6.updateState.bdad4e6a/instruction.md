# Bug Report

### Describe the bug

When using `updateState` with a function that returns the new state, the state update is not working as expected. The function seems to be called incorrectly, causing the state to be set to unexpected values.

### Reproduction

```js
const store = createStore({ count: 0 });

// This should update the state based on the current state
store.updateState((currentState) => ({
  count: currentState.count + 1
}));

// The state is not updated correctly
console.log(store.getState()); // Expected: { count: 1 }, but getting unexpected result
```

### Expected behavior

When passing a function to `updateState`, it should:
1. Call the function with the current state
2. Use the returned value as the new state
3. The state should be updated correctly

### System Info
- @mantine/store version: latest
- Node version: 18.x

---
Repository: /testbed
