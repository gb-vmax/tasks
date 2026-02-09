# Bug Report

### Describe the bug
When using `insertAfter()` with negative indices on a PropertyList, the method doesn't handle them correctly. Negative indices should count from the end of the list (similar to how array indices work in many languages), but currently they're not being processed properly.

### Reproduction
```js
const list = new PropertyList();
list.append(item1);
list.append(item2);
list.append(item3);

// Trying to insert after the second-to-last item using negative index
list.insertAfter(newItem, -2);

// Expected: newItem should be inserted after item2
// Actual: newItem gets appended to the end instead
```

### Expected behavior
Negative indices should be normalized to count from the end of the list. For example:
- `-1` should refer to the last item
- `-2` should refer to the second-to-last item
- etc.

The item should be inserted at the correct position based on the normalized index.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
