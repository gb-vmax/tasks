# Bug Report

### Describe the bug

I'm experiencing an issue with identifier name conversion when using hyphenated names. It seems like the conversion to camelCase is not working as expected - letters after hyphens are being converted to lowercase instead of uppercase.

### Reproduction

```js
// When converting a hyphenated identifier like 'my-variable-name'
// Expected: 'myVariableName'
// Actual: 'my-variable-name' (hyphens removed but lowercase)

const result = makeLegal('my-test-value');
// Expected: myTestValue
// Actual: mytestvalue
```

Also noticing that when an empty string is passed, it returns an empty string instead of a fallback value:

```js
makeLegal('');
// Expected: '_'
// Actual: ''
```

### Expected behavior

1. Hyphenated identifiers should be converted to proper camelCase (e.g., `my-variable` → `myVariable`)
2. Empty strings should return a valid fallback identifier

This is breaking identifier generation in my build output.

### System Info
- Latest version from main branch

---
Repository: /testbed
