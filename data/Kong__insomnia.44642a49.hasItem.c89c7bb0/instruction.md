# Bug Report

### Describe the bug

The `hasItem()` method in the plugin store is not working correctly after a recent update. When I call `setItem()` to store a value and then immediately check with `hasItem()`, it returns `false` even though the item was just stored.

### Reproduction

```js
// Store a value
await store.setItem('myKey', 'myValue');

// Check if it exists - returns false but should return true
const exists = await store.hasItem('myKey');
console.log(exists); // false (unexpected!)

// If I wait a bit and check again, it works
setTimeout(async () => {
  const existsLater = await store.hasItem('myKey');
  console.log(existsLater); // true (expected)
}, 100);
```

This is particularly problematic when doing sequential operations like:
1. Check if key exists
2. If not, create it with setItem
3. Verify it was created with hasItem
4. Step 3 fails even though step 2 succeeded

### Expected behavior

`hasItem()` should return `true` immediately after `setItem()` completes successfully. The method should reflect the current state of the store, not a cached/stale value.

### Additional context

This seems to have started happening recently. I'm using the plugin store API to persist configuration data, and this behavior is breaking my plugin's initialization logic.

---
Repository: /testbed
