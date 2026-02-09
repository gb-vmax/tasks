# Bug Report

### Describe the bug

When using `expect(response).to.not.have.header()` in test scripts, the assertion doesn't work as expected. The negated assertion always passes regardless of whether the header actually exists or not.

### Reproduction

```js
// Given a response with a 'Content-Type' header
pm.test("negated header assertion", function() {
    // This should fail but passes incorrectly
    pm.expect(pm.response).to.not.have.header('Content-Type');
});
```

### Expected behavior

When using `.not.have.header()`, the assertion should fail if the header is present in the response. Currently it seems like the negation isn't being respected and the assertion always passes.

### System Info
- Insomnia SDK
- Using response object assertions

---
Repository: /testbed
