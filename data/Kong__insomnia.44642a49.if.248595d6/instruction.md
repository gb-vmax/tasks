# Bug Report

### Describe the bug
When using `PropertyList.remove()` with a predicate function, items that should be removed are being kept instead, and items that should be kept are being removed. The behavior is completely inverted from what's expected.

### Reproduction
```js
const list = new PropertyList();
list.append({ id: 1, name: 'item1' });
list.append({ id: 2, name: 'item2' });
list.append({ id: 3, name: 'item3' });

// Try to remove items where id > 1
// Expected: item1 should remain, item2 and item3 should be removed
// Actual: item1 is removed, item2 and item3 remain
list.remove(item => item.id > 1, {});

console.log(list.count()); // Shows 2 instead of 1
console.log(list.toJSON()); // Shows item2 and item3 instead of item1
```

### Expected behavior
When calling `remove()` with a predicate function, items where the predicate returns `true` should be removed from the list, and items where it returns `false` should remain.

In the example above, after `list.remove(item => item.id > 1, {})`, only `item1` (where `id === 1`) should remain in the list.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
