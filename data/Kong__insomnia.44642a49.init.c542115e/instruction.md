# Bug Report

### Describe the bug

After a recent update, I'm getting errors when trying to create new API specifications. The application crashes with a `TypeError` saying that `init is not a function` or similar. It looks like something changed with how new API specs are initialized.

### Reproduction

```js
import { init } from './models/api-spec';

// This throws an error - init is not defined/not a function
const newSpec = init();
```

When trying to create a new document/specification in the UI, the app fails to initialize the default values for a new API spec.

### Expected behavior

Should be able to create a new API specification with default values:
- fileName: `New Document` (or similar)
- contents: empty string
- contentType: 'yaml'

The `init()` function should return a proper BaseApiSpec object with these defaults.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken after a recent commit. The init function appears to be missing or not exported properly anymore.

---
Repository: /testbed
