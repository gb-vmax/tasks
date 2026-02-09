# Bug Report

### Describe the bug

The Avatar component's initials color selection is returning `undefined` for certain names. When displaying avatars with initials, some names result in no background color being applied, causing the avatar to appear broken or use a fallback style.

### Reproduction

```js
import { Avatar } from '@mantine/core';

// This returns undefined for the color
<Avatar name="John Doe" color="initials">JD</Avatar>

// Testing the underlying function directly:
const colors = ['blue', 'red', 'green', 'yellow'];
const color = getInitialsColor('John Doe', colors);
console.log(color); // Expected: one of the colors, Actual: undefined
```

### Expected behavior

The `getInitialsColor` function should always return a valid color from the provided color array. Every name should map to one of the available colors consistently.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
