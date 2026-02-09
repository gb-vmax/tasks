# Bug Report

### Describe the bug

After a recent update, MDX content is not being parsed correctly. JSX components within MDX files are no longer recognized, causing them to be rendered as plain text instead of being processed as components.

### Reproduction

Create an MDX file with JSX components:

```mdx
# Hello World

<CustomComponent>
  This should be rendered as a component
</CustomComponent>

Some regular markdown text.
```

When this MDX content is processed, the `<CustomComponent>` tags appear as literal text in the output instead of being parsed and rendered as a JSX component.

### Expected behavior

JSX components embedded in MDX files should be properly parsed and rendered. The `<CustomComponent>` should be recognized as a JSX element and processed accordingly, not treated as plain text.

### Additional context

This appears to have started happening recently. Previously, JSX components in MDX files were working fine. The markdown content itself still renders correctly, but any JSX/component syntax is broken.

---
Repository: /testbed
