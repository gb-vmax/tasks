# Bug Report

### Describe the bug

The JSON prettifier is not handling escaped quotes correctly in string values. When a JSON string contains an escaped quote character (`\"`), the prettifier seems to treat it as the end of the string, causing the output to be malformed.

### Reproduction

```js
const json = '{"message": "He said \\"hello\\" to me"}';
const prettified = jsonPrettify(json);
console.log(prettified);
```

The output is incorrectly formatted - the string gets terminated prematurely at the escaped quote.

### Expected behavior

The prettifier should recognize that `\"` is an escaped quote and not the end of the string. The output should be properly formatted JSON with the escaped quotes preserved within the string value.

Example expected output:
```json
{
  "message": "He said \"hello\" to me"
}
```

### Additional context

This seems to affect any JSON strings that contain escaped quotes. The prettifier appears to be losing track of whether it's inside a string or not when it encounters these escape sequences.

---
Repository: /testbed
