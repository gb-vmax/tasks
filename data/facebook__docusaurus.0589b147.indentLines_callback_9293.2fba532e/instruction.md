# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow elements not being properly serialized. When rendering MDX content that contains JSX flow elements (block-level JSX), the indentation and formatting is incorrect in the output.

### Reproduction

```jsx
const mdxContent = `
# Heading

<MyComponent>
  <NestedComponent>
    Content here
  </NestedComponent>
</MyComponent>

More content
`

// Process this MDX content
// The JSX flow elements lose their proper formatting
```

When I process MDX documents containing block-level JSX components (flow elements), they're not being handled correctly. The indentation seems off and blank lines are getting extra indentation added to them.

### Expected behavior

JSX flow elements should maintain their proper structure and indentation when serialized. Blank lines within JSX blocks should not have indentation added, and the overall formatting should be preserved correctly.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The output formatting for nested JSX components in MDX files is not what I'd expect.

---
Repository: /testbed
