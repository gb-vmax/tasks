# Bug Report

### Describe the bug

When trying to generate test code, nothing is being output even when valid test objects are provided. The test generation appears to be completely broken - no test lines are generated regardless of the input.

### Reproduction

```js
const test = {
  name: 'My Test',
  code: 'expect(response.status).to.equal(200)'
};

// Try to generate test lines
const result = generateTestLines(1, test);

// Result is an empty array when it should contain test code
console.log(result); // []
```

### Expected behavior

When a valid test object is passed to `generateTestLines()`, it should return an array containing the generated test code lines. Currently it returns an empty array even when the test object is properly defined.

This seems to have broken test generation completely - any workflow that relies on generating tests from test objects will fail silently.

### System Info
- insomnia-testing version: latest
- Node version: 18.x

---
Repository: /testbed
