# Bug Report

### Describe the bug

Directive syntax is not being parsed correctly - the parser seems to be looking for the wrong character code when tokenizing leaf directives. This causes valid directive syntax to fail parsing.

### Reproduction

```js
// Trying to use a leaf directive with the standard syntax
const input = `:directiveName[content]`

// Parser fails to recognize this as a valid directive
// The directive is not tokenized properly
```

### Expected behavior

The parser should correctly tokenize leaf directives that start with `:` (colon, character code 58). Currently it appears to be checking for a different character code instead.

Additionally, the end condition for directives seems inverted - it's exiting when it should continue parsing and continuing when it should exit.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
