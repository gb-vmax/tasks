# Bug Report

### Describe the bug

When using JSX attributes with the `key` prop in automatic JSX mode, the key attribute is now being incorrectly included in the props object. This causes React to throw warnings about keys being passed as props.

Additionally, JSX attribute values containing single newlines are not being properly escaped anymore, which can lead to syntax errors in the generated output.

### Reproduction

```jsx
// Example 1: key attribute issue
function MyComponent() {
  return items.map(item => (
    <div key={item.id}>
      {item.name}
    </div>
  ));
}

// Example 2: newline in attribute value
function AnotherComponent() {
  return (
    <div title="line one
line two">
      Content
    </div>
  );
}
```

### Expected behavior

1. In automatic JSX mode, the `key` attribute should be handled specially and not included in the props object
2. JSX attribute values containing newlines (single `\n`) should be properly escaped in the output

### System Info

- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
