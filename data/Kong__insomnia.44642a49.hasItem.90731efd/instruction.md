# Bug Report

### Describe the bug

After a recent update, the plugin store's `hasItem()` method is not detecting newly created items. When I set an item using `setItem()` and immediately check for it with `hasItem()`, it returns `false` even though the item was just created.

### Reproduction

```js
// Set a new item
await store.setItem('myKey', 'myValue');

// Check if it exists - returns false but should return true
const exists = await store.hasItem('myKey');
console.log(exists); // false (expected: true)
```

The issue seems to happen when:
1. Creating a new item with `setItem()`
2. Immediately checking for its existence with `hasItem()`
3. The check returns `false` even though the item was just stored

This is breaking my plugin's logic that relies on checking if a key exists before performing certain operations.

### Expected behavior

`hasItem()` should return `true` immediately after `setItem()` creates a new item. The method should reflect the current state of the store.

### Additional context

This started happening after the latest update. It works fine if I wait a few seconds between `setItem()` and `hasItem()`, but that's not a reliable workaround for production use.

---
Repository: /testbed
