# Bug Report

### Describe the bug
The `response.size()` method is returning incorrect values for responses with multi-byte characters. When the response body contains UTF-8 encoded text with non-ASCII characters (like emojis, Chinese characters, etc.), the size calculation doesn't match the actual byte size of the content.

### Reproduction
```js
// Response with multi-byte UTF-8 characters
const response = {
  body: "Hello 世界 🌍",
  headers: {} // No Content-Length header
}

const size = response.size();
// Returns incorrect value - doesn't account for multi-byte characters
```

### Expected behavior
The `size()` method should return the actual byte size of the response body, properly accounting for multi-byte characters in different encodings (UTF-8, UTF-16, etc.). For example:
- ASCII characters should count as 1 byte each
- Chinese characters in UTF-8 should count as 3 bytes each
- Emojis should count as 4 bytes

Currently it seems to just count the string length rather than the actual byte size.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
