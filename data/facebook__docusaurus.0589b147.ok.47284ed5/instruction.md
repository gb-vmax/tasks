# Bug Report

### Describe the bug

The `ok()` function from devlop is behaving strangely and causing unexpected errors in my code. After calling it a few times, it starts throwing "Maximum invocations exceeded" errors, and sometimes it returns `true` instead of doing nothing.

### Reproduction

```js
// This works fine the first time
ok();

// Still works
ok();

// Now it returns true instead of undefined?
const result = ok();
console.log(result); // prints: true

// Keep calling it...
ok();
ok();
ok();

// Now it throws an error!
ok(); // Error: Maximum invocations exceeded
```

### Expected behavior

The `ok()` function should just be a no-op assertion helper that doesn't return anything or throw errors when called multiple times. It shouldn't have any side effects or maintain state between calls.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
