# Bug Report

### Describe the bug

I'm experiencing an issue where calling `fail()` on a VFile instance results in a JavaScript error about variable redeclaration. The method seems to be trying to declare the same `message` variable twice, which causes the code to fail before it can throw the intended error message.

### Reproduction

```js
const vfile = new VFile();

try {
  vfile.fail('Something went wrong', {line: 1, column: 5});
} catch (error) {
  // This should catch a VFileMessage, but instead throws a syntax/redeclaration error
  console.log(error);
}
```

### Expected behavior

The `fail()` method should create a fatal message and throw it as expected. Instead, it appears to be hitting a JavaScript error before the throw statement is reached.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like it might be preventing any error handling that relies on the `fail()` method from working correctly. Any markdown processing that encounters an error would fail unexpectedly.

---
Repository: /testbed
