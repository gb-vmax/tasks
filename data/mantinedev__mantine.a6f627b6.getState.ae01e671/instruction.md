# Bug Report

### Describe the bug

I'm having an issue with the store's `getState()` method. When I call it and then modify the returned object, it seems to affect the internal state of the store directly. This shouldn't happen - the state should be isolated from external modifications.

### Reproduction

```js
const store = createStore({ count: 0, user: { name: 'John' } });

// Get the state
const state = store.getState();

// Modify the returned object
state.count = 999;
state.user.name = 'Modified';

// The internal state is now corrupted!
const newState = store.getState();
console.log(newState.count); // Expected: 0, Actual: 999
console.log(newState.user.name); // Expected: 'John', Actual: 'Modified'
```

### Expected behavior

`getState()` should return a copy or snapshot of the state that is independent from the store's internal state. Modifying the returned object should not affect the store itself.

### System Info
- @mantine/store version: latest
- Node version: 18.x

This is causing issues in my application where components accidentally mutate the state object returned by `getState()`, leading to unpredictable behavior.

---
Repository: /testbed
