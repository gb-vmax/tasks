# Bug Report

### Describe the bug

I'm encountering an issue with directive attributes parsing where the attribute name and value are getting mixed up or not stored correctly. When I use directives with attributes in my markdown, the resulting parsed data structure seems to have the wrong format.

### Reproduction

```js
// Parsing markdown with directive attributes
const markdown = `
:::myDirective{name="value"}
content
:::
`;

// After parsing, the directive attributes array contains incorrect data
// Expected: [["name", "value"]]
// Actual: The structure is malformed
```

### Expected behavior

Directive attributes should be stored as key-value pairs in an array format like `[["attributeName", "attributeValue"]]`. The attribute name should come first, followed by the value.

### Additional context

This seems to affect any directive that uses attributes with the `{key="value"}` syntax. The parsed output doesn't match what I'd expect based on the directive syntax specification.

---
Repository: /testbed
