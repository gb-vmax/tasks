# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM block parsing where the `data.estree` property is being set incorrectly. When processing MDX files with ESM imports/exports, the estree data seems to be attached to nodes even when it shouldn't be.

### Reproduction

```js
// MDX file with ESM block
import { something } from 'somewhere'

export const config = { value: 123 }

# My Component

Some content here
```

When parsing this MDX content, the resulting AST nodes for the ESM blocks have unexpected `data.estree` properties. It appears that the estree data is being set on nodes when the estree value is falsy, which doesn't seem right.

### Expected behavior

The `data.estree` property should only be set on mdxjsEsm nodes when there's actually valid estree data to attach. If there's no estree or if it's explicitly false/undefined, the data property shouldn't be created or should be handled differently.

### Additional context

This seems to affect how the ESM blocks are processed and could potentially cause issues with transformations or plugins that rely on the AST structure being correct.

---
Repository: /testbed
