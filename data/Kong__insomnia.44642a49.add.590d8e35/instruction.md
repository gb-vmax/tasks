# Bug Report

### Describe the bug

I'm experiencing strange behavior with the `PropertyList.add()` method. When adding items to a PropertyList, duplicate entries are being created under certain conditions. It seems like items are being added multiple times when they shouldn't be.

### Reproduction

```js
const propertyList = new PropertyList();

// Add some properties
propertyList.add(property1);
propertyList.add(property2);
propertyList.add(property3);

// After adding 3 items, the list contains 4 items somehow
console.log(propertyList.list.length); // Expected: 3, Actual: 4
```

The issue appears to happen when the list reaches an even number of items. Adding a new item at that point results in duplicates being added to the list.

### Steps to reproduce
1. Create a new PropertyList instance
2. Add an odd number of properties (e.g., 1 or 3)
3. Add one more property to make it an even count
4. Check the list length - it will be higher than expected

### Expected behavior

Each call to `add()` should add exactly one item to the list. The list should not contain duplicate entries unless explicitly added by the user.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
