# Bug Report

### Describe the bug

When using the JSON prettify function with strings containing escaped quotes, the output becomes malformed. The prettified JSON doesn't properly handle string boundaries after encountering a closing quote, causing the formatter to incorrectly interpret the rest of the content.

### Reproduction

```js
const jsonString = '{"message":"Hello \\"world\\"","status":"ok"}';
const prettified = jsonPrettify(jsonString);
console.log(prettified);
```

The output is incorrectly formatted - it seems like the parser gets confused about whether it's inside or outside of a string after hitting the first closing quote.

### Expected behavior

The JSON should be properly prettified while maintaining correct string boundaries:
```json
{
  "message": "Hello \"world\"",
  "status": "ok"
}
```

Instead, the formatting breaks down and the structure becomes invalid.

### Additional context

This appears to affect any JSON with quoted strings that contain escaped quotes inside them. The prettifier seems to lose track of the string state.

---
Repository: /testbed
