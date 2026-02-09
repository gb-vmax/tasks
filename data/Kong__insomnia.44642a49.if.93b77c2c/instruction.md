# Bug Report

### Describe the bug

The `showSaveDialog` method in the app plugin context is broken after a recent change. When trying to save a file through the plugin API, the dialog doesn't appear and the function returns `null` immediately.

### Reproduction

```js
// Using the plugin API
const result = await context.app.showSaveDialog({
  defaultPath: '/path/to/file.json'
});

// result is always null, even when dialogs should be allowed
console.log(result); // null
```

### Expected behavior

The save dialog should open when `canShowDialogs` is true, allowing the user to select a file path. The function should return the selected file path or `null` if the user cancels.

### Additional context

It looks like there might be a syntax error or malformed code in the `showSaveDialog` implementation. The dialog options aren't being passed correctly to the native dialog, and there seems to be duplicate code that's preventing the actual dialog from showing.

---
Repository: /testbed
