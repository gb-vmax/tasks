# Bug Report

### Describe the bug

I'm experiencing an issue with error handling when processing markdown files. When an error occurs during transformation, the promise resolves successfully instead of rejecting. This makes it impossible to catch and handle errors properly in async/await code.

### Reproduction

```js
const processor = remark();

try {
  // Add a transformer that throws an error
  processor.use(() => {
    return (tree) => {
      throw new Error('Transform failed');
    };
  });
  
  const result = await processor.process('# Test');
  console.log('Success:', result); // This executes instead of catching the error
} catch (error) {
  console.log('Error caught:', error); // This never executes
}
```

### Expected behavior

When a transformer throws an error, the promise should reject and the error should be catchable in a try/catch block. Currently, the promise resolves even when errors occur, which breaks error handling flow.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
