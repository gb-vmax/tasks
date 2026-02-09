# Bug Report

### Describe the bug
I'm encountering a syntax error when using the response assertion methods in the SDK. The code appears to have malformed object structure that's causing parsing issues.

### Reproduction
```js
const response = // ... get response object

// Trying to use the 'not' assertion methods
response.to.not.have.jsonBody({ key: 'value' })
```

When attempting to use any of the `response.to.not.have` assertion methods, the code fails to execute properly. It seems like there's a structural issue with how the assertion object is defined.

### Expected behavior
The `response.to.not.have` assertions should work correctly, allowing me to verify that the response does NOT contain certain properties. For example:
- `response.to.not.have.status(404)` - verify status is not 404
- `response.to.not.have.header('X-Custom')` - verify header doesn't exist
- `response.to.not.have.jsonBody({ error: true })` - verify JSON doesn't match

### Additional context
This appears to have broken recently. The positive assertions (`response.to.have.*`) seem to work fine, but the negative ones (`response.to.not.have.*`) are not functioning.

---
Repository: /testbed
