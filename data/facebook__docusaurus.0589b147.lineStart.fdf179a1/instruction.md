# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the content is not being parsed correctly. It seems like the parser is terminating prematurely or not properly handling the content inside container directives.

### Reproduction

```markdown
:::note
This is some content inside a container directive.
It should be parsed as part of the container.
:::
```

When parsing this markdown with remark-directive, the content inside the container directive either gets cut off early or the closing fence is not recognized properly. The directive container appears to end before it should.

### Expected behavior

The entire content between the opening `:::note` and closing `:::` should be captured as part of the directive container content. The parser should correctly identify where the container starts and ends, including all lines in between.

### Additional context

This might be related to how null codes are being handled in the line parsing logic. The container content seems to be affected when there are multiple lines or specific line ending scenarios.

---
Repository: /testbed
