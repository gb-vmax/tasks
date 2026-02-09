# Bug Report

### Describe the bug

There's an issue with the `patchConsoleError.release()` function where calling it multiple times causes the console.error to be overwritten incorrectly. After the second call to `release()`, console.error gets set to itself instead of the original implementation.

### Reproduction

```js
import { patchConsoleError } from '@mantine-tests/core';

// Patch console.error
patchConsoleError();

// Release once - this works fine
patchConsoleError.release();

// Patch again
patchConsoleError();

// Release again - console.error is now broken
patchConsoleError.release();

// At this point, console.error no longer points to the original implementation
```

### Expected behavior

The `release()` function should always restore console.error to its original implementation, regardless of how many times patch/release is called. Multiple patch/release cycles should work correctly.

### System Info
- Package: @mantine-tests/core
- Version: latest

---
Repository: /testbed
