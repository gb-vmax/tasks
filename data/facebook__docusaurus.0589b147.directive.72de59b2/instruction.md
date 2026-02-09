# Bug Report

### Describe the bug

I'm encountering an issue with remark-directive where directives are not being parsed correctly. It seems like the text and flow directives aren't working as expected after a recent change.

### Reproduction

When trying to use directives in markdown content, they're not being recognized or processed properly. For example:

```markdown
::container
Some content here
::

:leafDirective
```

The directives should be parsed and transformed, but instead they're being treated as regular text or ignored entirely.

### Expected behavior

Directives should be properly tokenized and parsed according to the remark-directive specification. Both container directives (`::`) and leaf directives (`:`) should work correctly in flow content.

### Additional context

This appears to affect both text-level and flow-level directives. The tokenizer doesn't seem to be registering the directive handlers properly, causing the parser to skip over them.

---
Repository: /testbed
