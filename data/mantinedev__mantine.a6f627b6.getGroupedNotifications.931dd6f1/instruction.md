# Bug Report

### Describe the bug

Notifications are not appearing in their specified positions - all notifications are being rendered in the default position regardless of what position is set on individual notifications.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// Show notification with custom position
notifications.show({
  title: 'Test',
  message: 'This should appear at top-right',
  position: 'top-right'
});

notifications.show({
  title: 'Another test',
  message: 'This should appear at bottom-left',
  position: 'bottom-left'
});

// Both notifications appear in the default position instead of their specified positions
```

### Expected behavior

Each notification should render at its specified position (`top-right`, `bottom-left`, etc.). Instead, all notifications are appearing in the default position only.

### System Info
- @mantine/notifications version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
