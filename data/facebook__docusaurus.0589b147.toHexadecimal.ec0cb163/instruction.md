# Bug Report

### Describe the bug

After a recent update, HTML entity encoding is producing lowercase hexadecimal values instead of uppercase. This is causing issues with systems that expect uppercase hex entities.

### Reproduction

When encoding special characters to HTML entities, the hexadecimal representation is now in lowercase format:

```js
// Current behavior (incorrect):
// Produces: &#x1f600; 

// Expected behavior:
// Should produce: &#x1F600;
```

The entity codes are being generated with lowercase letters (a-f) instead of uppercase letters (A-F) as they were before.

### Expected behavior

HTML hexadecimal entity references should use uppercase letters for the hexadecimal digits (A-F), not lowercase (a-f). This was the previous behavior and is the standard format expected by many parsers and validators.

### Additional context

This appears to affect the `stringify-entities` functionality in the rehype-stringify package. The change is breaking compatibility with systems that validate or parse these entities expecting uppercase format.

---
Repository: /testbed
