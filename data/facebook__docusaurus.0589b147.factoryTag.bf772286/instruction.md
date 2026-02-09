# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where quoted attribute values are not being handled correctly. When using JSX-style attributes with quoted strings in MDX files, the parser seems to fail or produce unexpected results.

### Reproduction

```mdx
<Component name="value" />
```

When I try to use a component with a quoted attribute value like the example above, the attribute parsing doesn't work as expected. The quoted string is not being recognized properly, causing the MDX content to fail parsing or render incorrectly.

### Expected behavior

The parser should correctly handle quoted attribute values in JSX-style tags within MDX content. Attributes like `name="value"` should be parsed normally and the component should render with the correct props.

### Additional context

This seems to be related to how the parser handles the opening and closing quotes of attribute values. It's affecting all quoted attributes in my MDX files, making it impossible to use string literals in component props.

---
Repository: /testbed
