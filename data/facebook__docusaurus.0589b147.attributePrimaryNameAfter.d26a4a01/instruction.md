# Bug Report

### Describe the bug

When parsing MDX attributes with the `=` sign, the parser seems to be incorrectly handling the attribute value state. After encountering an equals sign in an attribute name, the parser is not properly transitioning to parse the attribute value.

### Reproduction

```jsx
<Component attribute="value" />
```

When parsing JSX/MDX tags with attributes that have values (using `=`), the attribute value is not being recognized or parsed correctly. This affects any component that uses standard HTML/JSX attribute syntax.

### Expected behavior

The parser should correctly handle attributes with values:
- Recognize the `=` as an initializer marker
- Transition to the attribute value parsing state
- Parse the attribute value (quoted strings, expressions, etc.)

Instead, it appears the parser may be transitioning to the wrong state after encountering the equals sign, causing attribute values to not be processed as expected.

### Additional context

This seems to affect basic JSX/MDX syntax that should work out of the box. Any component with attributes like `className="foo"` or `value="bar"` would be impacted.

---
Repository: /testbed
