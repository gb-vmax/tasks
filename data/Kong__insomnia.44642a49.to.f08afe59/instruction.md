# Bug Report

### Describe the bug

I'm experiencing an issue where the response assertion methods are not working properly. When trying to use `insomnia.response.to.have.status()`, `insomnia.response.to.have.header()`, or `insomnia.response.to.have.body()` in my scripts, I get errors saying these methods are undefined or not accessible.

### Reproduction

```js
// This throws an error - methods are not available
insomnia.response.to.have.status(200);

// Same issue with other assertion methods
insomnia.response.to.have.header('Content-Type');
insomnia.response.to.have.body('expected response');
```

The `to` property seems to be accessible, but the nested `have` object and its methods (`status`, `header`, `body`, etc.) are not working as expected.

### Expected behavior

The assertion methods should be available and functional for validating response properties:
- `insomnia.response.to.have.status(200)` should verify the response status code
- `insomnia.response.to.have.header('header-name')` should check for header presence
- `insomnia.response.to.have.body('text')` should validate response body content

### System Info
- Insomnia SDK version: latest
- The issue appeared after a recent update

---
Repository: /testbed
