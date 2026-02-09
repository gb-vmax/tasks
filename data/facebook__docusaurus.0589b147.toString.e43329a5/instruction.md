# Bug Report

### Describe the bug

I'm encountering an issue with the VFile `toString()` method. When the file value is a string, it's being passed to `TextDecoder.decode()` which expects a buffer/typed array, not a string. This causes the method to fail or produce incorrect output.

### Reproduction

```js
const file = new VFile({ value: 'some text content' });
const result = file.toString();
// This should return 'some text content' but fails because 
// TextDecoder.decode() doesn't accept strings
```

### Expected behavior

When `value` is already a string, `toString()` should just return it directly without trying to decode it. The TextDecoder should only be used when the value is a buffer or typed array.

### Additional context

This seems like it might be a regression - the logic for handling string values appears to have been changed. Previously it would check if the value was already a string and return it immediately, but now it's trying to decode string values which doesn't make sense.

---
Repository: /testbed
