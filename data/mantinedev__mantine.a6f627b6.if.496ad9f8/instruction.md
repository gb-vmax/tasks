# Bug Report

### Describe the bug

When passing string values to Combobox components, the parsed data structure is incorrect. The `value` property is being set to `undefined` instead of the actual string value.

### Reproduction

```js
import { Combobox } from '@mantine/core';

const data = ['React', 'Angular', 'Vue'];

<Combobox data={data} />
```

When using simple string arrays as data for the Combobox, the items are not being parsed correctly. The value field ends up as `undefined` which breaks selection functionality.

### Expected behavior

String items should be converted to `{ value: 'string', label: 'string' }` format automatically. Selecting an item should work properly with the string value being used for both the value and label properties.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
