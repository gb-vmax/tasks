# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component resolution where the `MDXLayout` component is not being properly aliased to `wrapper` in the compiled output. When I use `MDXLayout` in my MDX file, it seems like the component mapping is getting confused.

### Reproduction

```jsx
// MyComponent.mdx
export { CustomLayout as MDXLayout } from './layouts'

# Hello World

This is my content
```

When this gets compiled, the `MDXLayout` export should be mapped to `wrapper` internally, but it appears the mapping is incorrect. The component doesn't render as expected and the layout is not applied.

### Expected behavior

The `MDXLayout` component should be correctly aliased to `wrapper` in the compiled JSX output so that the layout is properly applied to the MDX content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
