# Bug Report

### Describe the bug

The `cleanQueue` function in `useQueue` hook is swapping the state and queue values instead of clearing the queue. After calling `cleanQueue()`, the queue contains the previous state and the state contains the previous queue, which is completely backwards.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

function MyComponent() {
  const { state, queue, add, cleanQueue } = useQueue({
    initialValues: ['item1', 'item2']
  });

  // Initial state: state = ['item1', 'item2'], queue = []
  
  add('item3');
  add('item4');
  // Now: state = ['item1', 'item2'], queue = ['item3', 'item4']
  
  cleanQueue();
  // Expected: state = ['item1', 'item2'], queue = []
  // Actual: state = ['item3', 'item4'], queue = ['item1', 'item2']
  
  console.log('State:', state); // Shows ['item3', 'item4'] instead of ['item1', 'item2']
  console.log('Queue:', queue); // Shows ['item1', 'item2'] instead of []
}
```

### Expected behavior

When `cleanQueue()` is called, it should clear the queue array while keeping the state unchanged. The state should remain as it was before calling `cleanQueue()`, and the queue should become an empty array.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
