# Bug Report

### Describe the bug

The `PropertyList.remove()` method is not working as expected. When trying to remove items from a property list, all matching items are being removed instead of respecting a limit on the number of items to remove.

### Reproduction

```js
const list = new PropertyList();
list.add({ id: 1, name: 'item1' });
list.add({ id: 2, name: 'item2' });
list.add({ id: 3, name: 'item3' });
list.add({ id: 4, name: 'item4' });

// Try to remove only 2 items matching the predicate
const context = { _maxRemove: 2 };
list.remove(item => item.id > 0, context);

// Expected: 2 items removed, 2 items remain
// Actual: All 4 items are removed
```

### Expected behavior

When a `_maxRemove` property is provided in the context object, the `remove()` method should only remove up to that number of matching items. The remaining matching items should stay in the list.

For example, if there are 4 matching items and `_maxRemove` is set to 2, only the first 2 matching items should be removed, leaving 2 items in the list.

### System Info

- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
