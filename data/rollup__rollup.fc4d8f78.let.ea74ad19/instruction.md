# Bug Report

### Describe the bug

When passing an empty array as input via command line arguments (e.g., `command._` being an empty array `[]`), the CLI incorrectly treats it as a valid input source instead of falling through to check other input options. This causes unexpected behavior where an empty array is used as the input source rather than using the `command.input` value or other fallback options.

### Reproduction

```js
// When command object looks like this:
const command = {
  _: [],  // empty array from command line parsing
  input: 'src/index.js'
}

// The current code will use command._ (empty array) as inputSource
// instead of falling back to command.input
```

This happens because the condition checks for the existence of `command._` rather than checking if it's a non-empty array.

### Expected behavior

When `command._` is an empty array, the code should fall through to the next condition and use `command.input` instead. Only non-empty arrays should be treated as valid input sources from command line arguments.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
