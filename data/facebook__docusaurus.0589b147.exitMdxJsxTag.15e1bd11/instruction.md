# Bug Report

### Describe the bug

MDX JSX tags with matching opening and closing tags are being incorrectly flagged as mismatched. When I use properly paired JSX tags in my MDX content, I'm getting an error saying "Unexpected closing tag" even though the tags match perfectly.

### Reproduction

```mdx
<CustomComponent>
  Some content here
</CustomComponent>
```

When parsing this MDX, an error is thrown:
```
Unexpected closing tag `</CustomComponent>`, expected corresponding closing tag for `<CustomComponent>` (line:col)
```

The opening and closing tags clearly match, but the parser is treating them as if they don't.

### Expected behavior

The MDX parser should successfully parse matching opening and closing tags without throwing an error. The above code should work without any issues since the tag names are identical.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
