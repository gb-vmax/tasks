# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where modifying the state object returned by `getState()` doesn't update the actual store state. It seems like changes to the returned object are now isolated and don't affect the store's internal state.

### Reproduction

```js
const store = createStore({ count: 0 });

const state = store.getState();
state.count = 5;

// The store's internal state is still 0
console.log(store.getState().count); // Expected: 5, Actual: 0
```

Previously, the object returned by `getState()` was a direct reference to the internal state, so modifications would persist. Now it appears to be returning something different.

### Expected behavior

When I get the state object and modify it, those changes should be reflected in subsequent `getState()` calls, or at least the behavior should be consistent with previous versions.

### Additional context

This is breaking existing code that relied on being able to mutate the state object directly. Is this an intentional breaking change or a regression?

---
Repository: /testbed
