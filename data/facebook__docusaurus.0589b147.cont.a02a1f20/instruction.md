# Bug Report

### Describe the bug

I'm encountering an issue with identifier continuation validation in JSX/MDX parsing. It seems like valid identifiers are being rejected while invalid ones are being accepted. The behavior is completely inverted from what it should be.

### Reproduction

When parsing MDX content with JSX elements that have valid identifier names, the parser incorrectly rejects them. Conversely, identifiers that should be invalid are being accepted.

For example:
```jsx
// Valid identifiers that should work but don't
<MyComponent123 />
<Component_Name />

// Invalid identifiers that shouldn't work but do
<Component-Invalid />
<123Component />
```

The issue appears to affect the continuation character validation for identifiers - characters that are valid for continuing an identifier (like letters, digits, underscores) are being treated as invalid, and vice versa.

### Expected behavior

The parser should correctly validate identifier continuation characters according to the ECMAScript/JSX specification:
- Valid continuation characters (letters, digits, underscores, etc.) should be accepted
- Invalid continuation characters (hyphens, spaces, special symbols at invalid positions) should be rejected

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression as this was working correctly in previous versions.

---
Repository: /testbed
