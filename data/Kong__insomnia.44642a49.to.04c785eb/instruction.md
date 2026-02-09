# Bug Report

### Describe the bug

The response validation methods are not working anymore. When trying to use `insomnia.response.to.have.status()`, `insomnia.response.to.have.header()`, or `insomnia.response.to.have.body()` in scripts, I'm getting errors that these properties/methods are undefined.

### Reproduction

```js
// This used to work but now throws an error
insomnia.response.to.have.status(200);

// Also fails
insomnia.response.to.have.header('Content-Type');

// Same issue
insomnia.response.to.have.body('expected response');
```

When running these, I get something like "Cannot read property 'have' of undefined" or similar errors indicating that the `to` property is not accessible.

### Expected behavior

The response assertion methods should work as before. The `to.have` chain should be available on the response object for validating status codes, headers, and body content.

### System Info
- Insomnia SDK version: latest
- Using pre-request/after-response scripts

---
Repository: /testbed
