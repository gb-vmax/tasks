# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute parsing where the `>` character is not being properly recognized as the end of a tag when it appears after an attribute name. This causes the parser to incorrectly continue parsing instead of closing the tag.

### Reproduction

```jsx
<Component attribute>
  content
</Component>
```

When parsing JSX tags with attributes that don't have values (boolean attributes), the closing `>` bracket is not recognized correctly. The parser seems to treat it as part of the attribute name or continues parsing when it should stop.

This also affects cases like:
```jsx
<div className="test" disabled>Hello</div>
```

The `>` character should signal the end of the tag opening, but it's being handled incorrectly.

### Expected behavior

The parser should recognize `>` (character code 62) as a valid terminator for attribute names and properly close the tag opening. Boolean attributes (attributes without values) should be parsed correctly with the tag closing immediately after the attribute name.

### Additional context

This appears to be related to how character codes are being checked in the attribute name parsing logic. The comparison operators might not be handling the boundary conditions correctly for special characters like `>` and `=`.

---
Repository: /testbed
