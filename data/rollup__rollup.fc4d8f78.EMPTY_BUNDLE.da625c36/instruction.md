# Bug Report

### Describe the bug

The warning message for empty bundles is displaying incorrect grammar. When a single empty chunk is generated, the message incorrectly shows "Generated an empty chunk" instead of "Generated empty chunk".

### Reproduction

Build a configuration that generates a single empty bundle/chunk. The warning output will show:

```
Generated an empty chunk
```

But when multiple empty chunks are generated, it correctly shows:

```
Generated empty chunks
```

### Expected behavior

For a single empty chunk, the message should be:
```
Generated empty chunk
```

The article "an" should only appear when there are multiple chunks (e.g., "Generated an empty chunks" doesn't make grammatical sense anyway, but the logic seems reversed).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
