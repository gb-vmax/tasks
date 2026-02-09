# Bug Report

### Describe the bug

The translation extraction is not working correctly when using the `translate()` function. When I call `translate()` with a single argument (the translation message), it's not being extracted properly.

### Reproduction

```js
import {translate} from '@docusaurus/Translate';

// This translation is not being extracted
const message = translate('Hello world');
```

The translation extraction seems to skip over valid `translate()` calls that have exactly one argument. This worked fine in previous versions.

### Expected behavior

The `translate()` function should accept a single argument (the message string) and the translation extractor should detect and extract it properly. Single-argument calls are valid and commonly used throughout the codebase.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
