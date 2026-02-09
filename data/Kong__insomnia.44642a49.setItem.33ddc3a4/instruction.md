# Bug Report

### Describe the bug
I'm experiencing an issue with the memory driver where stored data is being corrupted. When I store a Buffer value and then retrieve it, the data I get back is different from what I originally stored.

### Reproduction
```js
const driver = new MemoryDriver();

// Store binary data
const originalData = Buffer.from([0x00, 0x01, 0x02, 0xFF]);
await driver.setItem('myKey', originalData);

// Retrieve the data
const retrieved = await driver.getItem('myKey');

// The retrieved data doesn't match the original
console.log('Original:', originalData);
console.log('Retrieved:', retrieved);
// Expected: Buffer containing [0x00, 0x01, 0x02, 0xFF]
// Actual: Something different
```

### Expected behavior
The data retrieved from the memory driver should be identical to the data that was stored. Binary data should be preserved exactly as it was written.

### Additional context
This seems to affect any binary data stored through the memory driver. The issue appears when working with the sync store functionality.

---
Repository: /testbed
