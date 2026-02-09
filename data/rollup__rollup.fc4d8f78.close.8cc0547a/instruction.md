# Bug Report

### Describe the bug

When closing a watcher instance, the `'close'` event is emitted after the watcher has already been marked as closed and listeners have been removed. This causes issues when trying to handle cleanup logic in close event handlers.

### Reproduction

```js
const watcher = new Watcher(/* ... */);

watcher.emitter.on('close', () => {
  console.log('Cleanup logic here');
  // This handler may not execute or may execute unreliably
});

await watcher.close();
// Expected: 'close' event handler should be called
// Actual: Handler doesn't execute because listeners are removed first
```

### Expected behavior

The `'close'` event should be emitted before removing all listeners, so that any registered close handlers can properly execute their cleanup logic. The watcher should only be marked as closed after all cleanup is complete.

### Additional context

This affects any code that relies on the close event for cleanup operations, such as releasing resources or performing final operations before the watcher shuts down.

---
Repository: /testbed
