# Bug Report

### Describe the bug

I'm experiencing an issue with Unicode escape sequence conversion in JSON prettification. When converting Unicode sequences like `\u0048` to their character equivalents, the conversion seems to be including an extra character from the original string before the converted character.

### Reproduction

```js
const input = '{"message": "\\u0048ello"}';
const prettified = prettify(input);

// Expected: {"message": "Hello"}
// Actual: {"message": "\\Hello"}
```

The backslash before the Unicode sequence is being included in the output when it shouldn't be. This happens with any Unicode escape sequence in the string.

Another example:
```js
const input = '{"text": "Test\\u0020string"}';
// Expected: {"text": "Test string"}
// Actual: {"text": "Test\\ string"}
```

### Expected behavior

Unicode escape sequences should be cleanly converted to their character representations without including the preceding character from the original string.

### System Info
- Package: insomnia
- Version: latest

---
Repository: /testbed
