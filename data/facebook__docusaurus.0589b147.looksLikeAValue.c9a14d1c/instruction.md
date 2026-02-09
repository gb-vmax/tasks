# Bug Report

### Describe the bug

I'm encountering an issue with file processing where certain valid input types are being rejected. It seems like the validation logic is too strict and is not accepting inputs that should be valid.

### Reproduction

```js
// This should work but doesn't
const processor = remark();

// String input - works fine
processor.process("# Hello");

// Uint8Array input - this fails now
const buffer = new Uint8Array([35, 32, 72, 101, 108, 108, 111]); // "# Hello" in bytes
processor.process(buffer);
```

The second case with Uint8Array should be accepted as valid input, but it's being rejected. This worked in previous versions.

### Expected behavior

Both string and Uint8Array inputs should be accepted as valid input types for processing. The validator should return `true` for either type.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
