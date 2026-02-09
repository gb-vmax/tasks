# Bug Report

### Describe the bug

I'm experiencing an issue with JSX element depth calculation in MDX rendering. It seems like the depth counter is off by one, causing nested JSX elements to render with incorrect indentation or structure.

### Reproduction

When working with nested MDX JSX flow elements, the depth calculation appears to be incorrect. For example:

```jsx
<Component>
  <NestedComponent>
    <DeeplyNestedComponent />
  </NestedComponent>
</Component>
```

The depth inference seems to be starting from the wrong initial value, which affects how nested components are processed and rendered.

### Expected behavior

The depth calculation should accurately reflect the nesting level of JSX elements, starting from 0 for the root level and incrementing for each nested level. Currently, it appears to be off by one level.

### System Info

- remark-mdx version: 3.0.0
- Using with Jest vendor bundle

---
Repository: /testbed
