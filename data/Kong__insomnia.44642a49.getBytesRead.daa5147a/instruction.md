# Bug Report

### Describe the bug
The `getBytesRead()` method in the response context is returning incorrect values. When a response has 0 bytes read, it returns -1 instead of 0. Additionally, for any non-zero bytesRead value, the method always returns 0.

### Reproduction
```js
// Case 1: Response with 0 bytes read
const response1 = { bytesRead: 0 };
const context1 = init(response1);
console.log(context1.getBytesRead()); // Returns -1, expected 0

// Case 2: Response with actual bytes read
const response2 = { bytesRead: 1024 };
const context2 = init(response2);
console.log(context2.getBytesRead()); // Returns 0, expected 1024

// Case 3: Response with no bytesRead property
const response3 = {};
const context3 = init(response3);
console.log(context3.getBytesRead()); // Returns 0, which is correct
```

### Expected behavior
- When `bytesRead` is 0, the method should return 0 (not -1)
- When `bytesRead` has a value like 1024, the method should return 1024 (not 0)
- When `bytesRead` is undefined, the method should return 0 (current behavior is correct)

This seems to have broken recently and is affecting plugin scripts that rely on getting the actual number of bytes read from responses.

---
Repository: /testbed
