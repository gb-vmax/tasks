# Bug Report

### Describe the bug

The `Avatar` component's initials color selection seems to be inconsistent. When passing a name to generate avatar initials, the color assignment doesn't properly distribute across all available colors in the palette. Some colors appear to never be used, while others are used more frequently than expected.

### Reproduction

```tsx
import { Avatar } from '@mantine/core';

// Create avatars with different names
<Avatar name="Alice" color="initials" />
<Avatar name="Bob" color="initials" />
<Avatar name="Charlie" color="initials" />
// ... more names

// The last color in the default color array never gets assigned
// Color distribution is uneven across the available colors
```

### Expected behavior

All colors in the default color palette (or custom color array) should have an equal chance of being selected based on the name hash. The color selection should evenly distribute across the entire range of available colors.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
