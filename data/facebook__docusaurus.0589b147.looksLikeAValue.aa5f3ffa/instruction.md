# Bug Report

### Describe the bug

I'm encountering an issue with file processing where valid string content is being rejected. After a recent update, the system seems to be incorrectly validating input values, causing legitimate string data to fail validation checks.

### Reproduction

```js
// This should work but doesn't
const content = "# Hello World\n\nThis is markdown content";
// Processing fails even though content is a valid string

// Also affects Uint8Array inputs
const buffer = new Uint8Array([72, 101, 108, 108, 111]);
// This also gets rejected incorrectly
```

### Expected behavior

Both string content and Uint8Array buffers should be accepted as valid input values. The validation logic should treat these as separate valid types (string OR Uint8Array), not require both conditions simultaneously.

Currently getting unexpected validation failures when trying to process markdown files with string content.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
