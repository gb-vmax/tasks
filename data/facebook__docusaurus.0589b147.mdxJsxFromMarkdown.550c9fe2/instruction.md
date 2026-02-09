# Bug Report

### Describe the bug

When using JSX tags in MDX content, I'm getting an error about mismatched closing tags even though my tags are properly matched. The error message says it's expecting a closing tag, but the tags are correctly nested and closed.

### Reproduction

```mdx
<Component>
  <NestedComponent>
    Content here
  </NestedComponent>
</Component>
```

This throws an error like:
```
Unexpected closing tag `</NestedComponent>`, expected corresponding closing tag for `<Component>` ...
```

Even though the tags are properly nested and closed in the correct order.

### Expected behavior

The MDX parser should correctly recognize properly nested and closed JSX tags without throwing errors about mismatched tags.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
