# Bug Report

### Describe the bug

The plural form selection is completely broken - it's returning the wrong forms in the wrong order. When I try to use pluralization in my theme, I'm getting forms that shouldn't even be there for my locale, and they're appearing in reverse order.

### Reproduction

```js
import { usePluralForm } from '@docusaurus/theme-common';

// For a locale that supports 'one' and 'other' forms
const selectPlural = usePluralForm();

// Trying to select the correct plural form
const result = selectPlural(1, 'message');
// Returns the wrong form or forms that don't exist for this locale
```

When I check what forms are being used, I'm seeing plural forms that my locale doesn't even support, and they're in completely the wrong order. For example, if my locale only uses `one` and `other`, I'm getting back forms like `zero`, `two`, `few`, `many` instead.

### Expected behavior

The function should return only the plural forms that are valid for the current locale, in the correct order (zero, one, two, few, many, other).

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is making it impossible to use pluralization properly in my theme customizations. Any help would be appreciated!

---
Repository: /testbed
