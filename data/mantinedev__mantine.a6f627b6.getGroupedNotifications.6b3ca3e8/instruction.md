# Bug Report

### Describe the bug

When using notifications with custom positions, all notifications are being grouped under the default position instead of respecting their individual `position` property. This causes all notifications to appear in the same location on screen regardless of what position was specified.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// Show notification with custom position
notifications.show({
  title: 'Top notification',
  message: 'This should appear at top-right',
  position: 'top-right'
});

notifications.show({
  title: 'Bottom notification', 
  message: 'This should appear at bottom-left',
  position: 'bottom-left'
});

// Both notifications appear at the default position instead of their specified positions
```

### Expected behavior

Each notification should appear at its specified position. Notifications with `position: 'top-right'` should display in the top-right corner, notifications with `position: 'bottom-left'` should display in the bottom-left corner, etc.

Currently all notifications are appearing at the default position regardless of the `position` property being set.

### System Info

- @mantine/notifications version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
