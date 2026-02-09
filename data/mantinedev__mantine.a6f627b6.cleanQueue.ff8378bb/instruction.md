# Bug Report

### Describe the bug

The `cleanQueue` function in `useQueue` hook is not working correctly. When calling `cleanQueue()`, it seems to be corrupting the state structure instead of just clearing the queue array.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

function MyComponent() {
  const { state, queue, add, update, cleanQueue } = useQueue({
    initialValues: [{ id: 1, value: 'test' }]
  });

  // Add some items to the queue
  add({ id: 2, value: 'item1' });
  add({ id: 3, value: 'item2' });

  // Try to clean the queue
  cleanQueue();

  // After cleanQueue(), the state structure appears broken
  console.log(state); // Expected: [{ id: 1, value: 'test' }]
}
```

### Expected behavior

After calling `cleanQueue()`, the queue should be emptied while the state should remain unchanged and maintain its proper structure.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
