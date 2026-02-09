# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the closing fence is not being recognized correctly. When I have a code block with a closing fence that has the exact same number of backticks as the opening fence, the code block doesn't close properly.

### Reproduction

```markdown
````js
const example = 'test';
````
```

The closing fence with 4 backticks should close the code block that was opened with 4 backticks, but it's not working as expected. The parser seems to require more backticks in the closing fence than the opening fence.

### Expected behavior

A fenced code block should close when the closing fence has at least the same number of fence characters (backticks or tildes) as the opening fence. According to the CommonMark spec, the closing fence needs to have at least as many characters as the opening fence, not strictly more.

For example:
- Opening with ``` should close with ``` or more
- Opening with ```` should close with ```` or more

Currently it seems like the closing fence needs to have MORE characters than the opening fence, which is incorrect.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
