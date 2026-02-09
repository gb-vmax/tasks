# Bug Report

### Describe the bug

The `Avatar` component is not rendering correctly when used inside an `AvatarGroup`. The avatars are behaving as if they're not part of a group even when they're clearly wrapped in an `AvatarGroup` component.

### Reproduction

```jsx
import { Avatar, AvatarGroup } from '@mantine/core';

function MyComponent() {
  return (
    <AvatarGroup>
      <Avatar src="user1.jpg" />
      <Avatar src="user2.jpg" />
      <Avatar src="user3.jpg" />
    </AvatarGroup>
  );
}
```

### Expected behavior

When `Avatar` components are placed inside an `AvatarGroup`, they should:
- Apply group-specific styling (overlapping, borders, etc.)
- Recognize that they are within a group context
- Render with the proper spacing and layout

Instead, the avatars render as if they are standalone components, ignoring the group context entirely.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
