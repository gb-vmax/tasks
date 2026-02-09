# Bug Report

### Describe the bug

The `insertAfter` method in `PropertyList` is not working correctly. When I try to insert an item after a specific position, it seems to be appending the item twice instead of inserting it at the correct position.

### Reproduction

```js
const list = new PropertyList();
list.append(item1);
list.append(item2);
list.append(item3);

// Try to insert item4 after position 1
list.insertAfter(item4, 1);

// Expected: [item1, item2, item4, item3]
// Actual: items appear to be duplicated or inserted in wrong position
```

### Expected behavior

The `insertAfter` method should insert the new item immediately after the specified position. If I call `insertAfter(item, 1)`, the item should be inserted at index 2 (after the item at index 1).

### Additional context

This seems to have started happening recently. The method appears to be executing append logic multiple times or in an unexpected way.

---
Repository: /testbed
