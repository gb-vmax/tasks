# Bug Report

### Describe the bug

The `insomnia.response.to` property is not working anymore. When trying to access any of the assertion methods like `insomnia.response.to.have.status()`, `insomnia.response.to.have.header()`, or `insomnia.response.to.have.body()`, they are undefined and the script fails.

### Reproduction

```js
// This used to work but now throws an error
insomnia.response.to.have.status(200);
// TypeError: Cannot read property 'status' of undefined

// Same issue with other assertions
insomnia.response.to.have.header('Content-Type');
// TypeError: Cannot read property 'header' of undefined

insomnia.response.to.have.body('expected text');
// TypeError: Cannot read property 'body' of undefined
```

### Expected behavior

The `to.have` assertion chain should be accessible and work as before. Scripts should be able to verify response status codes, headers, and body content using the fluent assertion syntax.

### System Info
- Insomnia SDK version: latest
- Platform: All platforms

This seems to have broken recently. The `to` getter appears to be incomplete or not returning the proper object structure anymore.

---
Repository: /testbed
