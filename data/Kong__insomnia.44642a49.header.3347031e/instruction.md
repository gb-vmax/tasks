# Bug Report

### Describe the bug
The `response.to.have.header()` method is not working correctly when checking for headers. After a recent update, the header verification seems to be broken and always fails even when the header is present in the response.

### Reproduction
```js
// Example response with headers
const response = {
  headers: {
    'Content-Type': 'application/json',
    'X-Custom-Header': 'some-value'
  }
}

// This check fails even though the header exists
pm.expect(response).to.have.header('Content-Type')

// This also doesn't work as expected
pm.expect(response).to.have.header('X-Custom-Header')
```

### Expected behavior
The `to.have.header()` assertion should pass when the specified header is present in the response, regardless of the case of the header name (since HTTP headers are case-insensitive).

### Additional context
This seems to have started happening in the latest version. The header checks were working fine before. Not sure if this is related to recent changes in the SDK or if I'm missing something.

---
Repository: /testbed
