# Bug Report

### Describe the bug

When parsing fenced code blocks in MDX, the closing fence sequence is not being properly recognized. The parser seems to be entering the `codeFencedFenceSequence` state at the wrong time, which causes code blocks to not close correctly.

### Reproduction

```markdown
\`\`\`js
const example = 'test';
\`\`\`
```

When the above MDX is parsed, the closing fence (```) is not properly detected and the code block remains open or produces unexpected output.

### Expected behavior

The parser should:
1. Recognize the closing fence sequence when it matches the opening marker
2. Properly close the code block
3. Continue parsing subsequent content correctly

The closing fence should be detected when the marker characters match, and the `codeFencedFenceSequence` state should only be entered when appropriate.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
