# Bug Report

### Describe the bug

I'm encountering an issue with JSX/MDX tag parsing where tags followed by whitespace or line endings are being rejected when they should be accepted. The parser seems to have inverted logic that's causing valid syntax to fail.

### Reproduction

```jsx
// This should be valid but gets rejected
<Component />

// Also fails with whitespace after the tag
<Component /> 
```

When parsing MDX content with JSX tags that have whitespace or newlines immediately after the closing `>`, the parser incorrectly rejects them as invalid syntax.

### Expected behavior

JSX/MDX tags followed by whitespace or line endings should be parsed successfully. The presence of whitespace after a tag is normal and valid syntax that should not cause parsing to fail.

### Additional context

This appears to be related to the tag marker parsing logic. The behavior changed recently and is now causing previously working MDX files to fail parsing.

---
Repository: /testbed
