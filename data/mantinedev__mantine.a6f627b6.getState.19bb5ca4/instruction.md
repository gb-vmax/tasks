# Bug Report

### Describe the bug

The `getState()` method is returning a new object copy instead of the actual state reference. This breaks scenarios where you need to maintain reference equality or work with the actual state object directly.

### Reproduction

```js
const store = createStore({ count: 0 });

const state1 = store.getState();
const state2 = store.getState();

// These should be the same reference but they're not
console.log(state1 === state2); // Expected: true, Actual: false

// Also, modifying the returned state doesn't affect the store
state1.count = 5;
console.log(store.getState().count); // Expected: 5, Actual: 0
```

### Expected behavior

`getState()` should return the same reference to the state object on subsequent calls. This is important for:
- Reference equality checks
- Performance optimizations that rely on reference comparison
- Direct state manipulation patterns (if supported)

### Additional context

This seems like a recent change. Previously `getState()` was returning the direct state reference which allowed for reference equality checks and other use cases that depend on object identity.

---
Repository: /testbed
