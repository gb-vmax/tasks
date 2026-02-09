# Bug Report

### Describe the bug

I'm encountering an issue when parsing MDX JSX tags with attributes. It seems like the parser is now incorrectly throwing errors for valid opening tags that have attributes, while at the same time not catching errors for closing tags with attributes (which should be invalid).

### Reproduction

```mdx
<MyComponent foo="bar" />
```

When trying to parse the above MDX content, I'm getting an unexpected error about the attribute. This used to work fine before.

Also, this invalid syntax doesn't throw an error anymore:

```mdx
<MyComponent></MyComponent foo="invalid">
```

The closing tag with an attribute should be rejected but it's being accepted now.

### Expected behavior

- Opening tags with attributes should parse successfully without errors
- Self-closing tags with attributes should parse successfully without errors  
- Closing tags with attributes should throw an error with message "Unexpected attribute in closing tag, expected the end of the tag"

### Additional context

This seems to have started happening recently. The validation logic for JSX tag attributes appears to be inverted - it's rejecting valid cases and accepting invalid ones.

---
Repository: /testbed
