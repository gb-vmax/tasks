# Bug Report

### Describe the bug

The `indent` function is not properly indenting strings anymore. When I have multi-line content that needs to be indented for code generation, the indentation is completely broken.

### Reproduction

```js
const multiLineString = `line1
line2
line3`;

const indented = indent(multiLineString);
// Expected: "  line1\n  line2\n  line3"
// Actual: Incorrect indentation or missing leading spaces
```

Also happens with strings that have trailing newlines:

```js
const stringWithTrailingNewline = `content
`;

const indented = indent(stringWithTrailingNewline);
// The indentation is wrong
```

### Expected behavior

All lines in the string should be indented by 2 spaces consistently. The function should add "  " at the beginning and replace all newlines with "\n  " to maintain proper indentation throughout the entire string.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently and is affecting route generation code.

---
Repository: /testbed
