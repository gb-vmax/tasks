# Bug Report

### Describe the bug
The `remove()` method on `PropertyList` is not working correctly when using a predicate function. Instead of removing items that match the predicate, it appears to be keeping them (or behaving in the opposite way).

### Reproduction
```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });

// Try to remove items where id > 1
list.remove(item => item.id > 1);

// Expected: list should only contain item1
// Actual: item1 is removed instead, item2 and item3 remain
```

### Expected behavior
When calling `remove()` with a predicate function, items that match the predicate (where the function returns `true`) should be removed from the list. Currently it seems to be doing the inverse - removing items where the predicate returns `false`.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
