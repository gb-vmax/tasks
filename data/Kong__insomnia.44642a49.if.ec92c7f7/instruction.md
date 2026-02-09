# Bug Report

### Describe the bug

The `insertAfter` method in `PropertyList` seems to have duplicate code that causes unexpected behavior. When trying to insert an item after a specific position, the method appears to append the item twice - once in the intended position and once at the end of the list.

### Reproduction

```js
const list = new PropertyList();
list.append(item1);
list.append(item2);
list.append(item3);

// Try to insert item4 after position 1
list.insertAfter(item4, 1);

// Expected: [item1, item2, item4, item3]
// Actual: [item1, item2, item4, item3, item4] (duplicate item4)
```

### Expected behavior

The `insertAfter` method should only insert the item once at the specified position. If the position is invalid, it should append to the end, but not do both operations.

### System Info

- insomnia-sdk version: latest
- The issue appears after recent changes to the PropertyList class

---
Repository: /testbed
