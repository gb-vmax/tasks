# Bug Report

### Describe the bug

The `getStatusMessage()` function is returning unexpected values when a response doesn't have an explicit status message. Instead of returning just the status message (or empty string), it's now returning a formatted string like "404 Not Found" which breaks existing functionality that depends on the original behavior.

### Reproduction

```js
// When making a request that returns a response without an explicit statusMessage
const response = {
  statusCode: 404,
  statusMessage: undefined  // or not set
}

// Previously this would return ''
// Now it returns '404 Not Found'
const message = context.response.getStatusMessage()
console.log(message) // Outputs: "404 Not Found" instead of ""
```

### Expected behavior

The `getStatusMessage()` function should return the actual status message from the response object, or an empty string if no status message is present. It should not be constructing a formatted string with the status code included.

If I need the formatted version with status code, I would call `getStatusCode()` separately and format it myself.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
