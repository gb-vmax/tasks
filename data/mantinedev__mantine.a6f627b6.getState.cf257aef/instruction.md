# Bug Report

### Describe the bug
After updating to the latest version, `getState()` is returning a new object instance every time it's called instead of returning a reference to the actual state. This breaks equality checks and causes unnecessary re-renders in components that rely on reference equality.

### Reproduction
```js
const store = createStore({ count: 0 });

const state1 = store.getState();
const state2 = store.getState();

console.log(state1 === state2); // Expected: true, Actual: false
```

This also affects scenarios where you're comparing state objects:

```js
const store = createStore({ user: { name: 'John' } });

const prevState = store.getState();
// ... no state changes ...
const nextState = store.getState();

if (prevState !== nextState) {
  // This block incorrectly executes even though nothing changed
  console.log('State changed!');
}
```

### Expected behavior
`getState()` should return the same reference when the state hasn't changed. Multiple calls to `getState()` without any state updates in between should return identical references that pass strict equality checks (`===`).

### System Info
- @mantine/store version: latest
- Node: 18.x

---
Repository: /testbed
