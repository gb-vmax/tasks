# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where attributes in opening tags are being incorrectly rejected with an error message "Unexpected attribute in closing tag, expected the end of the tag".

### Reproduction

When trying to parse MDX content with JSX tags that have attributes, the parser throws an error even though the attributes are on opening tags, not closing tags.

```jsx
<Component attribute="value">
  content
</Component>
```

The above valid MDX should parse correctly, but instead throws an error about unexpected attributes in closing tags, even though the attribute is clearly on the opening tag.

### Expected behavior

Opening tags with attributes should be parsed successfully without errors. The error message about attributes in closing tags should only appear when attributes are actually present on closing tags (e.g., `</Component attribute="value">`), which is invalid syntax.

### Additional context

This seems to affect any MDX JSX component that uses attributes on opening tags. The error message itself is also confusing since it mentions "closing tag" when the attribute is actually on an opening tag.

---
Repository: /testbed
