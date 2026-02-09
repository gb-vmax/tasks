# Bug Report

### Describe the bug

When using JSX attributes with member expressions (like `foo.bar`), the MDX compiler is incorrectly throwing an error saying "Member expressions in attribute names are not supported" even though member expressions should not be allowed in attribute names.

### Reproduction

```jsx
// This should throw an error but currently doesn't
<Component foo.bar="value" />
```

The compiler is accepting member expression syntax in JSX attribute names when it should be rejecting them. This allows invalid JSX to pass through without proper validation.

### Expected behavior

The compiler should throw an error when member expressions are used in JSX attribute names, as they are not valid JSX syntax. Currently, the validation logic appears to be inverted - it's throwing errors for valid attribute names and accepting invalid ones.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
