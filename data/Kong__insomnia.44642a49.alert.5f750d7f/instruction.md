# Bug Report

### Describe the bug

After a recent update, the `app.alert()` function in plugins is not working correctly. When calling `alert()` with a title and message, the function seems to hang or not display the alert at all. This is breaking plugin functionality that relies on showing alerts to users.

### Reproduction

```js
// In a plugin context
app.alert('Test Alert', 'This is a test message');
// Alert doesn't show up or the function never resolves
```

Also noticed that if you try to show multiple alerts in quick succession, only some of them appear:

```js
app.alert('First Alert', 'Message 1');
app.alert('Second Alert', 'Message 2');
app.alert('Third Alert', 'Message 3');
// Sometimes only the first one shows, or none at all
```

### Expected behavior

The alert should display immediately with the provided title and message. Multiple alerts should all be shown to the user in sequence.

### Additional context

This was working fine before the recent changes. Not sure if this is related to the new alert severity handling or the queueing mechanism, but something is definitely broken with the basic alert functionality.

---
Repository: /testbed
