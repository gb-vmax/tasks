# Bug Report

### Describe the bug

The `upsert()` method in PropertyList appears to be broken after a recent update. When trying to use it, I'm getting unexpected behavior - the method seems to be duplicated or malformed in some way.

### Reproduction

```js
const propertyList = new PropertyList();
const item = new Property({ key: 'test', value: 'value1' });

// Try to upsert an item
propertyList.upsert(item);

// This throws an error or behaves unexpectedly
```

### Expected behavior

The `upsert()` method should work as before - inserting new items or updating existing ones based on whether the item already exists in the list. It should return `true` when inserting a new item and `false` when updating an existing one.

### Additional context

This seems to have started happening recently. The method was working fine before but now something is wrong with its implementation. Not sure if this was from a bad merge or what, but the code doesn't look right.

---
Repository: /testbed
