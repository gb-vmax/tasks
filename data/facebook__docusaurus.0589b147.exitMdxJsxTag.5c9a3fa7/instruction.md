# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being handled correctly. When using self-closing tags like `<Component />`, they appear to be treated as regular opening tags instead of self-closing ones, which causes issues with the component tree structure.

### Reproduction

```mdx
<CustomComponent />

Some text here

<AnotherComponent>
  Content
</AnotherComponent>
```

When parsing the above MDX content, self-closing tags don't properly close themselves and interfere with subsequent elements in the document.

### Expected behavior

Self-closing JSX tags should be recognized and handled as complete elements without requiring a separate closing tag. The parser should correctly identify `<Component />` as a self-closing tag and not expect a `</Component>` closing tag later in the document.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
