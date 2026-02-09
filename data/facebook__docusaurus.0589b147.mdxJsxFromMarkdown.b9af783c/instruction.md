# Bug Report

### Describe the bug
I'm experiencing an issue with JSX tag validation in MDX files. When I have properly matched opening and closing JSX tags, I'm getting an error about "unexpected closing tag" even though the tags are correctly paired.

### Reproduction
```mdx
<CustomComponent>
  Some content here
</CustomComponent>
```

When parsing this MDX content, I get an error message like:
```
Unexpected closing tag `</CustomComponent>`, expected corresponding closing tag for `<CustomComponent>`
```

This is confusing because the closing tag DOES match the opening tag. The error message suggests there's a mismatch when there isn't one.

### Expected behavior
Valid JSX with matching opening and closing tags should parse without errors. The parser should only throw an error when tags are actually mismatched (e.g., `<Foo>` closed with `</Bar>`).

### Additional context
This seems to have started happening recently. Previously, properly matched JSX tags would parse correctly without any issues. Now even the most basic JSX components are throwing validation errors.

---
Repository: /testbed
