# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where self-closing tags are not being properly recognized. When using self-closing JSX syntax in MDX files, the parser seems to be setting the wrong property on the tag object.

### Reproduction

```mdx
<MyComponent />
```

When this MDX is parsed, the tag object should have a `close` property set to `true` for self-closing tags, but it appears the property name has changed or is being set incorrectly.

This affects any MDX content that uses self-closing JSX tags, which is a very common pattern in React/JSX.

### Expected behavior

Self-closing JSX tags should be properly identified with the correct property so that downstream processing can distinguish between:
- `<Component />` (self-closing)
- `<Component></Component>` (with separate closing tag)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
