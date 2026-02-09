# Bug Report

### Describe the bug

I'm encountering an issue with identifier/name continuation validation in MDX content. It seems like valid identifier characters are being rejected incorrectly, causing parsing to fail on what should be valid MDX syntax.

### Reproduction

```jsx
// This MDX content fails to parse correctly
<MyComponent propertyName="value" />

// Even simple identifiers with valid continuation characters are affected
<div className="test" />
```

When trying to parse MDX with components that have standard property names or className attributes, the parser rejects them as invalid even though they should be perfectly valid according to JavaScript identifier rules.

### Expected behavior

The parser should correctly identify valid identifier continuation characters and allow standard JSX/MDX syntax to parse without errors. Properties and component names using alphanumeric characters should be accepted.

### Additional context

This appears to affect any MDX content with component properties or attributes. The issue seems related to character validation for identifiers, where valid characters are being incorrectly flagged as invalid.

---
Repository: /testbed
