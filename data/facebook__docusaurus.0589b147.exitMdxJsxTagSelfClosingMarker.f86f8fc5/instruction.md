# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being properly marked as self-closing. When parsing JSX components with the self-closing syntax (`<Component />`), the `selfClosing` property is being set to `false` instead of `true`.

### Reproduction

```jsx
// Input MDX content
<MyComponent />

// Expected parsed output
{
  type: 'mdxJsxFlowElement',
  name: 'MyComponent',
  selfClosing: true,
  attributes: []
}

// Actual parsed output
{
  type: 'mdxJsxFlowElement',
  name: 'MyComponent',
  selfClosing: false,  // Should be true!
  attributes: []
}
```

### Expected behavior

When a JSX tag uses the self-closing syntax (`/>`), the parser should set `selfClosing: true` on the tag node. This affects how the component is rendered and can cause issues with components that expect to be self-closing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
