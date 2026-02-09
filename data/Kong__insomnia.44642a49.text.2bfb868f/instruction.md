# Bug Report

### Describe the bug
The `response.text()` method is returning an incorrect value. When calling `text()` on a response object with a body, it returns `"[object Object]"` instead of the actual body content as a string.

### Reproduction
```js
const response = {
  body: 'Hello World'
}

// Expected: 'Hello World'
// Actual: '[object Object]'
const text = response.text()
console.log(text)
```

### Expected behavior
The `text()` method should return the response body converted to a string. For example, if the body is `'Hello World'`, calling `text()` should return `'Hello World'`.

### System Info
- insomnia-sdk version: latest
- Using response.text() to get body content

---
Repository: /testbed
