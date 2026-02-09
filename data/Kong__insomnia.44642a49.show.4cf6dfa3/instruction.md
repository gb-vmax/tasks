# Bug Report

### Describe the bug

I'm experiencing an issue with the error modal where it's not displaying when I try to show it. The modal seems to be completely broken after a recent update - calling `show()` on the error modal doesn't do anything at all.

### Reproduction

```js
// Try to show an error modal
errorModalRef.current?.show({
  title: 'Error',
  message: 'Something went wrong'
});

// Modal doesn't appear
```

The modal worked fine before but now it just doesn't show up. I've tried different error messages and titles but nothing displays.

### Expected behavior

The error modal should appear on screen when `show()` is called with the error details.

### Additional context

This seems to have started happening recently. I noticed that if I wait a few seconds and try again, sometimes it works, but it's very inconsistent. Not sure what changed but this is blocking our error handling flow.

---
Repository: /testbed
