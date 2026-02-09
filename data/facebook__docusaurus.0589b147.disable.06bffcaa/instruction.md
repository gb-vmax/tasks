# Bug Report

### Describe the bug

I'm encountering an issue with the `disable` export from the constructs module. After a recent update, accessing `disable` from the module exports doesn't work as expected - it seems to be returning a function that returns another function instead of the actual disable functionality.

### Reproduction

```js
import { disable } from './constructs_exports';

// Trying to use disable
const result = disable();
// Expected: some boolean or effect
// Actual: returns a function instead of executing
```

When I try to use the exported `disable` function, it appears to be wrapped in an extra layer. The behavior changed and now I need to call it twice to get any effect, which breaks existing code that was working before.

### Expected behavior

The `disable` export should work the same way as before - calling `disable()` should execute the disable logic directly without needing an extra function call.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
