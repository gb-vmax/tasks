# Bug Report

### Describe the bug

I'm experiencing an issue with the memory driver where items aren't being properly removed from storage. After calling `removeItem()`, the item still exists in the database object but with an `undefined` value instead of being completely deleted.

### Reproduction

```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('myKey', 'myValue');

// Remove the item
await driver.removeItem('myKey');

// Check if key still exists
// Expected: key should not exist in the database
// Actual: key exists with undefined value
```

When iterating over the database keys or checking for key existence, the removed items still appear in the object, which causes issues with operations that rely on checking what keys are present.

### Expected behavior

When `removeItem()` is called, the key should be completely removed from the internal database object (like using `delete`), not just set to `undefined`. This is important for:
- Accurate key enumeration
- Proper storage size calculations
- Checking if an item exists vs. checking if it's undefined

### System Info
- Package: @insomnia/sync
- Component: MemoryDriver

---
Repository: /testbed
