# Bug Report

### Describe the bug

I'm encountering an issue with closing tags in MDX content. When I have properly nested JSX tags, I'm getting an error message saying "Unexpected closing slash `/` in tag, expected an open tag first" even though the tags are correctly structured.

### Reproduction

```jsx
<Component>
  <NestedComponent />
</Component>
```

When parsing the above MDX content, the self-closing `NestedComponent` tag triggers an error about an unexpected closing slash, but the syntax is valid JSX.

### Expected behavior

The parser should correctly handle self-closing tags within other JSX elements without throwing errors. The closing slash in `<NestedComponent />` is valid syntax and should be parsed successfully.

### Additional context

This seems to happen specifically when there's a self-closing tag nested inside another component. Simple self-closing tags at the root level work fine, but nesting causes the parser to incorrectly identify the closing slash as problematic.

---
Repository: /testbed
