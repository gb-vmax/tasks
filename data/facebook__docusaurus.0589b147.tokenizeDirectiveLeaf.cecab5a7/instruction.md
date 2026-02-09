# Bug Report

### Describe the bug

I'm having trouble with directive leaf syntax parsing. It seems like the parser is not correctly recognizing directive leaf markers in my markdown files. The directives that should be parsed are being ignored or not processed at all.

### Reproduction

```markdown
:directiveName[label text]{key=value}
```

When I try to parse markdown with directive leaf syntax like the above, it doesn't work as expected. The directive is not being recognized by the parser.

### Expected behavior

The parser should correctly identify and tokenize directive leaf syntax starting with `:` followed by the directive name, optional label in brackets, and optional attributes in curly braces.

### Additional context

This seems to have broken recently. I'm using remark-directive for parsing custom directives in markdown documents, and the leaf directives are a critical part of my workflow. Container and text directives might be affected too, but I've specifically noticed issues with leaf directives.

---
Repository: /testbed
