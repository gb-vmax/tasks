# Bug Report

### Describe the bug

When using the app context's prompt functionality in plugins, the promise rejection is happening even after the user submits the prompt with a value. The prompt should resolve successfully when the user provides input and clicks submit, but instead it's rejecting with a cancellation error.

### Reproduction

```js
// In a plugin
const result = await context.app.prompt('Enter a value', {
  defaultValue: 'test'
});

// User enters a value and clicks submit
// Expected: result should contain the submitted value
// Actual: Promise is rejected with "Prompt Enter a value cancelled"
```

### Steps to reproduce
1. Create a plugin that uses `context.app.prompt()`
2. Show a prompt to the user
3. Enter a value in the prompt
4. Click the submit button
5. The promise rejects instead of resolving with the submitted value

### Expected behavior

When a user successfully submits a prompt with a value, the promise should resolve with that value. The rejection should only occur when the user explicitly cancels or closes the prompt without submitting.

Currently it seems like the promise is being rejected even in the success case, which makes it impossible to retrieve the user's input.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
