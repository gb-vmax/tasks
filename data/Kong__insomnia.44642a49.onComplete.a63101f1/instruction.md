# Bug Report

### Describe the bug

When using the plugin API to show a prompt dialog, the promise never resolves with the user's input value. After entering a value and clicking submit, the returned value is always an empty string instead of what was actually entered.

### Reproduction

```js
// In a plugin
const result = await context.app.prompt('Enter a value', {
  label: 'Value',
  defaultValue: 'test'
});

console.log(result); // Expected: user's input, Actual: empty string
```

### Steps to reproduce:
1. Create a plugin that uses `context.app.prompt()`
2. Show the prompt dialog
3. Enter some text in the input field
4. Click submit/OK
5. The promise resolves but with an empty string instead of the entered value

### Expected behavior

The prompt should return the value that the user entered in the dialog. If I type "hello world" and click submit, the promise should resolve with "hello world", not an empty string.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently, possibly after a recent update. The dialog shows up fine and accepts input, but the return value is always wrong.

---
Repository: /testbed
