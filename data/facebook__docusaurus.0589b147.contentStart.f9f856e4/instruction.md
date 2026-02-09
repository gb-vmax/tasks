# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the parser seems to be handling null/non-null codes incorrectly. When I try to use container directives in my markdown, the parsing behavior is not what I expect.

### Reproduction

```markdown
:::note
This is a container directive
:::
```

When parsing the above markdown with container directives, the content doesn't seem to be processed correctly. The parser appears to exit early or not enter the content state properly.

### Expected behavior

The container directive should properly parse the content between the opening `:::` and closing `:::` markers. The content should be entered and processed as `directiveContainerContent`.

### Additional context

This seems related to how the tokenizer handles the transition from the container start to the content. The logic for checking null vs non-null codes might be inverted, causing the parser to exit when it should continue or vice versa.

---
Repository: /testbed
