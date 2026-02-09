# Bug Report

### Describe the bug
I'm experiencing an issue with the `remove()` method on `PropertyList` objects. When trying to remove items using a predicate function, the behavior is completely wrong - it seems to be doing the opposite of what it should do or corrupting the list entirely.

### Reproduction
```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });

// Try to remove items where id > 1
list.remove(item => item.id > 1);

// Expected: only item with id=1 should remain
// Actual: list is either empty, contains wrong items, or throws an error
```

### Expected behavior
When calling `remove()` with a predicate function, items that match the predicate should be removed from the list, and items that don't match should remain. For example, if I want to remove all items where `id > 1`, only the item with `id: 1` should stay in the list.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is blocking our workflow as we rely heavily on the remove functionality with custom predicates. Any help would be appreciated!

---
Repository: /testbed
