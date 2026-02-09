# Bug Report

### Describe the bug

When setting `autoClose={false}` on individual notifications, they still auto-close after the default timeout. The notification-level `autoClose` prop is being ignored when it's explicitly set to `false`.

### Reproduction

```jsx
import { notifications } from '@mantine/notifications';

// This notification should stay open indefinitely, but it auto-closes
notifications.show({
  title: 'Important',
  message: 'This should not auto-close',
  autoClose: false
});
```

Even when explicitly setting `autoClose={false}` on a specific notification, it closes automatically after the default timeout period instead of staying open.

### Expected behavior

When `autoClose` is set to `false` on an individual notification, that notification should remain open indefinitely and not auto-close, regardless of any global `autoClose` settings.

### System Info
- @mantine/notifications version: latest
- React version: 18.x

---
Repository: /testbed
