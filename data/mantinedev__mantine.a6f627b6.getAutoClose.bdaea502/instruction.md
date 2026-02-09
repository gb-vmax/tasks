# Bug Report

### Describe the bug

The `autoClose` prop behavior for notifications seems broken. When I set `autoClose={false}` on a specific notification, it still auto-closes if the global `notificationAutoClose` is set to a number value. The notification-level prop should override the global setting but it's being ignored.

### Reproduction

```jsx
import { notifications } from '@mantine/notifications';

// Set global autoClose
notifications.show({
  title: 'Test',
  message: 'This should not auto-close',
  autoClose: false, // Explicitly disabled
});
```

With a global `notificationAutoClose` configured (e.g., 5000ms), the notification still closes automatically even though I explicitly set `autoClose={false}` on the individual notification.

### Expected behavior

When `autoClose={false}` is set on a notification, it should stay open indefinitely regardless of the global `notificationAutoClose` setting. The notification-level prop should take precedence over the global configuration.

### System Info
- @mantine/notifications version: latest
- React version: 18.x

---
Repository: /testbed
