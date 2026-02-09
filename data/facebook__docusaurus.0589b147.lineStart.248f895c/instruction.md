# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in remark-directive. When parsing container directives, the parser seems to be handling the closing fence incorrectly, causing content that should be inside the container to be treated differently than expected.

### Reproduction

```markdown
:::note
This is a container directive with some content.
It should properly handle multiple lines.
:::
```

When parsing the above markdown with remark-directive, the container content doesn't seem to be processed correctly. The closing fence detection appears to be inverted - it's triggering when it shouldn't and not triggering when it should.

### Expected behavior

The parser should correctly identify the opening `:::note` and closing `:::` fences, with all content between them being treated as the container's content. The closing fence should properly terminate the container directive.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
