# Bug Report

### Issue with Modal detection in date picker components

I'm experiencing an issue where the date picker modal appears to be incorrectly detected as closed when it's actually open. This is causing some unexpected behavior in my application where I need to verify whether the modal is displayed or not.

### Reproduction

When trying to check if the modal is closed after dismissing a date picker, the check seems to pass even when there's still a modal present in the DOM.

```js
// Open date picker modal
clickDateInput();

// Close modal
dismissModal();

// This check passes incorrectly when modal is still visible
expectNoModal(container);
```

### Expected behavior

When a modal is present in the DOM, the `expectNoModal` check should fail. Currently it seems like the logic for detecting whether a modal exists is not working correctly - it's checking for the wrong condition or element.

### System Info
- Package: @mantine/dates
- Using the date input test helpers

---
Repository: /testbed
