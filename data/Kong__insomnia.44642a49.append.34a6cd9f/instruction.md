# Bug Report

### Describe the bug

The `append()` method in `PropertyList` is now silently failing when trying to add items with duplicate index values. Previously, calling `append()` would add the item to the list, but now it returns `false` without any indication of why the operation failed.

### Reproduction

```js
const list = new PropertyList(SomePropertyClass, []);

// Add an item with id 'test'
const item1 = new SomePropertyClass({ id: 'test', name: 'First' });
list.append(item1);

// Try to add another item with the same id
const item2 = new SomePropertyClass({ id: 'test', name: 'Second' });
list.append(item2); // This now silently fails and returns false

console.log(list.count()); // Expected: 2, Actual: 1
```

### Expected behavior

Either the duplicate item should be added to the list (previous behavior), or there should be clear documentation/error messaging about why duplicate index values are being rejected. The silent failure makes it difficult to debug why items aren't being added to the list.

### Additional context

This appears to be a breaking change in behavior. Code that was working before now fails silently without any way to know that the append operation was rejected due to a duplicate index value.

---
Repository: /testbed
