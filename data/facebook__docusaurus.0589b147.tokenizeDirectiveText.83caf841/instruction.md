# Bug Report

### Describe the bug

I'm encountering an issue with directive text parsing where colons (`:`) in directive text are being incorrectly rejected. After a recent update, directives that should be valid are now failing to parse properly.

### Reproduction

```js
// This directive should be parsed correctly but isn't
:directive[label]{attr=value}

// The parser seems to be rejecting valid syntax with colons
:myDirective some text
```

When trying to use directive text syntax with colons, the parser appears to be treating them incorrectly. The directive text should allow colons in certain positions but they're being rejected.

### Expected behavior

Directive text with colons should be parsed correctly according to the directive syntax specification. The parser should properly handle the colon character in directive names and continue processing the rest of the directive (labels, attributes, etc.).

### Additional context

This seems related to how the tokenizer handles character codes - specifically around code `58` (colon character) and potentially code `123`/`125` (curly braces). The parsing logic appears to have changed in how it validates these characters in the directive text flow.

---
Repository: /testbed
