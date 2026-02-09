# Bug Report

### Describe the bug

When using MDX JSX tags with attributes in closing tags, the parser is throwing an error in the wrong scenario. It seems like the validation logic for detecting attributes in closing tags is inverted - it's throwing an error when attributes are found in **opening** tags instead of closing tags.

### Reproduction

```jsx
// This should work fine but throws an error
<Component attribute="value">
  content
</Component>

// Meanwhile, this invalid syntax (attribute in closing tag) is not being caught
<Component>
  content
</Component attribute="value">
```

The error message says "Unexpected attribute in closing tag, expected the end of the tag" but it's appearing for valid opening tags with attributes.

### Expected behavior

- Opening tags with attributes should be parsed successfully
- Closing tags with attributes should throw the error message about unexpected attributes
- The validation should correctly distinguish between opening and closing tags

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
