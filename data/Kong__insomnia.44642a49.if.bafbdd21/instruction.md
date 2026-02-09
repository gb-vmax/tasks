# Bug Report

### Describe the bug

The `remove()` method in `PropertyList` is not working as expected. When trying to remove items from the list, the method doesn't return any information about what was removed or whether the operation succeeded. This makes it difficult to know if the removal actually happened.

### Reproduction

```js
const list = new PropertyList();
// Add some items to the list
list.add(item1);
list.add(item2);
list.add(item3);

// Try to remove an item
list.remove(item2, context);

// No way to know if removal succeeded or how many items were removed
```

### Expected behavior

The `remove()` method should provide feedback about the operation, such as:
- How many items were removed
- Whether the list was modified
- Some indication of success/failure

This would be consistent with other collection manipulation methods that typically return information about the operation performed.

### Additional context

Currently the method just silently modifies the internal list without any return value, making it hard to track changes or verify that the removal worked correctly. This is especially problematic when using predicates where you might remove multiple items and want to know how many were affected.

---
Repository: /testbed
