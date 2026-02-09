# Bug Report

### Describe the bug

I'm experiencing an issue with parsing directives in markdown content. When a directive is placed after certain block elements, it's not being recognized correctly and the parser seems to be treating it as regular text instead of processing it as a directive.

### Reproduction

```markdown
Some paragraph content here.

::directive-name
This should be parsed as a directive
::
```

When parsing the above markdown, the directive is not being processed correctly. It appears that the lazy line checking logic is evaluating the wrong line, causing valid directives to be skipped.

### Expected behavior

The directive should be properly recognized and parsed regardless of what content precedes it. The parser should correctly identify directive boundaries and process them as directive nodes in the AST.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have started happening recently and is affecting our markdown processing pipeline. Any help would be appreciated!

---
Repository: /testbed
