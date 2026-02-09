# Bug Report

### Describe the bug

Notifications are not appearing in their specified positions. When I set a custom position for a notification (like `'top-right'` or `'bottom-left'`), it seems to be ignored and all notifications are being grouped into the same position instead.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// Try to show notifications in different positions
notifications.show({
  title: 'Notification 1',
  message: 'This should be top-right',
  position: 'top-right'
});

notifications.show({
  title: 'Notification 2', 
  message: 'This should be bottom-left',
  position: 'bottom-left'
});

// Both notifications appear in the same position (default position)
// instead of their specified positions
```

### Expected behavior

Each notification should appear in its specified position. The first notification should render at `top-right` and the second at `bottom-left`.

### System Info

- @mantine/notifications version: latest
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
