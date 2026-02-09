# Bug Report

### Describe the bug

Import statements are not being generated correctly. When trying to use code that contains import declarations, the output is completely broken and shows numeric values instead of proper import syntax.

### Reproduction

```js
// Input code with import statement
import { something } from 'module';
import * as utils from 'utils';
import defaultExport from 'package';

// Expected output:
// import { something } from 'module';
// import * as utils from 'utils';
// import defaultExport from 'package';

// Actual output:
// 1 2 3
// 4 5 6
// 7 8 9
```

The generator seems to be outputting literal numbers instead of processing ImportDeclaration nodes properly. This breaks any code that uses ES6 imports.

### Expected behavior

Import declarations should be correctly transformed into valid import statements with proper syntax including:
- Default imports
- Named imports  
- Namespace imports
- Mixed import types

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: 18.x

This is blocking our ability to use MDX files with any imports. Any help would be appreciated!

---
Repository: /testbed
