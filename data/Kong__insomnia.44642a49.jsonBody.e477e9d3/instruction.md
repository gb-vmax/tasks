# Bug Report

### Describe the bug

I'm experiencing an issue with the `expect` response assertions in the SDK. When trying to use `expect.to.have.jsonBody()` with nested object comparisons, the assertion seems to fail even when the JSON body contains the expected data.

### Reproduction

```js
// Given a response with JSON body:
// { "user": { "id": 123, "name": "John", "email": "john@example.com" } }

// This assertion fails unexpectedly
pm.expect(response).to.have.jsonBody({
  user: {
    id: 123
  }
});
```

The assertion should pass since the response body does contain a `user` object with `id: 123`, but it seems like the current implementation requires an exact match of the entire JSON structure rather than allowing partial matching.

### Expected behavior

The `jsonBody()` assertion should support partial object matching, allowing me to verify only specific fields exist in the response without having to specify the entire JSON structure. This is especially useful when dealing with large response objects where I only care about a few specific fields.

Additionally, it would be helpful if the assertion could support JSONPath expressions for extracting and validating nested values, similar to how other testing frameworks handle JSON assertions.

### System Info
- insomnia-sdk version: latest
- Platform: Node.js

---
Repository: /testbed
