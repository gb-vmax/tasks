# Bug Report

### Describe the bug

The `text()` method on the Response object is not working correctly when the response body is stored in the `stream` property instead of the `body` property. The method only checks for `this.body` and returns an empty string when the data is in `this.stream`.

### Reproduction

```js
// Create a response with data in stream property
const response = new Response({
  stream: Buffer.from('Hello World', 'utf-8'),
  // no body property set
});

// This returns empty string instead of 'Hello World'
const text = response.text();
console.log(text); // Expected: 'Hello World', Actual: ''
```

### Expected behavior

The `text()` method should decode and return the text content from the `stream` property when `body` is not available. It should also respect the charset encoding specified in the response's content-type header.

### System Info

- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
