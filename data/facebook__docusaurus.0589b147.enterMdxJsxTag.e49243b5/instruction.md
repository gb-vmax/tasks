# Bug Report

### Describe the bug

I'm experiencing an issue with nested JSX tags in MDX content. When using JSX components inside other JSX components, the inner component's attributes and properties seem to get mixed up or inherited from the outer component incorrectly.

### Reproduction

```mdx
<OuterComponent name="outer" color="blue">
  <InnerComponent name="inner" color="red" />
</OuterComponent>
```

When parsing this structure, the inner component appears to be picking up properties from the outer component instead of maintaining its own separate attributes. The `name` and other attributes of the inner component are not being handled correctly.

### Expected behavior

Each nested JSX component should maintain its own independent set of attributes and properties. The inner component should have `name="inner"` and `color="red"`, while the outer component should have `name="outer"` and `color="blue"`. They shouldn't interfere with each other.

### Additional context

This seems to happen specifically when JSX tags are nested. Self-closing tags at the same level work fine, but as soon as you nest one component inside another, the attribute handling breaks down.

---
Repository: /testbed
