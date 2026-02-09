# Bug Report

### Describe the bug

I'm encountering an issue with JSX tag name parsing in MDX content. When using primary JSX tag names (like `<Button>` or `<div>`), the parser seems to be failing to properly extract and assign the tag name. This appears to be causing problems with rendering JSX components in MDX files.

### Reproduction

```mdx
# My Document

<Button variant="primary">
  Click me
</Button>

<CustomComponent />
```

When parsing the above MDX content, the JSX tag names are not being correctly identified. The parser appears to be looking in the wrong location for tag data, which prevents proper component resolution.

### Expected behavior

JSX tags in MDX should be correctly parsed with their names properly extracted and assigned. Components like `<Button>` and `<CustomComponent>` should be recognized and rendered appropriately.

### Additional context

This seems to affect all primary JSX tag names (both HTML elements and custom components). Member expressions (like `<Foo.Bar>`) might be working differently, but the basic tag name extraction is definitely broken.

---
Repository: /testbed
