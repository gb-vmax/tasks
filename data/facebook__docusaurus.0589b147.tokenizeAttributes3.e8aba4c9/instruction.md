# Bug Report

### Describe the bug

I'm experiencing an issue with directive text attributes where the tokenization order seems to be causing problems. When using directives with various attribute types (IDs, classes, and regular attributes), the parsing doesn't work as expected.

### Reproduction

```js
// Example directive with mixed attributes
:directive[text]{#id .class attr=value}
```

When parsing directives that contain a combination of ID selectors, class selectors, and regular attributes, the attributes are not being recognized in the correct order. This affects how the directive is processed and can lead to incorrect attribute assignment.

### Expected behavior

All attribute types (IDs, classes, and name-value pairs) should be parsed correctly regardless of their order in the directive declaration. The tokenizer should handle:
- ID attributes (`#id`)
- Class attributes (`.class`)
- Regular attributes with values (`attr=value`)

in the proper sequence.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
