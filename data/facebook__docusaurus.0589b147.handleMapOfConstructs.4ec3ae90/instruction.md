# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where certain code constructs are not being properly recognized. When processing MDX content, some valid syntax is being skipped or incorrectly parsed, particularly when dealing with null/undefined code points.

### Reproduction

```js
// When the tokenizer encounters a null code point
// Expected: Should check map[code2] when code2 is null
// Actual: The lookup fails because the condition is inverted

const map = {
  null: [someConstruct],
  65: [otherConstruct]  // character 'A'
}

// Processing null code point doesn't retrieve the correct construct
// Processing non-null code points also fails to get the right definition
```

The tokenizer seems to be checking the wrong condition when looking up constructs from the map, causing it to miss valid syntax definitions.

### Expected behavior

The tokenizer should correctly retrieve construct definitions from the map for both null and non-null code points. Valid MDX syntax should be properly tokenized and parsed without being skipped.

### System Info
- MDX version: 3.0.0
- Environment: Jest testing environment

---
Repository: /testbed
