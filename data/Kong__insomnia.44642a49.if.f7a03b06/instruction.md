# Bug Report

### Describe the bug

After a recent update, the `upsert()` method in PropertyList appears to be broken. When trying to upsert items into a property list, I'm getting syntax errors and the method doesn't work at all.

### Reproduction

```js
const propertyList = new PropertyList();
const item = new Property({ id: 'test', value: 'data' });

// This should either add or update the item
propertyList.upsert(item);
```

### Expected behavior

The `upsert()` method should:
1. Add the item if it doesn't exist in the list
2. Update the item if it already exists
3. Return `true` if added, `false` if updated

Currently the code seems malformed and won't execute at all.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
