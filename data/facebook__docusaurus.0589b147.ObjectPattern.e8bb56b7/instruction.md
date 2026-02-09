# Bug Report

### Describe the bug

I'm encountering an issue with object destructuring patterns in MDX files. When using destructuring in function parameters or variable declarations, the first property is being skipped and not included in the generated output.

### Reproduction

```jsx
// Example 1: Function parameter destructuring
function MyComponent({first, second, third}) {
  return <div>{first} {second} {third}</div>
}

// Example 2: Variable destructuring
const {a, b, c} = props;
```

When these patterns are processed, the first property (`first` or `a`) is missing from the destructured pattern, causing undefined values or runtime errors.

### Expected behavior

All properties in the destructuring pattern should be included in the generated code. The destructuring should work correctly and extract all specified properties from the object.

### Additional context

This appears to affect any code using object destructuring patterns. The generated output seems to be starting from the second property instead of the first one, which breaks the destructuring behavior.

---
Repository: /testbed
