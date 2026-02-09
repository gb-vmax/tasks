# Bug Report

### Describe the bug

The `getBytesRead()` method in the response context is returning incorrect values or causing unexpected behavior. After a recent update, calling this method seems to be modifying the response object in ways that weren't happening before.

### Reproduction

```js
const response = {
  bytesRead: 1024,
  bytesContent: 512
};

// Call getBytesRead multiple times
const bytes1 = response.getBytesRead();
const bytes2 = response.getBytesRead();

// Response object now has unexpected _metadata property
console.log(response._metadata); // Shouldn't exist
```

### Expected behavior

The `getBytesRead()` method should simply return the number of bytes read without side effects. It shouldn't be adding new properties to the response object or performing calculations that aren't related to just reading the byte count.

### Additional context

This appears to have started after a change to the response context plugin. The method used to just return `response.bytesRead || 0` but now it's doing a lot more than that. Not sure why metadata tracking and compression ratio calculations are being added to what should be a simple getter method.

---
Repository: /testbed
