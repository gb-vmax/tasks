# Bug Report

### Describe the bug

I'm experiencing an issue with the `useQueue` hook where items are being duplicated and the queue management is not working as expected. When adding items to the queue, the current state appears to be duplicated instead of properly combining the state and queue.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

const { state, queue, add } = useQueue({
  initialValues: [1, 2, 3],
  limit: 3
});

// Initial state: [1, 2, 3]
// Initial queue: []

add(4, 5);

// Expected state: [1, 2, 3]
// Expected queue: [4, 5]

// Actual behavior: state contains duplicated values
// and queue is not managed correctly
```

### Expected behavior

When adding items to a queue that's at its limit, the new items should go into the queue portion. The current state should remain unchanged until items are removed, and the queue should hold the overflow items. Items should not be duplicated.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
