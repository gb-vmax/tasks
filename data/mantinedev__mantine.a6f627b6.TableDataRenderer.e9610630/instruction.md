# Bug Report

### Describe the bug

The `TableDataRenderer` component is rendering the table caption in the wrong position. According to HTML standards, the `<caption>` element should be the first child of a `<table>` element, appearing before `<thead>`, `<tbody>`, and `<tfoot>`. Currently, the caption is being rendered after the table head section.

### Reproduction

```jsx
import { Table } from '@mantine/core';

const data = {
  caption: 'My Table Caption',
  head: ['Column 1', 'Column 2'],
  body: [
    ['Row 1 Col 1', 'Row 1 Col 2'],
    ['Row 2 Col 1', 'Row 2 Col 2']
  ]
};

<Table.DataRenderer data={data} />
```

When inspecting the rendered HTML, the caption appears after the `<thead>` element instead of before it, which violates the HTML spec and may cause accessibility issues with screen readers.

### Expected behavior

The caption should be rendered as the first child of the table, before the thead element. The correct HTML structure should be:

```html
<table>
  <caption>My Table Caption</caption>
  <thead>...</thead>
  <tbody>...</tbody>
</table>
```

### Additional context

This affects accessibility as screen readers expect captions to be positioned correctly to properly announce table context to users.

---
Repository: /testbed
