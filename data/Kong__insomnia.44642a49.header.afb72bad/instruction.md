# Bug Report

### Describe the bug

The `response.to.not.have.header()` assertion is not working properly. When trying to assert that a response does NOT have a specific header, the test fails even though the header is not present in the response.

### Reproduction

```js
// This should pass but fails
pm.test("Response should not have X-Custom-Header", function () {
    pm.response.to.not.have.header('X-Custom-Header');
});

// Also fails with object syntax
pm.test("Response should not have header matching pattern", function () {
    pm.response.to.not.have.header({
        name: 'X-Custom-Header',
        value: 'some-value'
    });
});
```

### Expected behavior

The assertion should pass when the specified header is not present in the response. The `not.have.header()` check should work correctly for both string and object parameter formats.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
