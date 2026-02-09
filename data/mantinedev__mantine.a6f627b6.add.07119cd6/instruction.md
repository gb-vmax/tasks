# Bug Report

### Describe the bug

The `useQueue` hook is duplicating items in the state when adding new elements. When I call the `add` method, items that are already in the state appear twice, causing the queue to contain duplicate entries.

### Reproduction

```js
const { state, add } = useQueue({ 
  initialValues: ['item1', 'item2'],
  limit: 5 
});

// Initial state: ['item1', 'item2']
add('item3');
// Expected state: ['item1', 'item2', 'item3']
// Actual state: ['item1', 'item2', 'item1', 'item2', 'item3']
```

The state array is being duplicated before adding new items, which leads to incorrect behavior when managing the queue.

### Expected behavior

When adding new items to the queue, the existing state should not be duplicated. The `add` method should append new items to the current state and queue without creating duplicates of existing items.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
