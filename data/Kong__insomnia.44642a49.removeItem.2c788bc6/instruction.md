# Bug Report

### Describe the bug

The `removeItem` method in the memory driver is not working as expected. When trying to remove a simple key-value pair from the store, the item is not being deleted. It seems like the method now only removes items when the key contains wildcards (`*`), ends with a slash (`/`), or the value is a Buffer.

### Reproduction

```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('myKey', 'myValue');

// Try to remove it
await driver.removeItem('myKey');

// The item is still there!
const value = await driver.getItem('myKey');
console.log(value); // Expected: undefined, Actual: 'myValue'
```

### Expected behavior

Calling `removeItem('myKey')` should delete the key from the internal database, regardless of whether it's a Buffer, contains wildcards, or has special characters. Regular string values should be removable just like they were before.

### Additional context

This appears to be a regression - the method used to simply delete the key, but now it has additional logic that prevents normal string values from being removed. Only Buffer values seem to be deletable now, which breaks the basic functionality of the store.

---
Repository: /testbed
