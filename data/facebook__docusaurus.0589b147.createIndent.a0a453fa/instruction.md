# Bug Report

### Describe the bug

I'm experiencing an issue with MDX code formatting where the indentation levels are incorrect. Nested elements appear to be indented one level less than they should be, making the output look improperly formatted.

### Reproduction

When processing MDX content with nested JSX elements, the indentation doesn't match the expected nesting depth:

```jsx
<div>
  <Component>
    <NestedComponent>
      Content here
    </NestedComponent>
  </Component>
</div>
```

The generated output has incorrect indentation - everything seems shifted one level to the left compared to what it should be.

### Expected behavior

Each nested level should be properly indented according to its depth in the tree. A component at depth 2 should have 2 levels of indentation, not 1.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
