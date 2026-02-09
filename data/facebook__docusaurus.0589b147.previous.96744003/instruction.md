# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive where colons (`:`) in text directives are not being handled correctly. It seems like the parser is either accepting or rejecting colons in the wrong contexts, causing directives to be parsed incorrectly or not at all.

### Reproduction

```js
// Example 1: Directive with colon in content
:directive[text with : colon]

// Example 2: Escaped colon scenario
:directive[text with \: escaped colon]
```

The parser appears to be incorrectly determining when a colon character should be allowed or rejected during directive text tokenization. This affects both regular colons and escaped colons in directive content.

### Expected behavior

The parser should correctly distinguish between:
- Colons that are part of the directive syntax
- Colons that are part of the directive content
- Escaped colons that should be treated as literal characters

The directive should be parsed properly in all these cases without incorrectly rejecting or accepting colon characters.

### System Info
- remark-directive version: 3.0.0
- Environment: Node.js

---
Repository: /testbed
