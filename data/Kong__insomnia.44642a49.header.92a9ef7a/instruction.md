# Bug Report

### Describe the bug

When trying to use `pm.response.to.have.header()` with an object containing both `key` and `value` properties to verify a specific header value, the function doesn't work as expected. The code appears to have a syntax error or incorrect structure that prevents it from executing properly.

### Reproduction

```js
pm.test("Check header with specific value", function () {
    pm.response.to.have.header({
        key: 'Content-Type',
        value: 'application/json'
    });
});
```

When running this test, the assertion fails to execute correctly. It seems like the new functionality for checking header values was added but the code structure is broken.

### Expected behavior

The test should be able to check both the presence of a header and verify its value when passing an object with `key` and `value` properties. Alternatively, passing just a string should continue to work for checking header presence only.

```js
// This should work - checking header exists
pm.response.to.have.header('Content-Type');

// This should also work - checking header with specific value
pm.response.to.have.header({
    key: 'Content-Type',
    value: 'application/json'
});
```

### System Info
- Using the latest version of insomnia-sdk
- The issue appeared after a recent update

---
Repository: /testbed
