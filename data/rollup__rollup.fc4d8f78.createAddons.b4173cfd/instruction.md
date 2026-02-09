# Bug Report

### Describe the bug

When using the `intro` option in the output configuration, the generated code has the intro text appearing in the wrong position. Instead of being placed at the beginning of the chunk with proper spacing after it, the intro content is now incorrectly positioned with newlines before it.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    intro: '/* My intro comment */'
  }
}
```

After building, the intro text appears with newlines prepended instead of appended, causing it to be separated from the actual code in an unexpected way.

### Expected behavior

The intro should be placed at the start of the chunk with newlines added **after** it (not before), so that it's properly positioned before the actual code content with appropriate spacing.

For example, it should generate:
```
/* My intro comment */

[actual code here]
```

But instead it's generating something like:
```

/* My intro comment */[actual code here]
```

### Additional context

This seems to have started happening recently. The `banner` option also appears to be affected - it's no longer adding the expected newline after the banner text.

---
Repository: /testbed
