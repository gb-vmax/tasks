# Bug Report

### Describe the bug

The Grid component's gutter spacing is not being applied at the base/default breakpoint level. The `--grid-gutter` CSS variable is only being set for media queries but not for the base styles, causing the grid to have no gutter spacing at smaller screen sizes or when no breakpoint-specific gutter is defined.

### Reproduction

```jsx
import { Grid } from '@mantine/core';

function Demo() {
  return (
    <Grid gutter="md">
      <Grid.Col span={6}>Column 1</Grid.Col>
      <Grid.Col span={6}>Column 2</Grid.Col>
    </Grid>
  );
}
```

When rendering this component, the grid columns have no spacing between them at the base breakpoint. The gutter only appears when the viewport matches one of the larger breakpoints.

### Expected behavior

The gutter should be applied at all screen sizes, including the base/default breakpoint. The `--grid-gutter` CSS variable should be set in the base styles before any media queries are applied.

### Additional context

This also affects grids with responsive gutter objects:

```jsx
<Grid gutter={{ base: 'xs', sm: 'md', lg: 'xl' }}>
  {/* columns */}
</Grid>
```

The base gutter value is ignored and only the sm/lg values take effect.

---
Repository: /testbed
