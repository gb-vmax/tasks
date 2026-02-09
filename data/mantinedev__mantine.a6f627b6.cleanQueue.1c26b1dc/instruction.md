# Bug Report

### Describe the bug

I'm experiencing an issue with the `useQueue` hook where calling `cleanQueue()` causes the state to be overwritten incorrectly. After cleaning the queue, the `state` property seems to contain the wrong data - it appears to be set to the queue contents instead of maintaining the current state.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

const { state, queue, add, update, cleanQueue } = useQueue({
  initialValues: ['item1', 'item2']
});

// Add some items to the queue
add('item3');
add('item4');

// At this point:
// state = ['item1', 'item2']
// queue = ['item3', 'item4']

// Clean the queue
cleanQueue();

// Expected: state = ['item1', 'item2'], queue = []
// Actual: state gets corrupted with queue data
```

### Expected behavior

When `cleanQueue()` is called, it should clear the queue array while keeping the state unchanged. The state should remain as it was before calling `cleanQueue()`.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
