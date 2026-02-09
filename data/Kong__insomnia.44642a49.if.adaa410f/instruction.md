# Bug Report

### Describe the bug

The `upsert()` method in `PropertyList` is not working as expected. When trying to add or update items in a property list, the operation always fails and returns `false`, even when passing valid items.

### Reproduction

```js
const list = new PropertyList();
const item = new Property({ key: 'test', value: 'value' });

// This should add the item but returns false
const result = list.upsert(item);
console.log(result); // Expected: true, Actual: false

// The item is never added to the list
console.log(list.count()); // Expected: 1, Actual: 0
```

### Expected behavior

The `upsert()` method should:
1. Return `true` when successfully adding or updating a valid item
2. Add new items to the list if they don't exist
3. Update existing items if they're already in the list
4. Only return `false` when the item is null/undefined

Currently it seems to be rejecting all valid items instead of accepting them.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
