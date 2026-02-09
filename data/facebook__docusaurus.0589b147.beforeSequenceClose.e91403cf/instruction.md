# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX parsing. When I try to use code fences (triple backticks), the closing fence is not being recognized properly and the code block doesn't close as expected.

### Reproduction

```markdown
\`\`\`javascript
const example = 'test';
\`\`\`
```

When parsing this MDX content, the closing fence sequence is not matched correctly. The parser seems to be rejecting valid closing fences and treating them as part of the code content instead.

### Expected behavior

The closing fence (triple backticks) should be properly detected and close the code block. The code block should render correctly with the content between the opening and closing fences.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently - code fences were working fine before. Any help would be appreciated!

---
Repository: /testbed
