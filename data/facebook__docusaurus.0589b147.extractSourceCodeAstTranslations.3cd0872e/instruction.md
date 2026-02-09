# Bug Report

### Describe the bug

I'm experiencing an issue with the `<Translate>` component where it's not properly handling JSX content with whitespace. When I have a `<Translate>` component with text content that includes newlines or formatting, it seems to be incorrectly filtered out and treated as empty.

### Reproduction

```jsx
<Translate id="my.translation">
  Some text content
</Translate>
```

When using the component like above with text that has whitespace/newlines around it (which is pretty common with JSX formatting), the translation extraction doesn't work as expected. The content appears to be filtered out when it shouldn't be.

### Expected behavior

The `<Translate>` component should correctly extract translation strings even when there's whitespace or newlines in the JSX content. JSX formatting with proper indentation is standard practice and shouldn't affect how translations are processed.

### Additional context

This seems related to how the translation extractor filters JSX text nodes. It looks like the logic for determining whether a text node is "empty" or "useless" might be inverted, causing actual content to be removed instead of empty whitespace-only nodes.

---
Repository: /testbed
