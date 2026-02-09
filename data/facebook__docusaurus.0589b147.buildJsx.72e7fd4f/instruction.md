# Bug Report

### Describe the bug

When using MDX with JSX elements that have exactly one child, the children are not being wrapped in an array as expected. This causes issues with components that expect children to always be an array type.

### Reproduction

```jsx
// MDX file
<MyComponent>
  <div>Single child</div>
</MyComponent>

// Component expecting array children
function MyComponent({ children }) {
  // This fails because children is not an array when there's only one child
  return children.map((child, i) => <div key={i}>{child}</div>)
}
```

### Expected behavior

Children should be consistently wrapped in an array regardless of whether there's one child or multiple children. This would make it easier to handle children uniformly in components without having to check if it's an array first.

### Additional context

This seems to be related to how the JSX transformation handles the children property. With multiple children it works fine, but with a single child the behavior is different.

---
Repository: /testbed
