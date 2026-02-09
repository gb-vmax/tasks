# Bug Report

### Describe the bug

The `PropertyList.remove()` method isn't returning the removed items anymore. After removing items from a PropertyList, there's no way to know which items were actually removed from the list.

### Reproduction

```js
const list = new PropertyList();
list.add({ key: 'item1', value: 'test1' });
list.add({ key: 'item2', value: 'test2' });
list.add({ key: 'item3', value: 'test3' });

// Try to remove items and get the removed ones
const removed = list.remove(item => item.key === 'item2');

// Expected: removed should contain the removed item(s)
// Actual: removed is undefined
console.log(removed); // undefined
```

### Expected behavior

The `remove()` method should return an array of the items that were removed from the list, similar to how array methods like `splice()` work. This would allow users to:
1. Verify which items were actually removed
2. Perform cleanup or logging operations on removed items
3. Potentially undo remove operations

### System Info
- insomnia-sdk version: latest
- Using both function predicates and direct object comparisons for removal

This is particularly problematic when using predicate functions where you want to confirm which items matched the removal criteria.

---
Repository: /testbed
