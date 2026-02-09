# Bug Report

### Describe the bug

I'm experiencing an issue with the `vfile` function where it's not creating VFile objects correctly. When I pass in a value that should be converted to a VFile, it's being returned as-is instead. Conversely, when I pass in something that's already a VFile, it's being wrapped again.

### Reproduction

```js
// Case 1: Passing a plain object/string
const result1 = vfile('some content');
// Expected: VFile object
// Actual: Returns the string 'some content' directly

// Case 2: Passing an existing VFile
const existingVFile = new VFile('content');
const result2 = vfile(existingVFile);
// Expected: Returns the same VFile object
// Actual: Wraps it in another VFile
```

### Expected behavior

The `vfile` function should:
- Create a new VFile when given a non-VFile value
- Return the value as-is when it's already a VFile

### System Info
- remark version: 15.0.1

This seems like the logic is inverted somewhere. The function is doing the opposite of what it should be doing.

---
Repository: /testbed
