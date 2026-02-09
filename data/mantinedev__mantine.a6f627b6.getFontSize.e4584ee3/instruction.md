# Bug Report

### Describe the bug
When using `getFontSize()` utility function, it's returning incorrect CSS variable references. The function appears to be generating the wrong CSS variable name, which results in font sizes not being applied correctly.

### Reproduction
```js
import { getFontSize } from '@mantine/core';

// This returns the wrong CSS variable
const fontSize = getFontSize('md');
// Expected: var(--mantine-font-size-md)
// Actual: var(--mantine-size-md)
```

### Expected behavior
The `getFontSize()` function should return a reference to the `--mantine-font-size-*` CSS variable, not `--mantine-size-*`. This causes font sizes to not be applied properly in components that rely on this utility.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
