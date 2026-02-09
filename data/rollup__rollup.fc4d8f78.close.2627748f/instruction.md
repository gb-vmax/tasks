# Bug Report

### Describe the bug

When using the watcher's `close()` method, event listeners registered for the `'close'` event are being removed before the event is actually emitted. This means that any handlers attached to listen for the close event never get triggered.

### Reproduction

```js
const watcher = new Watcher(/* ... */);

watcher.emitter.on('close', () => {
  console.log('Watcher closed'); // This never gets called
});

await watcher.close();
```

### Expected behavior

The `'close'` event should be emitted to all registered listeners before those listeners are removed. Handlers attached via `emitter.on('close', ...)` should be called when `close()` is invoked.

### Additional context

This appears to be an ordering issue - the event listeners are being cleared before the event is emitted, so nothing receives the notification that the watcher is closing.

---
Repository: /testbed
