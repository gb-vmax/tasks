# Bug Report

### Describe the bug

The `app.alert()` plugin API method is showing the wrong content in alert dialogs. The title and message parameters appear to be swapped - what I pass as the title shows up as the message and vice versa.

### Reproduction

```js
// In a plugin
context.app.alert('Error Title', 'This is the error message');
```

**What happens:**
- Dialog title shows: "This is the error message"
- Dialog message shows: "Error Title"

**Expected:**
- Dialog title should show: "Error Title"
- Dialog message should show: "This is the error message"

### Additional context

Also noticed that the alert doesn't show at all in some contexts where it should be visible. It seems like the condition for showing dialogs might be inverted - alerts are being suppressed when they should display and might be attempting to display when they shouldn't.

This is breaking several plugins that rely on showing alerts to users for errors and notifications.

---
Repository: /testbed
