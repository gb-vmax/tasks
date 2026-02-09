# Bug Report

### Describe the bug

The `useQueue` hook is not maintaining the correct state when adding new items. After adding items to the queue, the current state array doesn't include previously active items - they seem to get lost during the add operation.

### Reproduction

```js
const { state, add } = useQueue({ initialValues: [1, 2, 3], limit: 3 });

// Initial state: [1, 2, 3]
console.log(state); // [1, 2, 3]

// Add new items
add(4, 5);

// Expected state: [1, 2, 3] (limit is 3, so first 3 items should remain in state)
// Actual state: Items 1, 2, 3 are missing from state
console.log(state); // Does not contain the original items
```

### Expected behavior

When adding new items to the queue, the existing state items should be preserved up to the limit. The `add` function should append new items to the end of the combined state + queue, then slice appropriately to maintain the limit for active state items.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
