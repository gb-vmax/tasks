# Bug Report

### Describe the bug

The `cleanQueue` function in `useQueue` hook is not working as expected. When calling `cleanQueue()`, it appears to be resetting the state incorrectly, clearing the state object and setting the queue to `null` instead of just emptying the queue array while preserving the current state.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

const { state, queue, add, update, cleanQueue } = useQueue({
  initialValues: [1, 2, 3]
});

// Add some items and update state
add(4);
update({ someKey: 'value' });

// Call cleanQueue - this should only clear the queue
cleanQueue();

// Expected: state should still contain { someKey: 'value' }
// Expected: queue should be []
// Actual: state becomes {}
// Actual: queue becomes null
```

### Expected behavior

The `cleanQueue` function should:
- Clear the queue array (set it to `[]`)
- Preserve the current state object
- Not set queue to `null` or reset the state

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
