# Bug Report

### Describe the bug

The `autoClose` property for notifications is not working correctly when passing a number value. When I set `notificationAutoClose` to a specific duration (e.g., 5000ms), the notification doesn't auto-close at all or behaves unexpectedly.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// This doesn't work as expected
notifications.show({
  title: 'Test notification',
  message: 'This should auto-close after 5 seconds',
  autoClose: 5000
});
```

When I pass a number for `autoClose`, the notification should close after that many milliseconds, but instead it seems to ignore the value completely.

### Expected behavior

The notification should automatically close after the specified duration in milliseconds when `autoClose` is set to a number value.

### System Info
- @mantine/notifications version: latest
- Browser: Chrome 120

---
Repository: /testbed
