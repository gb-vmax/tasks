# Bug Report

### Describe the bug

Media queries are being applied in the wrong order when using responsive style props. It seems like the breakpoints are sorted in reverse (largest to smallest) instead of smallest to largest, which causes styles for larger breakpoints to be overridden by smaller ones. Additionally, one of the media queries appears to be missing from the output.

### Reproduction

```tsx
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

When inspecting the generated CSS, the media queries are in the wrong order and the base breakpoint is missing. This causes the padding to not be applied correctly at different screen sizes - larger breakpoint styles get overridden by smaller ones.

### Expected behavior

Media queries should be sorted from smallest to largest breakpoint so that larger breakpoints properly override smaller ones. All defined breakpoints (including base) should be included in the output.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
