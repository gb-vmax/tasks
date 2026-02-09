# Bug Report

### Describe the bug

I'm encountering an issue where JSX attributes with quoted string values are not being parsed correctly. When I try to use double or single quotes for attribute values in JSX/MDX, the parser crashes with an error message.

### Reproduction

```jsx
// This fails to parse
<Component name="value" />

// This also fails
<Component name='value' />
```

The parser seems to reject both double and single quoted strings as attribute values, even though these are standard JSX syntax.

### Expected behavior

Standard JSX attribute syntax with quoted strings should be parsed without errors. Both of these should work:
- `<Component name="value" />`
- `<Component name='value' />`

The parser should accept quoted string literals as valid attribute values.

### Additional context

Expression-based attributes with curly braces might still work, but quoted string literals (which are the most common way to pass string values) appear to be broken.

---
Repository: /testbed
