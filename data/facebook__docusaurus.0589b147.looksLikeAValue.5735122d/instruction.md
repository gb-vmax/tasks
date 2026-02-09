# Bug Report

### Describe the bug

I'm experiencing an issue where string values are no longer being accepted as valid input. After a recent update, the system seems to reject string content even though it should be supported.

### Reproduction

```js
// This used to work but now fails
const content = "# Hello World\n\nThis is some content";
processContent(content);  // Not recognized as valid

// Only Uint8Array seems to work now
const buffer = new Uint8Array([/* ... */]);
processContent(buffer);  // This works
```

### Expected behavior

Both string and Uint8Array values should be accepted as valid input. Strings are a common format for content and should continue to be supported alongside binary data.

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: 18.x

---
Repository: /testbed
