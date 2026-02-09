# Bug Report

### Describe the bug

When using `AppShell` with padding configuration, the padding values are not being applied correctly. It seems like the base padding value is being ignored when using responsive padding objects, and primitive padding values are not being processed through the size conversion properly.

### Reproduction

```jsx
import { AppShell } from '@mantine/core';

// Case 1: Primitive padding value
<AppShell padding="md">
  {/* Content */}
</AppShell>

// Case 2: Responsive padding with base value
<AppShell padding={{ base: 'md', sm: 'lg' }}>
  {/* Content */}
</AppShell>
```

### Expected behavior

- For primitive padding values (e.g., `padding="md"`), the padding should be converted to the appropriate CSS value using the theme's size system
- For responsive padding objects with a `base` property, the base padding value should be applied to the `--app-shell-padding` CSS variable and used as the default padding before any media queries kick in

### Actual behavior

The padding is either not applied at all or applied incorrectly, causing the AppShell layout to break or look inconsistent across different viewport sizes.

### System Info

- @mantine/core version: 7.x
- Browser: Any

---
Repository: /testbed
