# Bug Report

### Describe the bug
The `remove()` method in `PropertyList` is not working correctly - it's keeping items that should be removed and removing items that should be kept. The behavior is completely reversed from what's expected.

### Reproduction
```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });

// Try to remove items where id > 1
list.remove(item => item.id > 1);

// Expected: list should contain only item1 (id: 1)
// Actual: list contains item2 and item3 (ids 2 and 3)
```

### Expected behavior
When using a predicate function with `remove()`, items matching the predicate should be removed from the list. Instead, items matching the predicate are being kept and everything else is removed.

For example:
- `list.remove(item => item.id === 2)` should remove the item with id 2, but it removes everything except that item
- `list.remove(item => item.active === false)` should remove inactive items, but it removes all active items instead

This makes the method completely unusable as it does the opposite of what's documented.

---
Repository: /testbed
