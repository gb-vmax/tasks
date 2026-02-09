# Bug Report

### Describe the bug

I'm experiencing an issue with the notification auto-close behavior. When I set `autoClose={false}` on a notification, it still closes automatically instead of staying open indefinitely.

### Reproduction

```jsx
import { notifications } from '@mantine/notifications';

// This notification closes automatically even though autoClose is false
notifications.show({
  title: 'Test notification',
  message: 'This should stay open',
  autoClose: false
});
```

### Expected behavior

When `autoClose={false}` is passed to a notification, it should remain open until manually dismissed by the user. The notification should not automatically close after any timeout period.

### System Info
- @mantine/notifications version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
