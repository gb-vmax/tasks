# Bug Report

### Describe the bug

When using JSX elements with multiple attributes where the `key` attribute appears after a spread attribute, the last attribute in the list is being skipped during rendering. This causes the final attribute to not be included in the compiled output.

### Reproduction

```jsx
const element = (
  <Component 
    {...spread} 
    key="test"
    data-last="value"
  />
)
```

In the example above, the `data-last` attribute is not being processed correctly. The issue occurs specifically when:
1. There's a spread attribute (`{...spread}`)
2. Followed by a `key` attribute
3. Followed by at least one more attribute

### Expected behavior

All attributes should be included in the compiled output, including the last one in the list. The `data-last` attribute should appear in the final rendered component.

### System Info

- Rollup version: latest
- JSX mode: automatic
- Build target: ES modules

---
Repository: /testbed
