# Bug Report

### Describe the bug

The `useQueue` hook is not managing items correctly when adding new elements. After calling `add()`, the state and queue are not being populated as expected - items seem to be sliced incorrectly, resulting in missing or misplaced elements.

### Reproduction

```js
const { state, queue, add } = useQueue({ 
  initialValues: [1, 2, 3], 
  limit: 2 
});

// Initial state should be [1, 2] and queue should be [3]
console.log(state); // Expected: [1, 2]
console.log(queue); // Expected: [3]

// Add new items
add(4, 5);

// After adding, state and queue are incorrect
console.log(state); // Expected: [1, 2], but getting wrong values
console.log(queue); // Expected: [3, 4, 5], but getting wrong values
```

### Expected behavior

When adding items to the queue:
1. The `state` should contain the first `limit` items from the combined array of current state, queue, and new items
2. The `queue` should contain all remaining items after the limit
3. Items should maintain their order and not be lost

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
