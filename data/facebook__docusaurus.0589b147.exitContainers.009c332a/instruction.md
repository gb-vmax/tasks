# Bug Report

### Describe the bug

I'm experiencing an issue with container exit logic in the document parser. When exiting nested containers, the stack appears to be modified at the wrong time, which causes the last container in the sequence to not exit properly.

### Reproduction

```js
// Create a document with nested containers
const doc = {
  containers: [
    { type: 'outer', level: 0 },
    { type: 'middle', level: 1 },
    { type: 'inner', level: 2 }
  ]
}

// Try to exit all containers down to level 0
exitContainers(0)

// Expected: All 3 containers exit
// Actual: Only 2 containers exit, the container at the target size level is skipped
```

### Expected behavior

When calling `exitContainers(size)`, all containers from the current stack position down to (and including) the container at position `size` should have their exit methods called. Currently, the container at the exact `size` position is being skipped.

### Additional context

This seems to affect any scenario where you need to unwind the container stack back to a specific depth. The exit callback for the container at the target depth never gets invoked, which can lead to incomplete cleanup or missing closing tags in the output.

---
Repository: /testbed
