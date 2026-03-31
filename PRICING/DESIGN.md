# Design System Specification

## 1. Overview & Creative North Star: "The Algorithmic Architect"

This design system moves away from the generic "tech startup" aesthetic toward a high-end editorial experience that blends the precision of Geospatial Information Systems (GIS) with the fluid intelligence of modern AI. 

**The Creative North Star: The Algorithmic Architect.**
We do not build static pages; we architect digital environments. This system thrives on **intentional asymmetry**, where large editorial typography meets a rigorous, math-driven layout. We break the "template" look by overlapping elements, utilizing wide-open negative space, and treating the UI as a series of translucent, illuminated layers rather than flat blocks. The goal is to make the user feel they are interacting with a sophisticated, premium tool built by experts.

---

## 2. Colors & Tonal Depth

Our palette is rooted in the "Deep Sea" spectrum—a foundation of stability and reliability—pierced by "Electric Cyan" to signal innovation and data-driven energy.

### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders are prohibited for sectioning. Structural boundaries must be defined solely through background color shifts or subtle tonal transitions. For example, a `surface-container-low` section should sit directly against a `surface` background to define its edges.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of frosted glass. Use the hierarchy below to define importance:
- **Base Layer:** `surface` (#0b1326)
- **Secondary Sectioning:** `surface-container-low` (#131b2e)
- **Feature Cards:** `surface-container-high` (#222a3d)
- **Interactive Floating Elements:** `surface-container-highest` (#2d3449)

### The "Glass & Gradient" Rule
To escape the "out-of-the-box" feel, use **Glassmorphism** for floating components (Modals, Tooltips, Navigation Bars). 
- **Recipe:** Apply `surface-variant` (#2d3449) at 60% opacity with a `20px` backdrop-blur.
- **Signature Textures:** For primary CTAs, use a subtle linear gradient from `primary` (#00daf3) to `primary_container` (#004d56) at a 135-degree angle. This adds "visual soul" that flat colors lack.

---

## 3. Typography: Editorial Authority

We use a high-contrast typographic scale to create an authoritative, expert tone.

*   **Display & Headlines (Space Grotesk):** This is our "Tech" voice. It is geometric, slightly wide, and feels engineered. Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero sections to create a bold, editorial impact.
*   **Titles & Body (Inter):** This is our "Expert" voice. Inter provides unmatched readability. Use `body-lg` (1rem) for long-form content to ensure the user never feels fatigued.
*   **Labels (Manrope):** Used for metadata, GIS coordinates, or AI status tags. Manrope adds a touch of modern sophistication to the smallest details.

**The Scale Logic:** The massive jump between `display-lg` and `body-md` is intentional. It creates a hierarchy that feels curated, like a high-end architecture magazine.

---

## 4. Elevation & Depth: Tonal Layering

Traditional shadows are too "heavy" for a modern tech brand. We achieve lift through light and color.

*   **The Layering Principle:** Depth is achieved by stacking. Place a `surface-container-lowest` card on a `surface-container-low` section. The slight shift in value creates a soft, natural lift.
*   **Ambient Shadows:** When a floating effect is required, use extra-diffused shadows. 
    *   *Blur:* 32px to 64px.
    *   *Opacity:* 6% - 8%.
    *   *Color:* Use a tinted version of `on-surface` (#dae2fd) rather than black. This mimics natural light reflecting off a tech-forward surface.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility, it must be a "Ghost Border": use the `outline-variant` (#40484c) at **15% opacity**. Never use 100% opaque lines.

---

## 5. Components

### Buttons
- **Primary:** Gradient from `primary` to `primary_container`. Text color `on-primary`. Roundedness `full` (9999px) for a high-tech, aerodynamic feel.
- **Secondary:** Transparent background with a `Ghost Border`. Text color `primary`. 
- **Interactions:** On hover, the primary button should "glow" by increasing the shadow spread of the `surface-tint` color.

### Cards & Services Portfolio
- **Constraint:** Zero divider lines. 
- **Styling:** Use `surface-container-high`. Use `xl` (0.75rem) corner radius. 
- **Layout:** Use asymmetric padding—more breathing room at the top (Spacing 12) than at the sides (Spacing 8) to give a "gallery" feel.

### Input Fields
- **Style:** Minimalist. A background of `surface-container-lowest` with a 2px bottom-only highlight in `primary` when focused.
- **Error State:** Use `error` (#ffb4ab) only for the text and icon; do not wrap the whole box in red, which breaks the aesthetic harmony.

### GIS & AI Specialized Components
- **Data Chips:** Use `secondary_container` with `label-md` typography. 
- **Status Indicators:** Use `tertiary` (#59dad1) with a soft pulse animation to represent "AI Thinking" or "Data Syncing."
- **Maps (GIS):** Map containers should always use `md` (0.375rem) roundedness and be inset within a `surface-container-low` wrapper to feel integrated into the "dashboard" environment.

---

## 6. Do’s and Don’ts

### Do:
- **Do** use large amounts of vertical white space (Scale 16 and 24) to separate major sections.
- **Do** overlap images or data visualizations over background text to create depth.
- **Do** use `primary_fixed_dim` for subtle icons that shouldn't compete with the main CTA.

### Don’t:
- **Don't** use 1px solid dividers. If you need a break, use a 1px tall rectangle of `surface-variant` at 20% opacity.
- **Don't** use standard "drop shadows" (Black/Grey). Always tint shadows with the brand's deep blues.
- **Don't** crowd the layout. If a section feels "busy," increase the spacing scale by two steps.
- **Don't** use sharp 90-degree corners. Everything must have at least the `DEFAULT` (0.25rem) roundedness to feel modern and approachable.