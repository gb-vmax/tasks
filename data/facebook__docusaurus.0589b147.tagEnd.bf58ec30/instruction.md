# Bug Report

### Describe the bug

After a recent update, JSX tag closing markers are not being properly tokenized in MDX files. The tag marker events appear to be emitted in the wrong order, causing the parser to produce incorrect token structures.

### Reproduction

```jsx
// Simple JSX tag in MDX
<div>content</div>
```

When parsing this, the tokenizer should enter and exit the tag marker (`>`) correctly, but instead the events are being fired out of sequence. This affects the token tree structure and can cause issues with downstream processors that rely on proper event ordering.

### Expected behavior

The tag end marker should be consumed between entering and exiting the marker type. The event sequence should be:
1. Enter tag marker
2. Consume the `>` character  
3. Exit tag marker
4. Exit tag type

Instead, the marker type is being exited before the character is consumed, leading to malformed token events.

### System Info
- MDX version: 3.0.0
- Parser: micromark-based tokenizer

This seems to have broken after some refactoring of the tag parsing logic. The issue appears specifically in the `tagEnd` function where tag closing markers are processed.

---
Repository: /testbed
