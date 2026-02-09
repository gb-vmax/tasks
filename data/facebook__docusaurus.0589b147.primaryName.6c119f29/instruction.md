# Bug Report

### Describe the bug

I'm encountering an issue with JSX tag parsing in MDX content. When using a self-closing JSX tag with a `>` character at the end of the tag name, the parser fails to properly recognize it and throws an error instead of treating it as the closing bracket of the tag.

### Reproduction

```jsx
<Component>
  content
</Component>
```

When the tag name ends and is immediately followed by `>`, the parser doesn't handle it correctly. This seems to affect basic JSX syntax that should be valid.

### Expected behavior

The parser should recognize `>` as the closing bracket of the opening tag and proceed to parse the content normally. Standard JSX syntax like `<Component>` should work without issues.

### Additional context

This appears to be related to how the parser validates characters that can appear after a tag name. The `>` character should be treated as a valid tag terminator, not as part of the name validation logic.

---
Repository: /testbed
