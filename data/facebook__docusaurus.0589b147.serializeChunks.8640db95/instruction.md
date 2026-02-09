# Bug Report

### Describe the bug

I'm experiencing an issue with chunk serialization in the MDX parser. It appears that the serialization logic is producing incorrect output when processing certain character sequences, particularly around tab characters.

### Reproduction

When parsing MDX content that contains specific character patterns, the serialized output doesn't match what's expected. This seems to affect:

1. The initial index position when iterating through chunks
2. Tab character detection logic

Example scenario:
```js
// Processing chunks that should serialize to specific output
// The serialization produces incorrect results, especially when
// tab characters or special character codes are involved
```

### Expected behavior

The chunk serialization should correctly:
- Start iteration at the proper index position
- Accurately detect and handle tab characters (character code checks)
- Produce the expected serialized string output

### System Info
- remark-mdx version: 3.0.0
- Affects MDX content parsing and serialization

This seems like it could be a regression as the logic around index initialization and tab character detection appears to have changed. The issue manifests when processing MDX files with certain formatting.

---
Repository: /testbed
