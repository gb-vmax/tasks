# Bug Report

### Describe the bug

The `upsert` method in `PropertyList` is completely broken after a recent change. When trying to upsert items into a property list, the method fails to execute properly and doesn't add or update items as expected.

### Reproduction

```js
const propertyList = new PropertyList();

// Try to add a new item
const newItem = { id: '1', name: 'test' };
const result = propertyList.upsert(newItem);

// Expected: item should be added to the list
// Actual: method doesn't work correctly, item is not properly handled
```

Also trying to update an existing item:

```js
const propertyList = new PropertyList();
propertyList.add({ id: '1', name: 'original' });

// Try to update the existing item
const updatedItem = { id: '1', name: 'updated' };
propertyList.upsert(updatedItem);

// Expected: existing item should be updated
// Actual: update behavior is broken
```

### Expected behavior

- `upsert()` should add new items when they don't exist in the list
- `upsert()` should update existing items when they already exist (based on `indexOf`)
- The method should return `true` for new items and `false` for updates (or vice versa based on the intended behavior)

### Additional context

This appears to have started happening recently. The method seems to have some code structure issues that prevent it from functioning at all. Looking at the implementation, there seems to be duplicate or malformed code in the upsert method.

---
Repository: /testbed
