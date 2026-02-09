# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing in MDX content. When using JSX tags in my MDX files, the parser seems to be generating an incorrect token structure at the end of tags. This appears to be affecting the proper closure of tag markers.

### Reproduction

```jsx
<div>
  <span>Hello</span>
</div>
```

When parsing the above MDX content, the tag end markers are not being properly sequenced. The issue occurs specifically when the closing `>` of a tag is processed.

### Expected behavior

JSX tags should be parsed correctly with proper token entry/exit ordering. The tag marker should be closed before the tag type itself exits, and there shouldn't be any additional tag type entries after the marker exits.

### Additional context

This seems to affect all JSX tags in MDX, both self-closing and regular closing tags. The token structure appears to be malformed which could cause issues with downstream processors that rely on the correct AST structure.

---
Repository: /testbed
