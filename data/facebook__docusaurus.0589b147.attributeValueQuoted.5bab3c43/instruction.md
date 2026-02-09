# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where quoted attribute values in JSX tags are not being parsed correctly. The parser seems to be mishandling the state transitions when processing attribute values enclosed in quotes.

### Reproduction

```mdx
<Component name="hello world" />
```

When parsing JSX tags with quoted attribute values like the above, the attribute value doesn't get properly extracted. It appears that the parser is returning to the wrong state or not properly closing the value token before transitioning.

### Expected behavior

The parser should correctly tokenize the quoted attribute value and maintain proper state transitions. The attribute value `"hello world"` should be fully captured and the parser should continue processing the rest of the tag normally.

### Additional context

This seems to affect any JSX-style tags in MDX documents that use quoted attribute values. The issue appears to be in the attribute value parsing logic where the state machine transitions are occurring.

---
Repository: /testbed
