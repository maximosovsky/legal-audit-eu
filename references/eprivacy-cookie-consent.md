# ePrivacy / PECR cookie and tracking review

Not legal advice. Cookie and tracking enforcement differs by country, but these checks reflect common EU/UK supervisory-authority expectations.

## Prior consent baseline

Before consent, load only strictly necessary storage/access. Normally block until opt-in:

- analytics: GA4, Adobe, Matomo if not configured under a regulator-specific exemption;
- advertising pixels: Meta, TikTok, LinkedIn, Google Ads;
- session replay/heatmaps: Hotjar, Clarity, FullStory;
- social embeds and cross-site tracking widgets;
- affiliate/retargeting/tracking identifiers.

## CMP requirements

- Accept and reject are equally prominent/easy.
- Granular choices by purpose/vendor where feasible.
- No pre-ticked non-essential categories.
- Withdrawal/change settings available after first choice.
- Consent record stores purposes, version, timestamp and source.
- Cookie policy table names cookie, provider, purpose, category, duration, and third-party access.

## Common red flags

- “By continuing you accept cookies” with no real choice.
- Close/X equals consent.
- Analytics fires before banner interaction.
- Reject button hidden behind extra clicks while accept is one click.
- Cookie table lists generic categories but code loads specific ad pixels.
- Session replay records form fields or sensitive pages without masking.
