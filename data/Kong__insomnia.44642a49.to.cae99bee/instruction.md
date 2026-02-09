# Bug Report

### Describe the bug

The response assertion API seems to be broken after a recent update. When trying to use `insomnia.response.to.have.status()` or other assertion methods in pre-request/test scripts, I'm getting errors that these properties/methods don't exist.

### Reproduction

```js
// In a test script
insomnia.response.to.have.status(200);
// Error: Cannot read property 'have' of undefined

// Same issue with other assertions
insomnia.response.to.have.header('Content-Type');
insomnia.response.to.have.body('expected body');
```

The `to` property appears to be undefined or not properly accessible, making it impossible to use any of the chained assertion methods.

### Expected behavior

The assertion chain should work as documented:
- `insomnia.response.to.have.status(200)` should verify the status code
- `insomnia.response.to.have.header('key')` should verify header existence
- `insomnia.response.to.have.body('text')` should verify body content
- `insomnia.response.to.not.have.status(404)` should support negation

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our ability to write proper test assertions. Any help would be appreciated!

---
Repository: /testbed
