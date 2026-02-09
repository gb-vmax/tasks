# Bug Report

### Describe the bug
The JSON prettify function is not handling escaped quotes correctly in strings. When a JSON string contains `\"` (escaped double quote), the prettifier seems to get confused about whether the string has ended or not, leading to incorrect formatting.

### Reproduction
```js
const jsonWithEscapedQuotes = '{"message":"He said \\"hello\\" to me"}';
const prettified = jsonPrettify(jsonWithEscapedQuotes);
console.log(prettified);
```

The output is malformed - the escaped quotes inside the string value are not being preserved properly, and the formatting breaks.

### Expected behavior
The prettified JSON should maintain the escaped quotes within string values and produce valid, well-formatted JSON output like:
```json
{
  "message": "He said \"hello\" to me"
}
```

### Additional context
This seems to affect any JSON strings that contain escaped double quotes. The prettifier should recognize that `\"` is not the end of a string, but rather an escaped character within the string.

---
Repository: /testbed
