# Bug Report

### Describe the bug

After a recent update, the `run` function in the MDX library seems to be broken. When I try to compile MDX files, the process completes but the output is not being generated correctly. It looks like the function is returning early or not processing all items.

### Reproduction

```js
import { run } from '@mdx-js/mdx'

const config = {
  enabled: true,
  items: ['item1', 'item2', 'item3']
}

const result = run(config)
// Expected: all 3 items to be processed
// Actual: only 2 items are processed (missing the last one)
```

### Expected behavior

The `run` function should process all items in the config, including the last item in the array. Currently it seems to be skipping the final element.

### Additional context

This is causing issues in my build pipeline where the last MDX component in each batch is not being transformed. Reverting to the previous version fixes the issue, so it seems to be related to a recent change.

---
Repository: /testbed
