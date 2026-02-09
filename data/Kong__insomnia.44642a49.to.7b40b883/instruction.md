# Bug Report

### Describe the bug

I'm experiencing an issue with the response assertion methods in the SDK. When trying to use `insomnia.response.to.have.status()`, `insomnia.response.to.have.header()`, or `insomnia.response.to.have.body()`, I'm getting errors that these methods are not accessible or undefined.

### Reproduction

```js
// This used to work but now throws an error
insomnia.response.to.have.status(200);

// Same issue with other assertion methods
insomnia.response.to.have.header('Content-Type');
insomnia.response.to.have.body('expected body');
```

The error indicates that the `have` property or its methods are not defined on the `to` object.

### Expected behavior

The assertion methods should be accessible and work as before to verify response status codes, headers, and body content. The chain `insomnia.response.to.have.status(200)` should successfully validate that the response has a 200 status code.

### Additional context

This appears to have started happening recently. The response object itself seems fine, but the assertion chain is broken. Not sure if this is related to a recent change or if I'm missing something in my setup.

---
Repository: /testbed
