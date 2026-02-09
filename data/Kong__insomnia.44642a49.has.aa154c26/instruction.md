# Bug Report

### Describe the bug

The `has()` method in `PropertyList` is not working correctly for the first element in the list. When checking if an item exists at index 0, the method returns `false` even though the item is present in the list.

### Reproduction

```js
const list = new PropertyList();
list.add(item1);
list.add(item2);

// This returns false even though item1 is in the list
console.log(list.has(item1)); // Expected: true, Actual: false

// This works correctly
console.log(list.has(item2)); // Returns: true
```

### Expected behavior

The `has()` method should return `true` for any item that exists in the list, including items at index 0.

### Additional context

This seems to affect only the first element in the list. All other elements are detected correctly. This is causing issues when trying to check for the existence of items that were added first to a PropertyList.

---
Repository: /testbed
