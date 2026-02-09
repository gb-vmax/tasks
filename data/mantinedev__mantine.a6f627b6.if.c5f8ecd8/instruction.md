# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where passing an empty array or certain types of data causes the dropdown to not render any options. The component seems to be processing the data incorrectly and returning an empty result even when valid data is provided.

### Reproduction

```js
import { Combobox } from '@mantine/core';

// This doesn't render any options
const data = ['Option 1', 'Option 2', 'Option 3'];

<Combobox data={data}>
  {/* No options appear */}
</Combobox>
```

Also tried with object format:

```js
const data = [
  { value: '1', label: 'Option 1' },
  { value: '2', label: 'Option 2' }
];

// Still no options rendered
<Combobox data={data} />
```

### Expected behavior

The Combobox should display all the provided options in the dropdown. String arrays should be converted to the proper format and object arrays should be rendered as-is.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
