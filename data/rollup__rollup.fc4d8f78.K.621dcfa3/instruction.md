# Bug Report

### Describe the bug

When using the `once()` method on WatchEmitter, the event listener is not being properly removed after the first invocation. The listener continues to fire on subsequent events even though it should only execute once.

### Reproduction

```js
const emitter = new WatchEmitter();

let callCount = 0;
emitter.once('myEvent', () => {
  callCount++;
  console.log('Event fired, count:', callCount);
});

emitter.emit('myEvent');  // Should fire, callCount = 1
emitter.emit('myEvent');  // Should NOT fire, but does, callCount = 2
emitter.emit('myEvent');  // Should NOT fire, but does, callCount = 3

// Expected: callCount = 1
// Actual: callCount = 3
```

### Expected behavior

The listener registered with `once()` should only execute on the first event emission and then automatically remove itself. Subsequent emissions of the same event should not trigger the listener again.

### System Info
- Latest version from main branch

---
Repository: /testbed
