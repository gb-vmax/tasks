# Bug Report

### Describe the bug

Media queries with specific formatting are not being parsed correctly. When using responsive style props with certain media query formats, the styles may not be applied in the correct order or at all.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      style={{
        '@media (min-width: 768em)': {
          padding: '20px'
        }
      }}
    >
      Content
    </Box>
  );
}
```

When the media query string contains a space after the colon in `(min-width: `, the parsing doesn't work as expected. This affects responsive breakpoints and can cause styles to be applied incorrectly or not sorted properly.

### Expected behavior

Media queries should be parsed and sorted correctly regardless of whether there's a space after the colon in the min-width declaration. Both `(min-width: 768em)` and `(min-width:768em)` formats should work.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
