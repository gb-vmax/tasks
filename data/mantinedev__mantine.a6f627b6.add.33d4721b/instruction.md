# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with the `useQueue` hook when adding items. The order of items in the queue seems to be reversed - newly added items appear at the beginning instead of being appended to the end. Additionally, it looks like items are being dropped from the queue incorrectly.

### Reproduction

```js
const { state, queue, add } = useQueue({
  initialValues: [1, 2, 3],
  limit: 3
});

// Initial state: [1, 2, 3]
// Queue should be empty

add(4, 5);

// Expected: state = [1, 2, 3], queue = [4, 5]
// Actual: state = [4, 5, 1], queue appears incorrect
```

When I add new items, they're appearing at the front of the state instead of being properly queued at the end. This breaks the expected FIFO behavior of a queue.

### Expected behavior

New items should be added to the end of the queue, not the beginning. The state should maintain the first `limit` items in order, and any additional items should go into the queue array to be processed later.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
