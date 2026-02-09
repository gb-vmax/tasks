# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in MDX files. It seems like the parser is incorrectly handling the opening sequence of fenced code blocks, which is causing problems with the event structure.

### Reproduction

When parsing MDX content with fenced code blocks, the events are being entered in the wrong order. This affects how the code fence metadata is processed.

```mdx
```js
console.log('test');
```
```

The parser appears to be looking at the wrong event in the events array (off by one) and also entering the fence-related events in an incorrect sequence.

### Expected behavior

The parser should:
1. Correctly identify the line prefix by looking at the right event in the history
2. Enter the code fence events in the proper order: `codeFenced` → `codeFencedFence` → `codeFencedFenceSequence`

### Additional context

This seems to be related to how the tokenizer processes the opening sequence of code fences. The event ordering is critical for proper parsing and any deviation causes downstream issues with code block rendering.

---
Repository: /testbed
