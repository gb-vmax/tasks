# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where only the first element from arrays is being rendered instead of all elements. When a handler returns an array of nodes, it seems like only the first node in the array is being included in the output.

### Reproduction

```js
// When processing MDX content with elements that return multiple nodes
const mdxContent = `
<CustomComponent>
  <Child1 />
  <Child2 />
  <Child3 />
</CustomComponent>
`

// Expected: All three child components should render
// Actual: Only Child1 renders
```

This appears to affect any scenario where the MDX processor handles nodes that should expand into multiple elements. The array spreading logic seems to have been modified and now only takes the first element instead of spreading all elements.

### Expected behavior

When a node handler returns an array of elements, all elements in that array should be included in the final output, not just the first one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
