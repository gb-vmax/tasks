# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.prompt()` method is completely broken. When trying to call `app.prompt()` from a plugin, the application crashes or behaves unexpectedly. It looks like there's a syntax error or structural issue in the prompt implementation.

### Reproduction

```js
// In a plugin context
module.exports.requestHooks = [
  context => {
    context.app.prompt('Enter value', {
      defaultValue: 'test',
      timeout: 5000
    });
  }
];
```

When this code executes, the prompt doesn't appear and the plugin fails to work properly.

### Expected behavior

The prompt dialog should appear and allow the user to enter a value. If a timeout is specified, it should close automatically after that duration and reject with a timeout error message.

### Additional context

This seems to have broken recently. The code structure looks malformed - there appears to be duplicate or misplaced code blocks in the prompt implementation. The `onHide` callback and `prompt` function definition seem to be in the wrong places or duplicated.

---
Repository: /testbed
