# Bug Report

### Describe the bug

After a recent update, I'm getting errors when trying to use exported functions from the unist-util-visit module. It seems like the exports are not being properly defined - I'm seeing `undefined` when trying to access exported members.

### Reproduction

```js
import { visit } from 'unist-util-visit';

// This throws an error or visit is undefined
const tree = {
  type: 'root',
  children: []
};

visit(tree, 'text', (node) => {
  console.log(node);
});
```

When I try to access any exported function, I get errors like `visit is not a function` or the import is just `undefined`.

### Expected behavior

The exported functions should be accessible and work as documented. The module exports should be properly defined so that imports work correctly.

### Additional context

This seems to have started happening recently. The module was working fine before, but now none of the exports are accessible. It looks like there might be an issue with how the module is bundling or exporting its functions.

---
Repository: /testbed
