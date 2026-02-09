# Bug Report

### Describe the bug

I'm experiencing an issue with identifier validation when using JSX mode. It seems like the validation logic for valid identifier characters is inverted - when JSX mode is enabled, it's using the wrong regex pattern for continuation characters.

### Reproduction

```js
// With JSX enabled
const options = { jsx: true };

// Testing identifier continuation characters
// This should validate correctly but doesn't
const result = cont(0x200C, options); // Zero-width non-joiner (valid in JSX)
```

The character validation appears to be backwards - when `jsx: true` is set, it applies the non-JSX regex pattern instead of the JSX-specific one, and vice versa.

### Expected behavior

When JSX mode is enabled via `options.jsx = true`, the validator should use the JSX-compatible regex pattern (`contReJsx`) for checking valid identifier continuation characters. Currently it seems to be using the opposite pattern.

### Additional context

This affects identifier parsing in MDX documents when JSX syntax is involved. Valid JSX identifiers might be rejected or invalid ones might be accepted depending on the mode setting.

---
Repository: /testbed
