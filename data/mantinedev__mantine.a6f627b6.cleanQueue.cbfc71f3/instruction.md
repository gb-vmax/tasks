# Bug Report

### Describe the bug

The `cleanQueue` function in `useQueue` hook is behaving incorrectly - it appears to be swapping the state and queue values instead of clearing the queue while preserving the state.

### Reproduction

```tsx
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
}
```

After calling `cleanQueue()`, the state and queue appear to be swapped instead of the queue being cleared.

### Expected behavior

When `cleanQueue()` is called, it should:
- Keep the current `state` unchanged
- Clear the `queue` to an empty array

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
