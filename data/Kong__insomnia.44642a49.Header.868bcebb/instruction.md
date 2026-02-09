# Bug Report

### Describe the bug
When creating headers with certain key names or values containing whitespace, the header normalization is causing issues. Header keys are being unexpectedly modified (capitalization changes) and header values with multiple spaces or tabs are being collapsed, which breaks compatibility with existing code that expects the original formatting.

### Reproduction
```js
const header1 = new Header({
  key: 'content-type',
  value: 'application/json'
});
console.log(header1.key); // Expected: 'content-type', but getting 'Content-Type'

const header2 = new Header({
  key: 'X-CUSTOM-HEADER',
  value: 'some  value  with    spaces'
});
console.log(header2.value); // Expected: 'some  value  with    spaces', but spaces are collapsed
```

### Expected behavior
Header keys and values should be preserved as-is when passed to the constructor. The original casing and whitespace formatting should not be modified automatically, as this can break APIs that expect specific header formats.

### Additional context
This appears to have started happening recently. Our integration tests are failing because headers are no longer matching the expected format. Some APIs we work with are case-sensitive for custom headers, and the automatic normalization is causing requests to fail.

---
Repository: /testbed
