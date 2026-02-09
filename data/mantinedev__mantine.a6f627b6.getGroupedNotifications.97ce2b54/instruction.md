# Bug Report

### Describe the bug

Notifications are not appearing in their specified positions. All notifications are being rendered in the default position regardless of the `position` property set on individual notifications.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// Try to show notification in top-right
notifications.show({
  title: 'Test notification',
  message: 'This should appear in top-right',
  position: 'top-right'
});

// Try to show notification in bottom-left
notifications.show({
  title: 'Another notification',
  message: 'This should appear in bottom-left',
  position: 'bottom-left'
});
```

### Expected behavior

Each notification should render in its specified position (top-right, bottom-left, etc.). Instead, all notifications are appearing in the default position only.

### System Info

- @mantine/notifications version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
