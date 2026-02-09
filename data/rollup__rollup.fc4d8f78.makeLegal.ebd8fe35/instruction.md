# Bug Report

### Describe the bug

I'm experiencing an issue with identifier transformation where kebab-case identifiers are not being converted correctly. When using identifiers with dashes (like `my-variable-name`), they're being converted to lowercase instead of camelCase.

### Reproduction

```js
// When transforming a kebab-case identifier
const input = 'my-variable-name';
const result = makeLegal(input);

// Expected: 'myVariableName'
// Actual: 'my_variable_name' (or similar incorrect format)
```

The transformation should convert dash-separated words to camelCase (e.g., `foo-bar` → `fooBar`), but instead the letters after dashes are being lowercased rather than uppercased.

### Expected behavior

Identifiers with dashes should be converted to valid camelCase identifiers:
- `my-var` should become `myVar`
- `some-long-name` should become `someLongName`
- `foo-bar-baz` should become `fooBarBaz`

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
