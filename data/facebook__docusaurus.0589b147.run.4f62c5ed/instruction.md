# Bug Report

### Describe the bug

After a recent update, the `run` export from `@mdx-js/mdx` is no longer functioning as expected. When trying to import and use the `run` function, I'm getting errors indicating that `run` is not a function or is undefined.

### Reproduction

```js
import { run } from '@mdx-js/mdx'

// This throws an error
const result = await run(vfile, options)
```

The code that was working before now fails with something like `run is not a function` or similar.

### Expected behavior

The `run` function should be directly callable as it was in previous versions. It should execute the MDX runtime and return the expected result.

### Additional context

This appears to have started happening after the latest update. The export seems to have changed structure - it looks like `run` might now be wrapped in some kind of factory function or object, but the public API should remain the same for backward compatibility.

---
Repository: /testbed
