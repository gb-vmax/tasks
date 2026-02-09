# Bug Report

### Describe the bug

I'm experiencing an issue with the Carousel component where responsive breakpoint styles are not being applied correctly. When I define `slideGap` or `slideSize` as responsive objects with breakpoint values, the carousel doesn't adjust its spacing or size at different screen sizes.

### Reproduction

```jsx
import { Carousel } from '@mantine/carousel';

<Carousel
  slideSize={{ base: '100%', sm: '50%', md: '33.333%' }}
  slideGap={{ base: 'xs', sm: 'md', md: 'lg' }}
>
  <Carousel.Slide>1</Carousel.Slide>
  <Carousel.Slide>2</Carousel.Slide>
  <Carousel.Slide>3</Carousel.Slide>
</Carousel>
```

When resizing the browser window, the slides don't change their size or gap according to the breakpoints. The carousel seems to be stuck with only the base styles and doesn't respond to viewport changes.

### Expected behavior

The carousel should apply different `slideSize` and `slideGap` values at different breakpoints (sm, md, lg, etc.). For example:
- At `base`: slides should be 100% width with xs gap
- At `sm`: slides should be 50% width with md gap  
- At `md`: slides should be 33.333% width with lg gap

### System Info

- @mantine/carousel version: latest
- @mantine/core version: 7.x
- Browser: Chrome 120

---
Repository: /testbed
