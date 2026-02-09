# Bug Report

### Describe the bug

The `Avatar` component with initials is not cycling through all available colors correctly. It seems like one of the colors in the color array is never being used when generating avatar colors based on user names.

### Reproduction

```js
import { Avatar } from '@mantine/core';

// Try creating avatars with different names
// You'll notice that one color from the default palette never appears
const names = [
  'Alice Anderson',
  'Bob Brown',
  'Charlie Clark',
  'David Davis',
  // ... many more names
];

// The last color in the default colors array is never selected
names.map(name => <Avatar name={name} color="initials">{name}</Avatar>)
```

### Expected behavior

All colors in the color array should be used with equal probability when generating initials colors. If there are N colors available, each color should have a 1/N chance of being selected for any given name.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
