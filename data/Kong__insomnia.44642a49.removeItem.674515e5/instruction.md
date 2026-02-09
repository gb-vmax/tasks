# Bug Report

### Describe the bug

The `removeItem` method in the memory driver doesn't remove items correctly when the key doesn't reference a Buffer object. I'm trying to delete stored data but it's not being removed from the database.

### Reproduction

```js
const driver = new MemoryDriver();

// Store a regular object
await driver.setItem('mykey', { data: 'test' });

// Try to remove it
const result = await driver.removeItem('mykey');

// Expected: item should be removed and result should be 1
// Actual: item is NOT removed and result is 0
```

The removal only works if the stored value is a Buffer. For any other data type (objects, strings, arrays, etc.), the `removeItem` method returns 0 and the data remains in the database.

### Expected behavior

The `removeItem` method should delete items regardless of their data type and return the number of items removed. Currently it only removes Buffer objects.

### Additional context

This seems to have been introduced recently. The method signature was also changed to return a Promise<number> but the actual removal logic is now checking if the value is a Buffer before deleting, which means non-Buffer values are never removed.

---
Repository: /testbed
