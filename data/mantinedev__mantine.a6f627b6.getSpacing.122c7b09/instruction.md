# Bug Report

### Describe the bug

The `getSpacing` utility function is not working correctly when passed numeric values. It seems like spacing values are being converted to strings and using the wrong CSS variable prefix, which causes spacing to not be applied properly in components.

### Reproduction

```js
import { getSpacing } from '@mantine/core';

// This doesn't work as expected
const spacing = getSpacing(16);
// Returns incorrect CSS variable reference

// Expected to work with numeric values
const spacing2 = getSpacing('md');
```

When using numeric spacing values in components, the spacing doesn't get applied correctly. For example:

```jsx
<Box p={16}>Content</Box>
```

The padding is not being rendered properly.

### Expected behavior

The `getSpacing` function should handle numeric values correctly and use the proper CSS variable prefix (`mantine-spacing` instead of `mantine-spacings`). Spacing values should be applied consistently whether passed as numbers or strings.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
