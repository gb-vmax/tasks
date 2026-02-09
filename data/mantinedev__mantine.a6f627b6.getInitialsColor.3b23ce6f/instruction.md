# Bug Report

### Describe the bug

The Avatar component's initials color selection is returning `undefined` in some cases. When generating avatar colors based on user names, occasionally the background color doesn't render at all, leaving the avatar without a proper background.

### Reproduction

```js
import { Avatar } from '@mantine/core';

// Sometimes returns undefined color
<Avatar name="John Doe" color="initials">JD</Avatar>

// The color array has specific length but the hash calculation
// can produce an index that's out of bounds
```

I noticed this happening randomly with different user names. Some names work fine and get a proper color assigned, but others result in no background color being applied to the avatar.

### Expected behavior

Every avatar with initials should receive a valid color from the color array. The hash-based color selection should always return a valid color index within the bounds of the available colors array.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
