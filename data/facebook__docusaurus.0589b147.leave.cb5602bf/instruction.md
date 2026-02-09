# Bug Report

Title: MDX compilation broken - incomplete function transformation

I'm experiencing an issue where MDX files are failing to compile correctly. It seems like the JavaScript rewrite transformation is getting cut off mid-execution.

### Describe the bug
After a recent update, MDX compilation appears to be incomplete. The `recmaJsxRewrite` function's `leave` handler is not fully processing function nodes, which results in malformed JavaScript output. The transformation just stops abruptly without completing the component resolution logic.

### Reproduction
Try compiling any MDX file that uses components:

```mdx
# Hello

<CustomComponent />

Some content here.
```

The compilation process doesn't complete properly and the generated JavaScript is truncated. The component destructuring and props handling code that should be generated is missing.

### Expected behavior
MDX files should compile successfully with complete JavaScript transformations. The `leave` handler should fully process function declarations/expressions and generate all necessary component resolution code including:
- Component defaults
- Component parameters
- Provider imports (if configured)
- Proper destructuring patterns

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking our entire build process since no MDX files can compile anymore. Any help would be greatly appreciated!

---
Repository: /testbed
