# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where closing tags with attributes are not being properly validated. It seems like the parser is allowing attributes on closing tags when it shouldn't.

### Reproduction

When parsing MDX content with a closing tag that has attributes, the parser doesn't throw an error as expected:

```jsx
<Component>
  content here
</Component attribute="value">
```

The above should fail with an error message about unexpected attributes in closing tags, but it's not being caught properly.

### Expected behavior

The parser should throw a `VFileMessage` error with the message "Unexpected attribute in closing tag, expected the end of the tag" when encountering attributes on closing JSX tags.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The validation logic for closing tags with attributes doesn't seem to be working correctly anymore.

---
Repository: /testbed
