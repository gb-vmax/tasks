# Bug Report

### Describe the bug

When using notifications with a custom position that isn't in the predefined positions array, the notification causes an error. The notification system seems to only work with positions that are explicitly defined upfront, but it should handle any position value gracefully.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// This works fine with default positions like 'top-right', 'bottom-left', etc.
notifications.show({
  title: 'Test',
  message: 'This works',
  position: 'top-right'
});

// But using a custom or undefined position causes issues
notifications.show({
  title: 'Test',
  message: 'This breaks',
  position: 'custom-position'
});
```

The notification with a custom position doesn't render properly and may cause the entire notification system to fail.

### Expected behavior

The notification system should handle any position value, even if it's not in the predefined positions list. Custom positions should either:
1. Work as expected and render in a custom location
2. Fall back to a default position gracefully

Currently it seems like the code expects all possible positions to be initialized beforehand, which limits flexibility.

### System Info
- @mantine/notifications version: latest
- React version: 18.x

---
Repository: /testbed
