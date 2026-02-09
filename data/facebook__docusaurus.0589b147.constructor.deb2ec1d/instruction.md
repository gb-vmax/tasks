# Bug Report

### Describe the bug

I'm encountering an issue where the output initialization in the State constructor is inconsistent. When no `output` option is provided, the output is being set to `null` instead of an empty string, which causes problems when trying to concatenate strings to it later.

### Reproduction

```js
const state = new State();
// state.output is now null instead of ""

// This will fail because you can't concatenate to null
state.write('some code');
// Expected: state.output === 'some code'
// Actual: TypeError or unexpected behavior
```

The issue occurs when creating a State instance without providing an output stream option. The constructor sets `this.output = null` in the else branch, but the `write` method expects it to be a string and tries to concatenate to it with `this.output += code2`.

### Expected behavior

When no output option is provided, `this.output` should be initialized as an empty string `""` so that the default `write` method can properly concatenate strings to it.

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: v18.x

---
Repository: /testbed
