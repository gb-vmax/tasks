# Bug Report

### Describe the bug

Media queries are not being sorted correctly when using responsive style props. The sorting logic appears to be broken, causing styles to be applied in the wrong order. This affects the responsive behavior of components when using breakpoint-based props.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      p={{ base: 'xs', sm: 'md', lg: 'xl' }}
      bg={{ base: 'red', md: 'blue' }}
    >
      Content
    </Box>
  );
}
```

When inspecting the generated CSS, the media queries are not in the expected order. Styles that should apply at larger breakpoints are being overridden by smaller breakpoint styles.

### Expected behavior

Media queries should be sorted by their min-width values in ascending order so that larger breakpoints correctly override smaller ones. The CSS output should have media queries ordered from smallest to largest breakpoint.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: macOS

---
Repository: /testbed
