# Bug Report

### Describe the bug

After a recent update, the store is throwing a syntax error and won't compile. It seems like there's an issue with the code structure in the `createStore` function.

### Reproduction

```js
import { createStore } from '@mantine/store';

const store = createStore({
  user: { name: 'John' }
});

// This will fail to even initialize
store.setState({ user: { name: 'Jane' } });
```

### Expected behavior

The store should compile without errors and `setState` should work normally to update the store state.

### System Info
- @mantine/store version: latest
- Node: 18.x

---
Repository: /testbed
