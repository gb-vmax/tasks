# Bug Report

### Describe the bug

The base64 template tag is broken after a recent update. When trying to use it for encoding/decoding, I'm getting incomplete or cut-off results, especially when using URL-safe base64 encoding.

### Reproduction

```js
// Try to encode text using URL-safe base64
{% base64 'encode', 'url', 'Hello World' %}

// The output appears to be truncated or incomplete
```

I've also noticed that the encoding doesn't complete properly - it seems like the function just stops mid-execution. This is affecting all my API requests that rely on base64 encoding for authentication headers.

### Expected behavior

The base64 tag should properly encode the input text to URL-safe base64 format (replacing `+` with `-`, `/` with `_`, and removing padding `=` characters). The encoded output should be complete and valid.

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine before, not sure what changed but it's blocking my workflow. Any help would be appreciated!

---
Repository: /testbed
