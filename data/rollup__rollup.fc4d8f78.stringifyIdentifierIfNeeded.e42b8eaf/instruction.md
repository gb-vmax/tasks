# Bug Report

### Describe the bug

I'm encountering an issue where valid JavaScript identifiers are being unnecessarily quoted/stringified in the generated output. This seems to be affecting property names and object keys that should be valid as-is.

### Reproduction

```js
// When generating code with valid identifiers
const obj = {
  validName: 'value',
  anotherValid123: 'test',
  $special: 'data'
}

// Expected output:
// { validName: 'value', anotherValid123: 'test', $special: 'data' }

// Actual output:
// { "validName": "value", "anotherValid123": "test", "$special": "data" }
```

Valid JavaScript identifiers (like `validName`, `test123`, `$value`, `_private`) are being wrapped in quotes when they shouldn't be. This makes the generated code unnecessarily verbose and harder to read.

### Expected behavior

Only identifiers that contain special characters, start with numbers, or are reserved keywords should be stringified. Normal valid identifiers should remain unquoted.

### Additional context

This appears to be a regression - the logic for determining when to stringify identifiers seems to be inverted. Valid identifiers that pass the identifier regex test are being quoted instead of invalid ones.

---
Repository: /testbed
