# Bug Report

### Describe the bug

I'm encountering an issue with closing JSX tags in MDX files. When I try to use a closing tag with a valid name, I'm getting an unexpected error about the tag name not being valid.

### Reproduction

```mdx
<div>
  Some content here
</div>
```

When parsing this MDX, the closing `</div>` tag is not being recognized properly. The parser seems to reject valid closing tag names that should be accepted.

### Expected behavior

The closing tag should be parsed correctly and the MDX should compile without errors. Valid JSX tag names (starting with letters, `$`, or `_`) should be accepted in closing tags just like they are in opening tags.

### Additional context

This seems to affect all closing tags with standard names. The opening tags work fine, but the closing tags fail validation even though they use the exact same naming convention.

---
Repository: /testbed
