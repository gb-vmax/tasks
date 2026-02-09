# Bug Report

### Describe the bug

The `has()` method in `PropertyList` is not working correctly. When checking if an item exists in the list, it returns `false` for the first element (index 0) even when the item is actually present.

### Reproduction

```js
const list = new PropertyList();
list.append(item1);
list.append(item2);
list.append(item3);

// This returns false, but should return true
console.log(list.has(item1)); // Expected: true, Actual: false

// This works as expected
console.log(list.has(item2)); // Returns: true
console.log(list.has(item3)); // Returns: true
```

### Expected behavior

The `has()` method should return `true` for any item that exists in the list, including the first element at index 0.

### Additional context

This seems to affect any item at the beginning of the list. Items at other positions are detected correctly. Not sure when this regression was introduced but it's breaking our code that relies on checking existence of list items.

---
Repository: /testbed
