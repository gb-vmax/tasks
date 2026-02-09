# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence sequence isn't being recognized correctly. When I have a code block with a closing fence that has MORE backticks than the opening fence, it's not properly closed and the parser seems to continue treating subsequent content as part of the code block.

### Reproduction

```markdown
````js
const example = 'test';
`````

Some text that should be outside the code block
```

In this case, the opening fence has 4 backticks but the closing fence has 5 backticks. According to the CommonMark spec, a closing fence should have at least as many backticks as the opening fence, so this should successfully close the code block.

### Expected behavior

The code block should be properly closed when the closing fence has MORE characters than the opening fence (not just equal). The text after the closing fence should be parsed as regular content, not as part of the code block.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
