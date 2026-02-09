# Bug Report

### Describe the bug

The JSON prettifier is not handling escape sequences correctly in strings. When prettifying JSON that contains escaped characters, the output is malformed with duplicate escape sequences appearing in the result.

### Reproduction

```js
const jsonString = '{"message": "Hello\\nWorld"}';
const prettified = jsonPrettify(jsonString);
console.log(prettified);
// Expected: 
// {
//   "message": "Hello\nWorld"
// }
// 
// Actual output has duplicated escape sequences
```

Another example with unicode escapes:

```js
const jsonWithUnicode = '{"emoji": "\\u2764"}';
const result = jsonPrettify(jsonWithUnicode);
// The unicode sequence gets duplicated or mangled
```

### Expected behavior

The prettifier should preserve escape sequences exactly as they appear in the input JSON. Valid JSON escape sequences like `\n`, `\t`, `\"`, `\\`, and unicode sequences like `\uXXXX` should be handled correctly without duplication.

### System Info
- Using latest version of Insomnia
- Affects JSON prettification in request/response bodies

---
Repository: /testbed
