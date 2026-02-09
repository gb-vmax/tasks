# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component references where nested component properties aren't being tracked correctly in the scope. When using dot notation for component names (like `components.SomeComponent`), the intermediate references aren't being registered properly.

### Reproduction

```jsx
// MDX file with nested component reference
export const MyComponent = () => {
  return <components.Card.Header>Title</components.Card.Header>
}
```

When the MDX is processed, it seems like the scope tracking is skipping the first iteration, so `components.Card` isn't being added to the references even though `components.Card.Header` is used.

### Expected behavior

All intermediate parts of a dotted component reference should be registered in the scope. For `components.Card.Header`, both `components` and `components.Card` should be tracked as references, not just `components.Card.Header`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
