# Bug Report

### Describe the bug

After updating to the latest version, MDX import statements are generating with an extra comma at the beginning. This breaks the generated JavaScript code and causes syntax errors.

### Reproduction

When using MDX with import statements like:

```mdx
import { Component } from './component'
import DefaultExport from './default'
import * as Everything from './everything'
```

The generated output has an unexpected leading comma:

```js
import , Component from './component';
import , DefaultExport from './default';
import , * as Everything from './everything';
```

This results in syntax errors when trying to execute the generated code.

### Expected behavior

Import statements should be generated without the leading comma:

```js
import Component from './component';
import DefaultExport from './default';
import * as Everything from './everything';
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
