# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor where the output is being set incorrectly on the file object. When processing markdown content, the result seems to be assigned to the wrong property (`value` vs `result`) on the file object.

### Reproduction

```js
const processor = remark();

const file = processor.processSync('# Hello World');

// Expected: file.value should contain the compiled output
// Actual: file.result contains the output instead (or vice versa)
console.log(file.value); // undefined or wrong value
console.log(file.result); // contains what should be in file.value
```

### Expected behavior

The processor should correctly determine whether the compile result is a value-like output and assign it to `file.value`, or assign it to `file.result` if it's not a value. The current behavior seems to be inverted - value-like results are going to `file.result` and non-value results are going to `file.value`.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
