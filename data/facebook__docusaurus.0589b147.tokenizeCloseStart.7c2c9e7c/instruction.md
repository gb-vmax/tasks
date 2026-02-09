# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the closing fence is not being recognized correctly. When using code fences with backticks or tildes, blocks that should close properly are being left open, causing the rest of the document to be treated as code.

### Reproduction

```markdown
# My Document

\`\`\`js
const x = 1;
\`\`\`

This text should be normal markdown but is being treated as code.
```

The closing fence with the same number of backticks as the opening fence doesn't properly close the code block. This causes everything after the intended code block to be parsed as part of the code content instead of regular markdown.

### Expected behavior

The code block should close when encountering a fence with the same or greater number of fence characters (backticks or tildes) as the opening fence. Content after the closing fence should be parsed as normal markdown.

### Additional context

This seems to affect all fenced code blocks regardless of the fence character used (backticks or tildes). The parser appears to require MORE fence characters to close than to open, which breaks standard markdown behavior where equal length fences should work.

---
Repository: /testbed
