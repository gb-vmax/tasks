# Bug Report

### Describe the bug

Media queries are not being sorted correctly, causing styles to be applied in the wrong order. After some investigation, it seems like the media query parsing is broken - it's removing the opening parenthesis from all media queries instead of just the `min-width:` part.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      style={{
        '@media (min-width: 768px)': { color: 'blue' },
        '@media (min-width: 1024px)': { color: 'red' }
      }}
    >
      Content
    </Box>
  );
}
```

When the component renders, the media queries get parsed incorrectly. The sorting logic is supposed to extract the pixel value from queries like `(min-width: 768px)` but it's stripping out the wrong part of the string.

### Expected behavior

Media queries should be sorted by their breakpoint values in ascending order, so smaller breakpoints apply first and larger breakpoints can override them. The parsing should correctly extract `768` from `(min-width: 768px)` and `1024` from `(min-width: 1024px)`.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
