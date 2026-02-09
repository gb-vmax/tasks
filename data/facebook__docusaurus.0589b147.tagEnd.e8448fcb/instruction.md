# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing where self-closing tags are not being handled correctly. It seems like the tag marker isn't being properly closed before the tag itself exits, which is causing unexpected behavior in the parsing flow.

### Reproduction

```jsx
const Component = () => {
  return <div />
}
```

When parsing JSX with self-closing tags like the one above, the tag markers appear to be in an incorrect state. The closing `>` marker doesn't get properly exited before the overall tag exits.

### Expected behavior

Self-closing JSX tags should be parsed correctly with all markers properly entered and exited in the right order. The tag marker should be fully processed (entered and exited) before the parent tag type exits.

### Additional context

This affects any JSX content with self-closing tags. The issue appears to be in the tag parsing logic where the marker exit is missing in the sequence of effects.

---
Repository: /testbed
