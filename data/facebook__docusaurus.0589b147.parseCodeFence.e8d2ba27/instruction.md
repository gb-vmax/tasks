# Bug Report

### Describe the bug

I'm experiencing an issue with code fence detection in markdown files. It seems like the parser is not correctly identifying when code blocks are opened or closed, which causes links inside code blocks to be incorrectly processed.

### Reproduction

When I have markdown content like this:

```markdown
Some text before

```js
const link = "[example](https://example.com)";
```

Some text after with [real link](https://example.com)
```

The link inside the code block is being treated as an actual markdown link and gets processed, even though it should be ignored since it's inside a code fence.

Also noticing weird behavior with code fences that have content on the same line:

```markdown
``` inline code fence
[this link](https://test.com) should not be processed
```

### Expected behavior

Links that appear inside code blocks (between triple backticks or tildes) should be treated as literal text and not processed as markdown links. The code fence parser should correctly determine when a fence is opening vs closing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
