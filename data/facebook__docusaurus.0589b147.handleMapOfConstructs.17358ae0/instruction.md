# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where it's not properly handling certain code patterns. When processing specific character codes, the tokenizer seems to be checking for the wrong condition and this causes it to miss valid constructs.

### Reproduction

```js
// When the tokenizer encounters a null code
// It should look up the construct definition for that code
// But instead it's checking if code === null before lookup

const map = {
  65: someConstruct,  // 'A'
  null: fallbackConstruct
}

// When code is 65 (character 'A'), it should find someConstruct
// But the logic is inverted and checks code === null instead of code !== null
```

The tokenizer is checking `code2 === null` when it should be checking `code2 !== null` for the definition lookup. This means:
- Valid character codes don't get their constructs
- The null fallback is being applied incorrectly

### Expected behavior

The tokenizer should:
1. Look up the construct for the actual code value when code is not null
2. Use the null fallback construct appropriately
3. Combine both lists correctly when both are available

### System Info
- MDX version: 3.0.0
- Parser: micromark-based tokenizer

---
Repository: /testbed
