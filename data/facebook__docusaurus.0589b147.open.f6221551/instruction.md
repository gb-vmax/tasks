# Bug Report

### Describe the bug
When parsing markdown image syntax, the parser is accepting invalid input that should be rejected. Specifically, when an image marker `![` is not followed by the expected opening bracket `[`, the parser continues processing instead of returning an error.

### Reproduction
```markdown
![test
```

or 

```markdown
!test
```

The parser should reject these malformed image references, but instead it's treating them as valid and continuing to parse.

### Expected behavior
The parser should only accept properly formatted image syntax like `![alt text](url)` or `![alt][ref]`. When the opening `![` is not followed by a proper bracket structure, it should fail to tokenize as an image and fall back to treating it as plain text.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
