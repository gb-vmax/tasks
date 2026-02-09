# Bug Report

### Describe the bug

I'm encountering an issue with directive leaf parsing where directives at the end of a document or before line breaks are not being recognized properly. The parser seems to be rejecting valid directive syntax that should be accepted.

### Reproduction

```markdown
This is a test :directive[content]
```

When this is parsed, the directive is not being processed correctly. It appears that directives followed by EOF or newlines are being treated as invalid syntax, even though they should be valid according to the directive specification.

### Expected behavior

Directive leaf syntax like `:directive[content]` should be properly recognized and parsed when:
- It appears at the end of a document (followed by EOF/null)
- It's followed by a line ending

The parser should accept these as valid directives and process them accordingly.

### Additional context

This seems to affect any inline directive that appears at the end of a line or document. The directive syntax itself is correct, but the tokenizer is rejecting it during the parsing phase.

---
Repository: /testbed
