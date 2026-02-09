# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where attributes in opening tags are being incorrectly rejected. When I try to use attributes on opening JSX tags in my MDX files, I'm getting an error message about "Unexpected attribute in closing tag" even though I'm clearly using an opening tag, not a closing one.

### Reproduction

```mdx
<MyComponent prop="value">
  Content here
</MyComponent>
```

When parsing the above MDX, the parser throws an error:
```
Unexpected attribute in closing tag, expected the end of the tag
```

This happens with any JSX component that has attributes on the opening tag. Self-closing tags without attributes seem to work fine, but as soon as I add any prop to an opening tag, it fails.

### Expected behavior

The parser should accept attributes on opening JSX tags without throwing errors. Attributes should only be rejected on closing tags (e.g., `</MyComponent prop="invalid">`), not on opening tags.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking my ability to use MDX components with props. Any help would be appreciated!

---
Repository: /testbed
