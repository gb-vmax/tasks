# Bug Report

### Describe the bug

When using theme radius values (like `'sm'`, `'md'`, `'lg'`) with the `radius` prop, the component doesn't apply the correct CSS variable. Instead, it seems to be converting the theme key to a rem value rather than using the theme's predefined radius values.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should use var(--mantine-radius-md) but doesn't work correctly
<Box radius="md" style={{ border: '1px solid red' }}>
  Content
</Box>

// Theme radius values like 'sm', 'lg', 'xl' also affected
<Box radius="sm">Small radius</Box>
<Box radius="lg">Large radius</Box>
```

### Expected behavior

When passing a theme radius key (e.g., `'md'`, `'sm'`, `'lg'`), the component should apply the corresponding CSS variable like `var(--mantine-radius-md)`. The theme values should take precedence over treating the string as a direct rem conversion.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
