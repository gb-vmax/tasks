# Bug Report

### Describe the bug

I'm encountering an issue with JSX tag matching in MDX files. When I have properly matched opening and closing tags, I'm getting an error saying the tags don't match, even though they clearly do.

### Reproduction

```mdx
<CustomComponent>
  Some content here
</CustomComponent>
```

This throws an error like:
```
Unexpected closing tag `</CustomComponent>`, expected corresponding closing tag for `<CustomComponent>` (1:1-1:17)
```

The error message doesn't make sense - it's complaining that the closing tag doesn't match, but then says it expects exactly that same closing tag.

### Expected behavior

The parser should recognize that `</CustomComponent>` is the correct closing tag for `<CustomComponent>` and not throw an error. Properly matched JSX tags should parse without issues.

### Additional context

This seems to have started happening recently. Previously, the same MDX content would parse fine. The error appears even with the simplest possible JSX component with matching opening and closing tags.

---
Repository: /testbed
