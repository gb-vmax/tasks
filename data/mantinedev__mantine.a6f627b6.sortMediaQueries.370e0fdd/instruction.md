# Bug Report

### Describe the bug
Media queries are not being applied in the correct order when using responsive style props. The styles seem to be sorted incorrectly, causing larger breakpoints to be overridden by smaller ones instead of the expected mobile-first approach.

### Reproduction
```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      p={{ base: '10px', sm: '20px', md: '30px', lg: '40px' }}
    >
      Content
    </Box>
  );
}
```

When inspecting the generated CSS, the media queries appear in the wrong order. The larger breakpoint styles are being overridden by smaller breakpoint styles, which is the opposite of what should happen.

### Expected behavior
Media queries should be sorted by their breakpoint values in ascending order (smallest to largest), so that larger breakpoints can properly override smaller ones following a mobile-first approach.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
