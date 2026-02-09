# Bug Report

### Describe the bug

JSX attributes with `=` (equals sign) in the attribute name are no longer being parsed correctly. When I try to use an attribute that contains an equals sign, it's not being recognized as a valid attribute name character.

### Reproduction

```jsx
<Component data-test=value />
```

When parsing this JSX, the `=` character in the attribute name position causes unexpected behavior. The parser seems to be treating `=` as a special character that terminates the attribute name, even when it should be part of the name itself.

### Expected behavior

The equals sign should be allowed as part of attribute names when appropriate, and the parser should handle it correctly according to JSX attribute naming rules. Previously this was working fine.

### Additional context

This seems to have started happening recently. I noticed the issue when working with attributes that use special characters. The parser is being too restrictive about what characters are allowed in attribute names.

---
Repository: /testbed
