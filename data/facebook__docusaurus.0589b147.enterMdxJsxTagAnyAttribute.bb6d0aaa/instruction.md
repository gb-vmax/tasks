# Bug Report

### Describe the bug

I'm encountering an issue when parsing MDX JSX tags with attributes. The parser is throwing unexpected errors about missing `mdxJsxTag` data when processing valid JSX opening tags with attributes.

### Reproduction

```jsx
<Component attribute="value">
  Content here
</Component>
```

When trying to parse the above MDX content, I get an error saying `expected 'mdxJsxTag'` is not met, even though this is a valid JSX opening tag with an attribute.

### Expected behavior

The parser should correctly handle JSX opening tags with attributes without throwing errors. The `mdxJsxTag` should be present in the context when entering attribute parsing for opening tags.

### Additional context

This seems to be affecting the `enterMdxJsxTagAnyAttribute` function during the markdown-to-AST transformation process. The error occurs specifically when attributes are being parsed on opening tags.

---
Repository: /testbed
