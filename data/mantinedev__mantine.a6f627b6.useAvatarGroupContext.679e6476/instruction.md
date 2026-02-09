# Bug Report

### Describe the bug

After a recent update, the `Avatar` component is not rendering correctly when used inside `AvatarGroup`. The avatars appear with incorrect spacing and styling, as if they're not detecting that they're within a group context.

### Reproduction

```jsx
import { Avatar, AvatarGroup } from '@mantine/core';

function Demo() {
  return (
    <AvatarGroup>
      <Avatar src="avatar1.png" />
      <Avatar src="avatar2.png" />
      <Avatar src="avatar3.png" />
    </AvatarGroup>
  );
}
```

### Expected behavior

The avatars should render with group-specific styles (overlapping, proper spacing, etc.) when placed inside `AvatarGroup`. Instead, they render as if they're standalone avatars.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
