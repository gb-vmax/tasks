# Bug Report

### Describe the bug

I'm experiencing an issue with JSON prettification where strings containing escape sequences are not being handled correctly. The prettifier seems to be corrupting the output when processing JSON strings with backslashes and escape characters.

### Reproduction

```js
const jsonString = '{"message": "Hello\\nWorld"}';
const prettified = jsonPrettify(jsonString);
// Output is malformed - escape sequences appear duplicated or broken
```

Another example:
```js
const jsonWithEscapes = '{"path": "C:\\\\Users\\\\test"}';
const result = jsonPrettify(jsonWithEscapes);
// The backslashes are not preserved correctly in the output
```

### Expected behavior

The prettifier should correctly preserve escape sequences in JSON strings. When prettifying JSON with `\n`, `\t`, `\\`, or other valid escape sequences, the output should maintain the exact same escape sequences as the input, just with added formatting/indentation.

### Additional context

This appears to be affecting any JSON that contains:
- Newline characters (`\n`)
- Tab characters (`\t`)
- Backslashes (`\\`)
- Unicode escape sequences (`\uXXXX`)

The prettified output either duplicates the escape characters or produces invalid JSON that can't be parsed back.

---
Repository: /testbed
