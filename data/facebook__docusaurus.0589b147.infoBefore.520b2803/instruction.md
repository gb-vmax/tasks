# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the parser seems to be emitting events in the wrong order. When parsing code blocks with info strings (like language identifiers), the `codeFencedFence` exit event appears to be happening at the wrong time, which breaks the expected token structure.

### Reproduction

```markdown
```javascript
const x = 1;
```
```

When this gets parsed, the token events don't follow the expected sequence. It looks like the fence closing is happening before the info string is processed, which causes downstream issues with syntax highlighting and code block metadata.

### Expected behavior

The parser should emit events in this order:
1. Enter `codeFencedFence`
2. Process fence sequence
3. Exit `codeFencedFence`
4. Enter `codeFencedFenceInfo`
5. Process info string
6. Exit `codeFencedFenceInfo`

Currently it seems like step 3 is happening after step 4, which breaks the token hierarchy.

### System Info
- MDX version: 3.0.0
- This affects code blocks with language identifiers (info strings)

---
Repository: /testbed
