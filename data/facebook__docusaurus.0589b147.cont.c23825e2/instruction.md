# Bug Report

### Describe the bug

I'm experiencing an issue with identifier parsing in MDX where valid identifiers are being rejected and invalid ones are being accepted. It seems like the validation logic is inverted - characters that should be allowed in identifiers are causing errors, while characters that shouldn't be valid are passing through.

### Reproduction

```js
// This should work but doesn't
const validIdentifier = "myComponent123"

// This incorrectly passes validation
const invalidIdentifier = "my-component@#$"
```

When trying to use standard JavaScript identifier names in MDX components, they're being flagged as invalid. Conversely, identifiers with special characters that shouldn't be allowed are not throwing errors.

### Expected behavior

The parser should accept valid JavaScript identifiers (letters, numbers, underscores, dollar signs in valid positions) and reject identifiers with invalid characters like hyphens, at-signs, or other special symbols.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started recently and is breaking existing MDX files that were working before.

---
Repository: /testbed
