# Bug Report

### Describe the bug

When passing inline styles to Box components, the styles are being overridden by theme defaults instead of taking precedence. This breaks the expected behavior where inline styles should have higher priority.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box style={{ color: 'red' }}>
      This text should be red
    </Box>
  );
}
```

If the theme has a default color set, it will override the inline `color: 'red'` style instead of the other way around.

### Expected behavior

Inline styles passed via the `style` prop should take precedence over theme defaults. The text in the example above should appear red regardless of theme settings.

### Additional context

This seems to have started happening recently. Previously inline styles would correctly override theme values. Also noticing that CSS variables defined via the `vars` prop are no longer being applied at all.

---
Repository: /testbed
