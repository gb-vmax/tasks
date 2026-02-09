# Bug Report

### Describe the bug

I'm encountering an issue with the `arguments` object handling in function contexts. When accessing properties of the `arguments` object, it seems like the deoptimization of arguments is happening at the wrong time, causing the array to be cleared before it's actually processed.

### Reproduction

```js
function test() {
  // Access arguments object properties
  return arguments[0] + arguments.length;
}

// The deoptimization seems to occur prematurely
// Arguments are cleared before being properly deoptimized
```

This appears to be related to how the `ArgumentsVariable` class processes path inclusions. The deoptimization logic runs in an unexpected order.

### Expected behavior

Arguments should be deoptimized before the array is cleared, not after. The current behavior causes the deoptimization loop to iterate over an empty array, which means arguments aren't properly handled during the inclusion phase.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
