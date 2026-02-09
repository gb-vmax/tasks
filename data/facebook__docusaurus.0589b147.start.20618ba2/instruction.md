# Bug Report

### Describe the bug

I'm encountering an issue where valid identifier names are being rejected when parsing MDX content. It seems like the identifier validation logic is broken - characters that should be accepted as valid starting characters for identifiers are not being recognized correctly.

### Reproduction

```js
// This should work but doesn't
const mdxContent = `
export const validIdentifier = 'test'
`

// Trying to parse MDX with valid JavaScript identifiers fails
// The parser rejects valid identifier names that start with 
// legitimate characters like letters or underscore
```

### Expected behavior

Valid JavaScript/JSX identifiers should be accepted by the parser. Any identifier starting with a letter, underscore, or dollar sign (followed by valid continuation characters) should parse successfully.

Currently it seems like the validation is inverted - it's rejecting valid identifiers instead of accepting them.

### Additional context

This appears to affect all identifier validation in MDX content, including variable names, function names, and component names. The issue manifests when the parser encounters what should be perfectly valid identifier syntax.

---
Repository: /testbed
