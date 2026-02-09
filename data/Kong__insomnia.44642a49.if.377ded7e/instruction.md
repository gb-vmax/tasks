# Bug Report

### Describe the bug
When using `insertAfter()` method on a PropertyList with negative indices, the method doesn't handle them correctly. Negative indices should work like they do in Python or other languages where `-1` refers to the last element, `-2` to the second-to-last, etc.

### Reproduction
```js
const list = new PropertyList();
list.append(item1);
list.append(item2);
list.append(item3);

// Try to insert after the last element using negative index
list.insertAfter(newItem, -1);
// Expected: newItem should be inserted after item3
// Actual: newItem is appended to the end (same position, but logic doesn't handle negative indices)

// Try to insert after second-to-last element
list.insertAfter(anotherItem, -2);
// Expected: anotherItem should be inserted after item2
// Actual: Doesn't work as expected
```

### Expected behavior
The `insertAfter()` method should support negative indices similar to how arrays work in many languages:
- `-1` should refer to the last element
- `-2` should refer to the second-to-last element
- And so on...

Currently it seems like negative indices are either ignored or treated as invalid, causing the item to just be appended to the end instead of being inserted at the correct position.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
