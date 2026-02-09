# Bug Report

### Describe the bug
When prettifying JSON that contains escaped unicode sequences like `\\u0041`, the conversion is producing incorrect output. The function seems to be handling the escape detection incorrectly, causing characters to be dropped or malformed in the final output.

### Reproduction
```js
const input = '{"test": "\\\\u0041"}';  // Escaped unicode sequence
const result = prettify(input);
// Result is malformed - characters are missing or incorrect
```

Another example:
```js
const input = '{"value": "\\u0048ello"}';  // \u0048 should convert to 'H'
const result = prettify(input);
// Expected: {"value": "Hello"}
// Actual: Characters appear to be shifted or dropped
```

### Expected behavior
The unicode conversion should properly handle escaped backslashes and convert unicode sequences without dropping characters. When a unicode sequence like `\u0048` is present, it should be converted to its corresponding character while preserving all other characters in the string.

### System Info
- Package: insomnia
- Component: JSON prettifier (utils/prettify/json.ts)

This seems to have started recently, possibly related to changes in how the escape character detection works in the `convertUnicode` function.

---
Repository: /testbed
