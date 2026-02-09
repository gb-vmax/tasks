# Bug Report

### Describe the bug
When using `response.to.have.body()` in the SDK, I'm getting a syntax error. It looks like the response body assertion code got corrupted somehow - there's a function definition appearing in the middle of the object literal which breaks the JavaScript syntax.

### Reproduction
```js
const response = await insomnia.send(request);

// This throws a syntax error
response.to.have.body('expected content');
```

### Expected behavior
The `response.to.have.body()` method should work correctly to assert response body content without throwing syntax errors.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This seems to have broken recently. The code structure looks malformed in the response.ts file where the `have` object is defined.

---
Repository: /testbed
