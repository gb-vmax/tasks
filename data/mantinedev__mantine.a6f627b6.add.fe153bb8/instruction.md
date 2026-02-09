# Bug Report

### Describe the bug

The `useQueue` hook is not maintaining the correct order when adding new items. Items are being added to the beginning of the queue instead of the end, which breaks the FIFO (first-in-first-out) behavior expected from a queue data structure.

### Reproduction

```js
import { useQueue } from '@mantine/hooks';

const { state, queue, add } = useQueue({ 
  initialValues: [1, 2, 3], 
  limit: 3 
});

// Initial state: [1, 2, 3]
console.log(state); // [1, 2, 3]

add(4, 5);

// Expected: [1, 2, 3] with queue [4, 5]
// Actual: [4, 5, 1] with incorrect queue handling
console.log(state);
```

### Expected behavior

New items should be added to the end of the queue, maintaining FIFO order. When the state is at capacity, older items should move to the queue, and new items should be appended after existing items in both state and queue.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
