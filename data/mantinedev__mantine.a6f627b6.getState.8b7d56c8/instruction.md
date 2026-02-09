# Bug Report

### Describe the bug

After a recent update, the store's `getState()` method is returning incorrect values. When I try to retrieve the state, I'm getting an empty object instead of the actual state I set previously.

### Reproduction

```js
import { createStore } from '@mantine/store';

const store = createStore({ count: 5, name: 'test' });

// Set some state
store.setState({ count: 10, name: 'updated' });

// Try to get the state
const state = store.getState();
console.log(state); // Expected: { count: 10, name: 'updated' }
                    // Actual: {} (empty object)
```

### Expected behavior

`getState()` should return the current state that was set with `setState()`. The state values should persist and be retrievable.

### Additional context

This seems to have broken after the latest changes. The store was working fine before, but now it's like the state is being reset or cleared every time I call `getState()`. This is breaking my entire application since I can't access any stored values.

---
Repository: /testbed
