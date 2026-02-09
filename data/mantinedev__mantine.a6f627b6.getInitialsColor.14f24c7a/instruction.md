# Bug Report

### Describe the bug

The `Avatar` component is not displaying the correct background color for initials. It seems like the color selection logic is broken - sometimes it returns `undefined` instead of a valid color from the color array, causing the avatar to not render properly or use a fallback color.

### Reproduction

```jsx
import { Avatar } from '@mantine/core';

// This should show an avatar with initials and a colored background
// but sometimes the color is undefined
<Avatar color="initials">John Doe</Avatar>

// Try with different names - some work, some don't
<Avatar color="initials">Alice Smith</Avatar>
<Avatar color="initials">Bob Johnson</Avatar>
```

When inspecting the component, the background color is sometimes missing entirely. It appears that the color selection is going out of bounds of the available colors array.

### Expected behavior

The avatar should always display with a valid color from the predefined color palette. Every name should map to one of the available colors consistently without returning undefined.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
