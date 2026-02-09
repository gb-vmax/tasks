# Bug Report

### Describe the bug

I'm experiencing an issue with notification positioning where notifications are not being grouped correctly by their position. It seems like notifications are being placed in the wrong position groups, and some position groups are not being initialized properly.

### Reproduction

```js
import { notifications } from '@mantine/notifications';

// Show notifications with different positions
notifications.show({
  message: 'Top notification',
  position: 'top-right'
});

notifications.show({
  message: 'Bottom notification', 
  position: 'bottom-left'
});

// Notifications appear in unexpected positions
// Some position groups seem to be missing entirely
```

### Expected behavior

Notifications should be grouped and displayed according to their specified `position` property. All position groups should be properly initialized regardless of whether they contain notifications or not.

### System Info
- @mantine/notifications version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
