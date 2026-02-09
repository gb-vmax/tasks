# Bug Report

### Describe the bug

The Avatar component's initials color generation is producing inconsistent results. When using the same name/string for multiple Avatar components, they sometimes render with different colors than expected. The color assignment seems to have changed and is no longer deterministic for the same input strings.

### Reproduction

```jsx
import { Avatar } from '@mantine/core';

function Demo() {
  return (
    <>
      <Avatar color="initials">John Doe</Avatar>
      <Avatar color="initials">John Doe</Avatar>
      {/* Both avatars should have the same color, but behavior is inconsistent */}
    </>
  );
}
```

Also noticed that avatars with similar names now produce very different colors compared to before:

```jsx
<Avatar color="initials">Alice Smith</Avatar>
<Avatar color="initials">Alice Jones</Avatar>
{/* Color distribution seems off */}
```

### Expected behavior

Avatars with the same initials/name should always render with the same color. The color assignment should be consistent and deterministic based on the input string.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
