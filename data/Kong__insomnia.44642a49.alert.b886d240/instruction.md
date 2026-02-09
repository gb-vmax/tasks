# Bug Report

### Describe the bug

When using the plugin API's `app.alert()` method, alerts with titles that start with an exclamation mark (`!`) are having the exclamation mark stripped from the displayed title. This is causing unexpected behavior where alert titles don't match what was passed to the function.

### Reproduction

```js
// Using the plugin context API
context.app.alert('!Important Warning', 'This is a critical message');

// Expected: Alert shows with title "!Important Warning"
// Actual: Alert shows with title "Important Warning" (exclamation mark removed)
```

### Steps to reproduce:
1. Create a plugin that uses `context.app.alert()`
2. Call the alert method with a title starting with `!`
3. Observe that the alert displays without the leading exclamation mark

### Expected behavior

The alert should display the exact title string that was passed to the function, including any leading special characters like `!`. The exclamation mark should not be stripped from the title.

### System Info
- Insomnia version: latest
- OS: Any

This seems to have started recently. Not sure if this is related to any deduplication logic but the title modification is unexpected behavior for the API.

---
Repository: /testbed
