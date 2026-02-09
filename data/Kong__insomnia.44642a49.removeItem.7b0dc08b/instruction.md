# Bug Report

### Describe the bug
The `removeItem` method in the memory driver is returning a count instead of just deleting items. This breaks existing code that expects `removeItem` to return `void` (or a Promise<void>).

### Reproduction
```js
const driver = new MemoryDriver();
await driver.setItem('key1', Buffer.from('value1'));

// This now returns a number instead of void
const result = await driver.removeItem('key1');
// result is 1, but should be undefined
```

### Expected behavior
The `removeItem` method should delete the item and not return anything (void/undefined), consistent with the original implementation and typical key-value store behavior.

### Additional context
This appears to have changed recently. The method signature suggests it should return `Promise<void>` but the implementation now returns a count. This is causing issues in code that doesn't expect a return value from `removeItem`.

---
Repository: /testbed
