# Bug Report

### Describe the bug

After a recent update, the plugin `app.alert()` function seems to be hanging indefinitely when called multiple times in quick succession. The first alert shows up fine, but subsequent alerts never appear and the promises never resolve.

### Reproduction

```js
// Call alert multiple times quickly
await app.alert('First alert', 'This one shows up');
await app.alert('Second alert', 'This one never appears');
await app.alert('Third alert', 'This one also never appears');

console.log('This line is never reached');
```

The first alert displays correctly, but after dismissing it, the second and third alerts don't show up. The code execution appears to be blocked waiting for the promise to resolve.

### Expected behavior

Each alert should display in sequence. When one alert is dismissed, the next one should appear immediately. All promises should eventually resolve so code execution can continue.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our plugin from working properly since we rely on showing multiple alerts to users during certain workflows. Any help would be appreciated!

---
Repository: /testbed
