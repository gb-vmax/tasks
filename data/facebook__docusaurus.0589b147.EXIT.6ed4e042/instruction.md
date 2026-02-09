# Bug Report

### Describe the bug

I'm experiencing an issue with the `EXIT` constant exported from `unist-util-visit`. When I try to use it in my visitor functions, I'm getting unexpected behavior - it seems like `EXIT` is now returning a function or an object instead of the expected constant value.

### Reproduction

```js
import { visit, EXIT } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] }
  ]
};

visit(tree, 'paragraph', (node) => {
  console.log(EXIT);
  return EXIT;
});
```

When I log `EXIT`, I'm seeing something different than what I expect. It looks like it's been wrapped or modified somehow, and my visitor logic that depends on returning `EXIT` to stop traversal isn't working correctly anymore.

### Expected behavior

`EXIT` should be a simple constant value that can be returned from visitor functions to stop tree traversal, just like `CONTINUE` and `SKIP`. The behavior was working fine before and I didn't change anything in my code.

### System Info
- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
