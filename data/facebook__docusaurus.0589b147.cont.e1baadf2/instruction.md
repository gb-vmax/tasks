# Bug Report

### Describe the bug

I'm experiencing an issue with MDX identifier validation where valid identifier characters are being rejected. It seems like the logic for checking whether a character can continue an identifier is inverted.

### Reproduction

When trying to use valid JavaScript identifiers in MDX components, they're incorrectly flagged as invalid. For example:

```jsx
<MyComponent prop={value} />
```

The identifier continuation check appears to fail for valid characters that should be allowed in JavaScript identifiers. This affects component names, prop names, and other identifiers in MDX content.

### Expected behavior

Valid JavaScript identifier characters should be recognized correctly. The identifier continuation logic should return `true` for valid identifier continuation characters and `false` otherwise.

### Additional context

This appears to be related to the character validation logic in the MDX parser. The behavior is backwards from what's expected - it's rejecting valid characters instead of accepting them.

---
Repository: /testbed
