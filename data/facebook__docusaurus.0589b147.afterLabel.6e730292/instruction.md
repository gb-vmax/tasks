# Bug Report

### Describe the bug

I'm encountering an issue with text directives in remark-directive where the parser behaves incorrectly when processing directives without attributes. The condition for checking the opening brace character `{` (code 123) seems to be inverted, causing the parser to attempt attribute parsing when it shouldn't and skip it when it should.

### Reproduction

```js
// This directive without attributes fails to parse correctly
:directive[label text]

// Meanwhile this one with attributes also has issues
:directive[label]{key="value"}
```

When parsing text directives, the logic after the label should check if the next character is `{` to determine whether to parse attributes. However, the current behavior is reversed - it's checking if the code is NOT 123 instead of checking if it IS 123.

### Expected behavior

Text directives should correctly parse both with and without attributes:
- `:directive[label]` should parse successfully without attempting to parse attributes
- `:directive[label]{attrs}` should parse successfully and extract the attributes

The parser should check if the character IS `{` (code 123) before attempting to parse attributes, not if it ISN'T.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
