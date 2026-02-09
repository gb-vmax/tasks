# Bug Report

### Describe the bug

I'm experiencing an issue with the notification auto-close behavior. When I set `autoClose={0}` on a notification, it's not respecting that value and instead behaves as if auto-close is disabled entirely. The notification stays open indefinitely even though I explicitly want it to close immediately (or with 0 delay).

### Reproduction

```jsx
import { notifications } from '@mantine/notifications';

// This notification should close immediately but stays open
notifications.show({
  title: 'Test',
  message: 'Should close immediately',
  autoClose: 0
});
```

### Expected behavior

When `autoClose` is set to `0`, the notification should close immediately (or with minimal delay). The value `0` is a valid number and should be treated differently from `false`. Currently, it seems like `0` is being treated as a falsy value and the notification doesn't auto-close at all.

### System Info
- @mantine/notifications version: latest
- Browser: Chrome

---
Repository: /testbed
