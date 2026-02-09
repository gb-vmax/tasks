# Bug Report

### Describe the bug

I'm encountering an issue with directive name parsing where names containing hyphens are being rejected incorrectly. It appears that directives with hyphens in their names are not being recognized as valid, even though they should be allowed.

### Reproduction

```js
// This directive name with a hyphen is not being parsed correctly
:::my-directive
content here
:::

// The parser seems to reject it even though hyphenated names should be valid
```

When I try to use directives with hyphenated names (e.g., `my-directive`, `custom-component`), they fail to parse. The same issue occurs with names like `foo-bar` or `test-123`.

### Expected behavior

Directive names containing hyphens should be parsed correctly and treated as valid identifiers. Hyphenated naming is a common convention and should be supported.

### Additional context

This seems to have started recently. I'm using directives in my markdown processing pipeline and many of my existing directive names follow the hyphenated convention. The parser appears to be treating the hyphen as an invalid character in directive names.

---
Repository: /testbed
