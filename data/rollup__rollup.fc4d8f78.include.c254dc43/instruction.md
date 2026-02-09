# Bug Report

### Describe the bug

I'm experiencing an issue with JSX element rendering where nested JSX children are not being included in the output bundle. When I have JSX elements with child components or elements inside them, those children are getting tree-shaken out even though they should be included.

### Reproduction

```jsx
function ParentComponent() {
  return (
    <div>
      <ChildComponent />
      <span>Some text</span>
    </div>
  );
}
```

In this case, the `ChildComponent` and `span` elements inside the `div` are not being included in the final bundle. The opening and closing `div` tags are there, but the children are missing.

### Expected behavior

All children elements within a JSX element should be included in the bundle when the parent element is included. The entire JSX tree should be preserved.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to tree-shaking optimizations or something else.

---
Repository: /testbed
