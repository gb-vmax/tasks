# Bug Report

### Describe the bug
After a recent update, the alert modal is showing unexpected behavior when multiple alerts are triggered in quick succession. The modal seems to be queueing alerts and showing them one after another, even after the user has dismissed them. This is causing alerts to appear that the user didn't explicitly trigger at that moment.

### Reproduction
```js
// Trigger multiple alerts quickly
alertModal.show({ title: 'Alert 1', message: 'First alert' });
alertModal.show({ title: 'Alert 2', message: 'Second alert' });
alertModal.show({ title: 'Alert 3', message: 'Third alert' });

// Expected: Only the last alert should be shown
// Actual: All three alerts are shown sequentially
```

### Steps to reproduce:
1. Open the application
2. Trigger multiple alert modals in quick succession (e.g., by clicking a button multiple times)
3. Dismiss the first alert
4. Notice that additional alerts continue to appear even though you only expected one

### Expected behavior
When multiple alerts are triggered quickly, only the most recent alert should be displayed. Previous alerts should be discarded or replaced by newer ones, not queued up to display sequentially.

The current behavior is particularly problematic when:
- Network errors trigger multiple alerts
- User rapidly clicks on actions that show confirmation dialogs
- Background processes generate multiple notifications

### Additional context
This seems to have started happening recently. Previously, calling `show()` multiple times would just update the current alert or show only the latest one.

---
Repository: /testbed
