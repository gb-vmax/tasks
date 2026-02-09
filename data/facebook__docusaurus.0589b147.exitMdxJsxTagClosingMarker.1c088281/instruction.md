# Bug Report

### Describe the bug

I'm experiencing an issue with self-closing JSX tags in MDX content. When using self-closing tags (like `<Component />`), they are not being parsed correctly and seem to be treated as if they have a closing marker set to `false` instead of `true`.

### Reproduction

```mdx
<MyComponent />
```

When parsing the above MDX content, the JSX tag's `close` property is incorrectly set to `false` even though it's a self-closing tag. This causes problems when the parsed AST is used for further processing or rendering.

### Expected behavior

Self-closing JSX tags should have their `close` property set to `true` to correctly indicate that they are self-closing. The parser should recognize the `/>` closing marker and set the appropriate flag.

### Additional context

This appears to be related to the `exitMdxJsxTagClosingMarker` function in the MDX parser. The behavior changed recently and is affecting how self-closing components are handled in our MDX documents.

---
Repository: /testbed
