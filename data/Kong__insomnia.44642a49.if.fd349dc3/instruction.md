# Bug Report

### Describe the bug

The `remove()` method in `PropertyList` is not working as expected - it appears to be keeping items that should be removed instead of removing them when using a predicate function.

### Reproduction

```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });

// Try to remove items where id > 1
list.remove(item => item.id > 1, {});

// Expected: list should only contain item with id: 1
// Actual: list still contains items with id: 2 and 3
console.log(list.all()); // Shows all items are still present
```

### Expected behavior

When calling `remove()` with a predicate function, items matching the predicate should be removed from the list. In the example above, items with `id: 2` and `id: 3` should be removed, leaving only the item with `id: 1`.

### Additional context

This seems to have started happening recently. The method works correctly when passing an object directly (non-function predicate), but fails when using a function predicate.

---
Repository: /testbed
