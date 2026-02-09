# Bug Report

### Describe the bug

I'm encountering an issue with directive attributes when they don't have explicit values assigned. The parser seems to be handling attribute names incorrectly, which causes problems when processing directives with boolean-style attributes.

### Reproduction

```markdown
::directive{attr1 attr2="value"}
content
::
```

When parsing a directive like the one above where `attr1` has no explicit value (boolean attribute), the attribute structure gets corrupted. The attribute name is being stored incorrectly in the internal data structure.

### Expected behavior

Attributes without values should be properly parsed and stored. The parser should handle both:
- Attributes with values: `attr="value"`
- Attributes without values: `attr`

Both should result in a consistent and usable attribute structure.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
