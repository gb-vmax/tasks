# Bug Report

### Describe the bug

I'm experiencing an issue with text directives where colons (`:`) are being handled incorrectly. It appears that directives with colons in certain positions are either not being parsed properly or are triggering unexpected behavior.

### Reproduction

```js
// Text directive with colon
:directive:text

// Expected to work but seems to fail
:some:directive[label]{attr}
```

When I try to use text directives that contain colons, they don't parse as expected. The directive parser seems to be rejecting valid syntax or accepting invalid syntax depending on where the colon appears.

### Expected behavior

Text directives should handle colons correctly according to the directive syntax specification. Directives with colons in the name portion should be parsed appropriately, and the parser should properly distinguish between valid and invalid colon placements.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
