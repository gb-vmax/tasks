# Bug Report

### Describe the bug

I'm encountering an issue with inline directive parsing in remark-directive. The parser seems to be rejecting valid inline directives that contain colons (`:`) in their syntax, but it's also not correctly handling the label syntax with square brackets.

### Reproduction

```js
// This directive is being rejected when it should be valid
:directiveName[label text]{attributes}

// The parser appears to be checking for the wrong character codes
// when validating directive syntax
```

When trying to parse inline text directives with the standard syntax, the parser incorrectly rejects them. It seems like the validation logic for what characters are allowed after the directive name is inverted or checking for the wrong conditions.

### Expected behavior

Inline directives with the format `:directiveName[label]{attributes}` should be parsed correctly. The parser should:
1. Accept the colon prefix
2. Parse the directive name
3. Handle optional label in square brackets
4. Handle optional attributes in curly braces

Currently, the character code validation after the directive name appears to be backwards - it's rejecting valid syntax and potentially accepting invalid syntax.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
