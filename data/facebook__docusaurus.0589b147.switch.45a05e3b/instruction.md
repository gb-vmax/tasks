# Bug Report

### Describe the bug

I'm experiencing an issue with the translation label validation in the eslint plugin. When I use string literals as translation labels, they're being incorrectly flagged or rejected, even though they should be valid. It seems like the validation logic is inverted.

### Reproduction

```js
// This should be valid but is being rejected
const label = 'Hello World';

// Template literals without expressions should also work
const template = `Static text`;
```

Both of these cases should pass validation as they are simple strings without any dynamic expressions, but they're being treated as invalid.

### Expected behavior

String literals and template literals without expressions should be recognized as valid translation labels. The validation should accept these cases and only reject strings that don't meet the translation label requirements.

### Additional context

This seems to have started recently. The behavior is backwards from what I'd expect - valid strings are being rejected while they should be accepted.

---
Repository: /testbed
