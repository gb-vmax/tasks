# Bug Report

### Describe the bug

I'm encountering an issue with link parsing in MDX content. When using standard markdown link syntax `[text](url)`, the parser seems to get stuck or doesn't properly complete the link tokenization process. The link marker tokens are being created but the flow doesn't continue to the next step.

### Reproduction

```markdown
This is a [link](https://example.com) in my MDX file.
```

When processing this MDX content, the link parsing appears to hang or fail to complete. The opening bracket `[` is consumed but the parser doesn't proceed to handle the rest of the link syntax correctly.

### Expected behavior

The link should be properly tokenized and parsed, with the flow continuing through the `after` function to validate and complete the link structure. Links should render correctly in the output.

### Additional context

This seems to affect basic markdown links. The tokenizer enters the label marker but doesn't return the proper continuation, so subsequent characters in the link aren't processed as expected.

---
Repository: /testbed
