# Bug Report

### Describe the bug

After a recent update, plugin data storage seems to be returning incorrect values when retrieving items. When I store a value using `setItem()` and then immediately retrieve it with `getItem()`, the returned value doesn't match what was originally stored.

### Reproduction

```js
// Store a simple string value
await store.setItem('myKey', 'hello world');

// Retrieve the value
const value = await store.getItem('myKey');

console.log(value); // Expected: 'hello world', but getting something different
```

Also seeing issues with JSON data:

```js
// Store a number as string
await store.setItem('count', '42');

// Get it back
const count = await store.getItem('count');
console.log(count); // Not returning '42' as expected
```

### Expected behavior

`getItem()` should return the exact same value that was stored with `setItem()`. If I store `'hello world'`, I should get back `'hello world'`, not a modified or processed version of it.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking my plugin's state management. Any help would be appreciated!

---
Repository: /testbed
