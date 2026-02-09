# Bug Report

### Describe the bug

I'm experiencing an issue with indent detection in my code. When I have source code that uses 2-space indentation, the indent string detection is not working correctly and seems to default to tabs instead of properly detecting the spaces.

### Reproduction

```js
const code = `
function test() {
  if (true) {
    console.log('hello');
  }
}
`;

// The indent detection returns '\t' instead of '  '
const indent = guessIndentString(code);
console.log(indent); // Expected: '  ', Actual: '\t'
```

### Expected behavior

When source code consistently uses 2-space indentation, the indent detection should return `'  '` (two spaces) rather than falling back to tabs.

### Additional context

This seems to have started happening recently. My codebase uses 2-space indentation throughout, but the detection is now incorrectly identifying it as tab-indented code. Files with 3+ space indentation seem to work fine, but 2-space indentation specifically is broken.

---
Repository: /testbed
