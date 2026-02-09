# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression handling after a recent update. When using inline MDX expressions (text expressions) in my documents, they're not being processed correctly. The expressions appear to be treated differently than they should be, causing rendering issues.

### Reproduction

```mdx
Here is some text with an inline expression: {someVariable}

And here is a block expression:

{
  someBlockExpression
}
```

When processing this MDX content, the inline text expressions don't render properly. Block expressions seem to work fine, but the inline ones are broken.

### Expected behavior

Both inline (text) and block (flow) MDX expressions should be handled correctly and render as expected. The text expressions should be processed the same way they were in previous versions.

### Additional context

This seems to have started happening recently. I noticed that inline expressions in particular are affected - they either don't render at all or throw errors during processing. Block-level expressions still work as expected.

---
Repository: /testbed
