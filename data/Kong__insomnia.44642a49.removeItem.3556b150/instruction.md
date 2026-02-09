# Bug Report

### Describe the bug

When using the plugin store's `removeItem()` method, the operation is taking significantly longer than expected. After removing items from the store, there's a noticeable delay before the method completes, especially when removing multiple items in succession.

### Reproduction

```js
const store = context.store;

// Removing a single item takes much longer than before
await store.removeItem('myKey');

// Removing multiple items becomes very slow
for (let i = 0; i < 10; i++) {
  await store.removeItem(`key${i}`);
}
```

### Expected behavior

The `removeItem()` method should execute quickly and efficiently, similar to how it worked in previous versions. Removing items should be a fast operation without any unexpected delays.

### Additional context

This seems to have started happening recently. The delay is more noticeable when there are already many items in the plugin store. Not sure if this is related to any recent changes to the store implementation.

---
Repository: /testbed
