# Bug Report

### Describe the bug
The JSON prettifier is not handling unicode escape sequences correctly. When converting unicode characters in JSON strings, the output is malformed - characters appear to be getting dropped or shifted incorrectly.

### Reproduction
```js
const jsonStr = '{"text": "Hello \\u0057orld"}';
const prettified = prettifyJson(jsonStr);
// Expected: {"text": "Hello World"}
// Actual: Characters are missing or incorrect
```

Another example with multiple unicode sequences:
```js
const jsonStr = '{"message": "\\u0048\\u0065\\u006c\\u006c\\u006f"}';
const prettified = prettifyJson(jsonStr);
// Expected: {"message": "Hello"}
// Actual: Output is corrupted
```

### Expected behavior
Unicode escape sequences like `\u0057` should be properly converted to their corresponding characters without losing or misplacing other characters in the string.

### Additional context
This seems to affect the `convertUnicode` function in the JSON prettifier. The conversion itself might be working, but there's something wrong with how the final string is being assembled - characters at the end of the string appear to be getting cut off.

---
Repository: /testbed
