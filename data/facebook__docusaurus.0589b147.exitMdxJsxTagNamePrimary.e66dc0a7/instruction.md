# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag name parsing. When using JSX tags in MDX files, the tag names are not being extracted correctly, which causes the parsed output to be malformed.

### Reproduction

```jsx
<CustomComponent>
  Some content
</CustomComponent>
```

When parsing the above MDX content, the tag name for `CustomComponent` is not being serialized properly. Instead of getting the actual tag name, it seems like the wrong token is being passed to the serialization function.

### Expected behavior

The parser should correctly extract and store the tag name `CustomComponent` from the JSX syntax. The tag object should have its `name` property set to the string value of the tag identifier.

### Additional context

This appears to affect primary tag names in JSX elements. The tag name extraction logic seems to be using an incorrect reference when serializing the token, leading to unexpected parsing results.

---
Repository: /testbed
