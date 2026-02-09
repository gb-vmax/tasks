# Bug Report

### Describe the bug

The plugin alert system is not working correctly after a recent update. When trying to show alerts from plugins, they either don't appear at all or behave unexpectedly. It seems like there's an issue with how alerts are being queued and displayed.

### Reproduction

```js
// In a plugin context
app.alert('Test Alert', 'This is a test message');
app.alert('Another Alert', 'This should show after the first one');
```

When calling `app.alert()` multiple times in quick succession, the behavior is broken. Sometimes alerts don't show up, and sometimes they get stuck.

### Expected behavior

Each alert should be displayed properly, one after another if multiple alerts are triggered. The promise returned by `app.alert()` should resolve when the user dismisses the alert.

### Additional context

This appears to have started happening recently. The alert functionality was working fine before. When testing with plugins that use `app.alert()`, the alerts either:
1. Don't show at all
2. Show but never resolve their promises
3. Get stuck in some kind of queue that never processes

This is blocking plugin development since we can't reliably show alerts to users anymore.

---
Repository: /testbed
