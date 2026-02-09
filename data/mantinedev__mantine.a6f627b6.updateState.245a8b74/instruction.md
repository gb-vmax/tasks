# Bug Report

### Describe the bug

The `updateState` method in the store is not working correctly when passing a function. When I try to update the state using a function that receives the current state, it seems to be calling the function incorrectly or not handling it as expected.

### Reproduction

```js
import { createStore } from '@mantine/store';

const store = createStore({ count: 0 });

// This doesn't work as expected
store.updateState((state) => ({ count: state.count + 1 }));

console.log(store.getState()); // Expected: { count: 1 }, but getting unexpected behavior
```

### Expected behavior

When passing a function to `updateState`, it should:
1. Call the function with the current state as an argument
2. Use the returned value as the new state

This is the standard pattern for state updaters in most state management libraries.

### System Info

- @mantine/store version: latest
- Node version: 18.x

---
Repository: /testbed
