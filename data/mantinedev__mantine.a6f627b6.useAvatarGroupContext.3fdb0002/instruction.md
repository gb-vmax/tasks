# Bug Report

### Describe the bug

When using `Avatar` components inside an `AvatarGroup`, the avatars are not rendering with the proper group styling. It appears that avatars within a group are being treated as standalone avatars, losing the overlap effect and other group-specific styles.

### Reproduction

```tsx
import { Avatar, AvatarGroup } from '@mantine/core';

function Demo() {
  return (
    <AvatarGroup>
      <Avatar src="image1.png" />
      <Avatar src="image2.png" />
      <Avatar src="image3.png" />
    </AvatarGroup>
  );
}
```

### Expected behavior

Avatars inside `AvatarGroup` should:
- Overlap each other slightly
- Apply group-specific spacing
- Recognize they are within a group context

Instead, they render as if they were standalone `Avatar` components with no group styling applied.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
