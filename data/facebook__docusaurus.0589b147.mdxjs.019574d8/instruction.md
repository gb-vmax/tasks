# Bug Report

### MDX parsing fails with ESM imports when using certain configurations

I've encountered an issue where MDX files with ESM imports are not being parsed correctly. The parser seems to be processing extensions in the wrong order, which causes import statements to not be recognized properly.

### Reproduction

Create an MDX file with an ESM import at the top:

```mdx
import { Component } from './Component'

# Hello World

<Component />
```

When parsing this file, the import statement is not handled correctly and the resulting output is malformed.

### Expected behavior

The ESM import should be parsed first before other MDX content, and the import statement should be properly extracted and included in the compiled output.

### Additional context

This seems to be related to how the parser extensions are being combined. The markdown extension might be interfering with the ESM import parsing when it runs before the ESM extension has a chance to process the imports.

---
Repository: /testbed
