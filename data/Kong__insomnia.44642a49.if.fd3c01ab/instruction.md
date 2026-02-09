# Bug Report

### Describe the bug

I'm experiencing an issue with JSON prettification when the input contains escaped characters at the end of a string. The prettifier seems to be handling escape sequences incorrectly in certain edge cases.

### Reproduction

```js
const jsonString = '{"test": "value with backslash\\"}';
const prettified = jsonPrettify(jsonString);
console.log(prettified);
```

When I try to prettify JSON that has a backslash as the last character before the closing quote, the output is malformed. The escape sequence isn't being processed correctly.

### Expected behavior

The JSON should be prettified correctly regardless of where escape sequences appear in the string, including at the end. The backslash should be properly escaped in the output.

### System Info
- Package: @insomnia/insomnia
- Component: utils/prettify/json.ts

---
Repository: /testbed
