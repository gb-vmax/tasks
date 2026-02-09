# Bug Report

### Describe the bug

The plural form selection for English locale is returning incorrect values. When I pass a count of 1, it's returning 'other' instead of 'one', which breaks pluralization in the UI.

### Reproduction

```js
import {usePluralForm} from '@docusaurus/theme-common';

const selectForm = usePluralForm();

// This returns 'other' but should return 'one'
console.log(selectForm(1)); // Expected: 'one', Actual: 'other'

// This also returns 'other' 
console.log(selectForm(5)); // Expected: 'other', Actual: 'other'

// This returns 'one' but should return 'other'
console.log(selectForm(0)); // Expected: 'other', Actual: 'one'
```

### Expected behavior

For English pluralization:
- Count of 1 should return 'one' (singular form)
- Count of 0, 2, 3, etc. should return 'other' (plural form)

Currently it seems like the logic is inverted - everything >= 1 is being treated as plural, and < 1 is being treated as singular.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
