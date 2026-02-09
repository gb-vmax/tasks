# Bug Report

### Describe the bug

When building with multiple empty chunks, the warning message shows incorrect grammar and displays the wrong chunk name. The message says "Generated an empty chunks" (grammatically incorrect) and shows the last chunk name instead of the first one.

### Reproduction

Create a build configuration that generates multiple empty chunks:

```js
// rollup.config.js
export default {
  input: ['empty1.js', 'empty2.js', 'empty3.js'],
  output: {
    dir: 'dist'
  }
}
```

Where the input files are empty or only contain comments.

When the build runs, you'll see:
```
Generated an empty chunks
"empty3"
```

### Expected behavior

The warning should display:
- Correct grammar: "Generated empty chunks" (not "an empty chunks")
- The first chunk name: "empty1" (not "empty3")

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
