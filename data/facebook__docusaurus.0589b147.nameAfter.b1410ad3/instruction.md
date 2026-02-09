# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing when using the `=` character in attribute names. The parser seems to be handling the transition between attribute name and value incorrectly, causing unexpected behavior when processing directives with attributes.

### Reproduction

```markdown
::directive{name=value}
content
::

::directive{attr="quoted value"}
more content
::
```

When parsing directives with attributes that have values assigned using `=`, the attribute structure is not being processed correctly. The issue appears to be related to how the parser handles the state transition after encountering the `=` character following an attribute name.

### Expected behavior

Directives with attributes should be parsed correctly, with proper separation between attribute names and their values. The parser should maintain the correct state transitions when moving from attribute name to initializer to value.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
