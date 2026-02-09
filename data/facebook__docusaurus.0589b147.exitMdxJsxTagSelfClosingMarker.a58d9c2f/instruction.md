# Bug Report

### Describe the bug

I'm experiencing an issue with self-closing JSX tags in MDX files. When using self-closing tags like `<Component />`, the parser doesn't correctly set the `selfClosing` property on the tag object. Instead of setting it on the tag itself, it appears to be set on a different object.

### Reproduction

```jsx
// In an MDX file
<MyComponent />
```

When parsing this, the expected behavior is that the tag object should have `selfClosing: true`, but this property is not being set correctly on the tag.

### Expected behavior

Self-closing JSX tags should have their `selfClosing` property set to `true` on the tag object itself. This is needed for proper rendering and transformation of MDX content.

### System Info
- remark-mdx version: 3.0.0

This seems to have broken recently and is affecting MDX parsing. Any help would be appreciated!

---
Repository: /testbed
