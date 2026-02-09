# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX where the order of events seems to be incorrect. When parsing fenced code blocks (the triple backtick blocks), the tokenizer appears to be emitting events in the wrong sequence.

### Reproduction

```markdown
```js
const example = 'test';
```
```

When this MDX content is parsed, the event emission order for the code fence doesn't match what's expected. The `codeFenced` and `codeFencedFence` events are being entered in the wrong order.

### Expected behavior

The tokenizer should emit events in the correct sequence:
1. Enter `codeFenced`
2. Enter `codeFencedFence` 
3. Enter `codeFencedFenceSequence`

But it seems like steps 1 and 2 are swapped.

Additionally, there might be an issue with how the `initialPrefix` is being calculated - it's looking at the wrong event in the events array to determine line prefix length.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing downstream issues with code block rendering and formatting. Any help would be appreciated!

---
Repository: /testbed
