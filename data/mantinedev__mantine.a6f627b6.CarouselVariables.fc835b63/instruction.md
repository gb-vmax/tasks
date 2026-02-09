# Bug Report

### Describe the bug

I'm experiencing an issue with the Carousel component where responsive `slideGap` and `slideSize` properties are not working correctly. When I pass an object with breakpoint-specific values, the carousel doesn't apply the correct sizing at different screen sizes.

### Reproduction

```tsx
import { Carousel } from '@mantine/carousel';

<Carousel
  slideSize={{ base: '100%', sm: '50%', md: '33.333333%' }}
  slideGap={{ base: 'xs', sm: 'md', md: 'xl' }}
>
  <Carousel.Slide>1</Carousel.Slide>
  <Carousel.Slide>2</Carousel.Slide>
  <Carousel.Slide>3</Carousel.Slide>
</Carousel>
```

When resizing the browser window or viewing on different screen sizes, the slides don't adjust their size or gap according to the breakpoint values provided. It seems like the responsive values aren't being picked up at all.

### Expected behavior

The carousel should apply different `slideSize` and `slideGap` values based on the current breakpoint. For example:
- On mobile (base): slides should be 100% width with 'xs' gap
- On small screens (sm): slides should be 50% width with 'md' gap  
- On medium screens (md): slides should be 33.333333% width with 'xl' gap

### System Info

- @mantine/carousel version: latest
- @mantine/core version: 7.x
- Browser: Chrome/Firefox

---
Repository: /testbed
