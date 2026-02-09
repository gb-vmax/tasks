# Bug Report

### Describe the bug

When using self-closing JSX tags in MDX content, the parser is incorrectly throwing an error about "Unexpected self-closing slash `/` in closing tag" for valid self-closing tags like `<Component />`. This appears to be a logic error in the validation.

### Reproduction

```jsx
// This valid MDX syntax now throws an error
<MyComponent />

// Error message:
// "Unexpected self-closing slash `/` in closing tag, expected the end of the tag"
```

The error is triggered when parsing any self-closing JSX tag, even though self-closing tags are perfectly valid JSX/MDX syntax.

### Expected behavior

Self-closing tags like `<Component />` should parse without errors. The error message about unexpected self-closing slash should only appear for actual closing tags that incorrectly include a slash, like `</Component />`.

### Additional context

This seems to have started recently. The validation logic appears to be inverted - it's rejecting self-closing tags when it should be accepting them, and would accept malformed closing tags when it should reject them.

---
Repository: /testbed
