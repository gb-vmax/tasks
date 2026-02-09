# Bug Report

### Describe the bug

I'm experiencing an issue with assignment expressions where compound assignment operators (like `+=`, `-=`, `*=`, etc.) are not being handled correctly. It seems like the logic for determining whether to access properties before assignment has been inverted.

### Reproduction

```js
let obj = { count: 0 };

// Compound assignment should read the property first, then assign
obj.count += 5;  // Expected: read obj.count (0), add 5, assign result (5)

// Simple assignment should NOT read the property first
obj.count = 10;  // Expected: just assign 10 without reading current value
```

The behavior appears to be backwards - simple assignments (`=`) are treating the left-hand side as if it needs to be accessed first, while compound assignments (`+=`, `-=`, etc.) are not checking if the property needs to be read before the operation.

### Expected behavior

- For compound assignments (`+=`, `-=`, `*=`, `/=`, etc.), the left-hand side should be accessed/read before performing the assignment since these operators need the current value
- For simple assignments (`=`), the left-hand side should NOT be accessed before assignment since we're just overwriting the value

This affects tree-shaking and side effect detection, as the bundler may incorrectly include or exclude code based on whether property accesses are considered to have effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
