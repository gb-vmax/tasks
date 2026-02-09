# Bug Report

### Describe the bug

I'm encountering an issue where valid JavaScript identifiers are being rejected when parsing MDX content. It seems like the identifier validation logic is inverted - identifiers that should be accepted are being rejected, and vice versa.

### Reproduction

```js
// This should work but doesn't
const mdxContent = `
export const validIdentifier = 'test'

<Component prop={validIdentifier} />
`

// Parsing fails for valid identifiers starting with letters, $, or _
// But somehow accepts invalid cases (like starting with numbers)
```

### Expected behavior

Valid JavaScript identifiers (starting with letters, `$`, or `_`) should be accepted when parsing MDX. The parser should correctly validate identifier names according to JavaScript naming rules.

### Additional context

This appears to affect any MDX content that uses standard variable names or component props. The validation seems to be backwards - rejecting valid identifiers while potentially accepting invalid ones.

---
Repository: /testbed
