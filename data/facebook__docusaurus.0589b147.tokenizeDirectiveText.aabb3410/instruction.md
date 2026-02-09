# Bug Report

### Describe the bug

I'm encountering an issue with directive text parsing in remark-directive. It seems like directives with colons (`:`) in the text are being rejected when they should be accepted, and the parser is checking for the wrong character code when processing attributes.

### Reproduction

```js
// This directive is incorrectly rejected
:directiveName[label]{attr}

// The parser seems to be checking for the wrong conditions:
// - Rejects when it encounters a colon (code 58) instead of accepting it
// - Checks for closing brace (code 125) instead of opening brace (code 123) for attributes
```

When trying to parse inline text directives with the standard syntax, they fail to parse correctly. The directive should accept the colon character as part of the valid syntax, but instead it's being treated as invalid.

### Expected behavior

Text directives should properly parse when they follow the correct syntax with colons. The parser should:
- Accept colons (`:`) as valid in directive text
- Check for opening braces (`{`) when looking for attributes, not closing braces (`}`)

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
