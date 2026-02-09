# Bug Report

### Describe the bug
I'm experiencing an issue with the MemoryDriver where calling `setItem()` multiple times with the same key doesn't update the value. After the first write, subsequent writes to the same key are silently ignored, leaving the old value in place.

### Reproduction
```js
const driver = new MemoryDriver();

// First write works fine
await driver.setItem('myKey', Buffer.from('initial value'));
console.log(await driver.getItem('myKey')); // Output: <Buffer 69 6e 69 74 69 61 6c 20 76 61 6c 75 65>

// Second write is ignored - the value doesn't update
await driver.setItem('myKey', Buffer.from('updated value'));
console.log(await driver.getItem('myKey')); // Output: <Buffer 69 6e 69 74 69 61 6c 20 76 61 6c 75 65> (still shows "initial value")
```

### Expected behavior
Calling `setItem()` with an existing key should overwrite the previous value, not ignore the new value. The second call should update the stored value to "updated value".

### Additional context
This is breaking sync functionality where we need to update stored data. Also noticed that `keys()` method seems to be returning incorrect results when using prefixes - it's matching keys that don't actually start with the given prefix.

---
Repository: /testbed
