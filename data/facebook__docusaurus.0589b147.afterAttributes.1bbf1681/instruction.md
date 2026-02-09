# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the parser crashes when processing leaf directives with attributes. The error occurs when trying to parse directives that have both labels and attributes.

### Reproduction

```js
const input = `::directive[label]{attr=value}`;

// Parser crashes when processing this input
parser.parse(input);
```

The issue seems to happen specifically with leaf directives (double colon syntax) that include both a label in square brackets and attributes in curly braces.

### Expected behavior

The parser should successfully parse leaf directives with attributes and return the appropriate AST nodes without throwing errors.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
