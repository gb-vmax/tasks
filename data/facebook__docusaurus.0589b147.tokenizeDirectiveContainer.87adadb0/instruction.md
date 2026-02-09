# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing in remark-directive. It seems like the minimum sequence length for container directives has changed, and now directives that should be valid are not being recognized properly.

### Reproduction

```markdown
::note
This is a container directive
::
```

When parsing the above markdown with remark-directive, the container directive is not being recognized. It appears that the parser now requires a different number of colons than before.

Additionally, there seems to be an issue with lazy continuation lines inside directive containers - content that should be part of the directive is being treated incorrectly, causing the directive structure to break.

### Expected behavior

Container directives with two colons (`::`) should be parsed correctly as they were in previous versions. The content inside the directive should be properly recognized as part of the directive block, not as separate lazy continuation lines.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This appears to be a regression from the previous behavior. Any help would be appreciated!

---
Repository: /testbed
