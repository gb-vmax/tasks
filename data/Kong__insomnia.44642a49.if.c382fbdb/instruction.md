# Bug Report

### Describe the bug

The `remove()` method in `PropertyList` is not working correctly - items are not being removed from the list as expected. When calling `remove()` with either a predicate function or a direct item reference, the list remains unchanged.

### Reproduction

```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });

// Try to remove item with id 2
list.remove(item => item.id === 2, {});

// Expected: list should contain only items 1 and 3
// Actual: list still contains all 3 items
console.log(list.count()); // prints 3 instead of 2
```

Also happens when removing by direct item reference:

```js
const itemToRemove = list.get(1); // get item at index 1
list.remove(itemToRemove, {});
// Item is still in the list
```

### Expected behavior

Items matching the predicate should be removed from the list. The list count should decrease and subsequent operations should reflect the removal.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
