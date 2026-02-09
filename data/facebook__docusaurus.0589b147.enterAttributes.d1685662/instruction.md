# Bug Report

### Describe the bug

I'm encountering an issue with directive attributes not being properly initialized. When using directives with attributes, I'm getting unexpected behavior where the attributes seem to be undefined or not accessible.

### Reproduction

```js
// Using a directive with attributes
:::note{#my-id .my-class}
Some content
:::
```

When parsing the above directive, the attributes don't seem to be captured correctly. The directive appears to parse, but accessing the attributes returns undefined or causes errors.

### Expected behavior

The directive attributes should be properly initialized and accessible. The parser should handle directives with ID and class attributes without issues.

### Additional context

This seems to affect any directive that includes attributes in the curly braces syntax. Simple directives without attributes work fine, but as soon as I add attributes like `{#id}` or `{.class}`, things break.

---
Repository: /testbed
