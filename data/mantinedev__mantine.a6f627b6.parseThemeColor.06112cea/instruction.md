# Bug Report

### Describe the bug

I'm experiencing an issue with theme color parsing in MantineProvider. When I explicitly pass a color shade (like `blue.5`), it seems to be ignored and the component always uses the primary shade instead. Conversely, when I don't specify a shade, I'm getting `undefined` instead of the expected primary shade value.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// Case 1: Explicitly setting shade - gets ignored
<Button color="blue.5">
  Click me
</Button>
// Expected: Uses blue shade 5
// Actual: Uses the primary shade (e.g., shade 6 or 7)

// Case 2: Not setting shade - returns undefined
<Button color="blue">
  Click me
</Button>
// Expected: Uses the primary shade
// Actual: Color is undefined/broken
```

### Expected behavior

- When a specific shade is provided (e.g., `blue.5`), that exact shade should be used
- When no shade is provided (e.g., `blue`), the primary shade for the current color scheme should be used

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to have started happening recently. The color parsing logic appears to be inverted somehow.

---
Repository: /testbed
