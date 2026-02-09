# Bug Report

### Describe the bug

The contrast color calculation seems to be inverted - light colors are getting white text and dark colors are getting black text, which makes the text unreadable. This is affecting buttons, badges, and other components that use the `getContrastColor` function.

### Reproduction

```tsx
import { Button, MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <MantineProvider theme={{ autoContrast: true }}>
      {/* Light background should have dark text, but gets white text instead */}
      <Button color="yellow">Click me</Button>
      
      {/* Dark background should have light text, but gets dark text instead */}
      <Button color="blue">Click me</Button>
    </MantineProvider>
  );
}
```

### Expected behavior

- Light backgrounds (like yellow, lime, cyan) should have **black** text for readability
- Dark backgrounds (like blue, violet, grape) should have **white** text for readability

Currently it's doing the opposite - light backgrounds get white text (invisible) and dark backgrounds get black text (also hard to read).

### Additional context

This is happening when `autoContrast` is enabled in the theme. The contrast colors appear to be swapped compared to what they should be.

---
Repository: /testbed
