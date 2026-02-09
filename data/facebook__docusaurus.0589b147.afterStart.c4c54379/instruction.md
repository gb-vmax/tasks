# Bug Report

### Describe the bug
Empty directive labels are not being parsed correctly. When I use a directive with an empty label like `::directive[]`, the parser seems to be immediately exiting the string type token without properly handling the content, which breaks the directive structure.

### Reproduction
```markdown
::directive[]

::directive[some text]
```

The first directive with empty brackets `[]` doesn't parse as expected. The parser appears to enter and immediately exit the string type, which causes issues with the token structure.

### Expected behavior
Empty directive labels should be handled the same way as labels with content - the parser should properly process the opening bracket, recognize there's no content, and then handle the closing bracket correctly.

Both `::directive[]` and `::directive[some text]` should parse successfully and maintain proper token hierarchy.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
