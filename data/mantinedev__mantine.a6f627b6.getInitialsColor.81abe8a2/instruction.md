# Bug Report

### Describe the bug

The Avatar component's initials color selection is not working correctly. When using the same name multiple times, the color assignment seems inconsistent, and some colors from the provided color array never get used.

### Reproduction

```tsx
import { Avatar } from '@mantine/core';

// Using default colors
<Avatar name="John Doe">JD</Avatar>
<Avatar name="Jane Smith">JS</Avatar>
<Avatar name="Bob Wilson">BW</Avatar>

// The last color in the default colors array never appears
// Also, the same name sometimes produces different colors on re-render
```

### Expected behavior

- All colors in the color array should be available for selection
- The same name should consistently map to the same color
- Color distribution should be even across all available colors

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
