# CLAUDE.md — Projektová pravidla: Web U Cerhů

> Tento soubor je závazný pro celou dobu životnosti projektu.
> Claude Code ho čte automaticky při každém spuštění v tomto adresáři.
> Pravidla jsou psána česky/anglicky dle kontextu.

---

## 1. Identita projektu

| Položka | Hodnota |
|---|---|
| **Projekt** | Web statku U Cerhů — svatební místo & ubytování |
| **Architektura** | statický multi-page web (viz sekce 3), bez build systému |
| **Vlastník** | Jiří Bartoň, Na Rynku 7, 294 02 Kněžmost |
| **Telefon** | +420 605 971 109 |
| **Email** | jiri_barton@centrum.cz |
| **Domain** | u-cerhu.cz |
| **GPS** | 50.4892°N, 15.0383°E |
| **Instagram** | https://www.instagram.com/ucerhu/ |
| **Facebook** | https://www.facebook.com/profile.php?id=100064278752605 |

---

## 2. Technický stack — ZÁVAZNÝ

```
HTML5 (sémantický)  +  Tailwind CSS (CDN)  +  Vanilla JavaScript
```

- **Žádné frameworky** (React, Vue, Angular…) a **žádný build systém / SSG** — čisté `.html` soubory, hlavička/patička/`<head>` boilerplate se mezi stránkami kopíruje 1:1 (viz sekce 3).
- **Žádné npm závislosti** ve výstupu — vše přes CDN.
- **Žádné `// TODO` placeholdery** — každý úsek musí být plně implementován. Jediná povolená výjimka je značka `[DOPLNIT: ...]` pro fakta nepodložená obsahem webu/zadáním (ceny, konkrétní jména, fotky) — musí být uvedena i v závěrečném shrnutí pro klienta.
- Tailwind loaded via: `<script src="https://cdn.tailwindcss.com"></script>` + identický `tailwind.config` (barvy/fonty, sekce 4) na každé stránce.
- Fonty přes Google Fonts CDN:
  - Headings/display: **Playfair Display** (serif) + **Bebas Neue** (display)
  - Body: **Inter**

---

## 3. Architektura webu — multi-page (od 09/2026)

Web je **statický multi-page web**, bez includes/partials a bez build systému. Každá URL je samostatný soubor `slozka/index.html`, servírovaný jako `/slozka/` (trailing slash, žádné `.html` v URL). Nová pravidla nahrazují dřívější „single-file SPA" konvenci — důvodem je pillar–cluster SEO architektura (viz `SEO-fixes.md`), která vyžaduje unikátní title/H1/meta na každou skupinu klíčových slov.

```
/
├── index.html                                — domovská stránka: #hero, #pribeh, #vitejte,
│                                                #galerie, #okoli, #kontakt (plné anchor sekce)
│                                                + #svatby, #ubytovani (KRÁTKÉ teasery s CTA
│                                                na plné pilíře — bez duplicitního obsahu)
├── svatby/
│   ├── index.html                            ← PILÍŘ /svatby/
│   ├── svatby-mlada-boleslav/index.html       ← lokální cluster
│   ├── svatby-liberec/index.html              ← lokální cluster
│   └── svatebni-catering/index.html           ← produktový cluster
├── ubytovani/index.html                      ← PILÍŘ /ubytovani/
├── oslavy-a-vyroci/index.html                 ← nová služba
├── okoli-cesky-raj/
│   ├── index.html                            ← PILÍŘ (turistika/okolí)
│   └── zricenina-hradu-valecov/index.html     ← cluster podstránka
├── magazin/
│   ├── index.html                            ← blogový rozcestník
│   ├── jak-naplanovat-svatbu-na-statku/index.html
│   ├── kolik-stoji-svatba-cesky-raj/index.html
│   └── svatebni-fotograf-cesky-raj/index.html
├── sitemap.xml
├── robots.txt
└── api/contact.js                            — Vercel serverless funkce, sdílená všemi kontakt formuláři
```

### Sdílená šablona stránky (kopíruj beze změny na každou novou stránku)
- **`<head>`**: meta charset/viewport, unikátní `<title>` / `<meta name="description">` / `<link rel="canonical">`, `og:*` a `twitter:*` tagy (title/description/url přizpůsobit dané stránce, zbytek identický), favicon, Google Fonts `<link>`, Tailwind CDN + identický `tailwind.config`, JSON-LD (plné `LocalBusiness`/`EventVenue` schéma na pilířích a homepage, `BreadcrumbList` + lehčí `WebPage`/`Article` schéma na cluster/magazín stránkách).
- **`<body>`**: identická hlavička (`#navbar`, desktop nav, hamburger, mobile menu) a `<footer>` jako na homepage, jen s aktuální nav položkou zvýrazněnou. **Cesty k obrázkům a interní odkazy musí být root-relative** (`/assets/images/...`, `/svatby/`), nikdy relativní (`assets/images/...`, `#svatby`) — jinak se na vnořených URL rozbijí.
- Divider (přeškrtnutý kruh SVG, sekce 4) mezi obsahovými bloky, `reveal` scroll animace, identický `<script>` blok pro hamburger/reveal/rok v patičce/formulář.

---

## 4. Design system — ZÁVAZNÝ

### Barvy

```css
--color-bg:        #FDFBF7;  /* Primary Background — Cream/Warm Off-White */
--color-text:      #1E293B;  /* Primary Text — Deep Slate */
--color-text-dark: #0F172A;  /* Headings — Charcoal */
--color-accent:    #606C38;  /* Sage Green (primary accent) */
--color-accent-2:  #A3B18A;  /* Light Sage (secondary) */
--color-gold:      #D4AF37;  /* Muted Gold (highlights, CTA hover) */
```

### Logo symbol „Přeškrtnutý kruh"

Inline SVG zobrazující přeškrtnutý kruh (stylizované U, C, ů, most).
Použití na **třech místech** — tato pravidla nesmí být porušena:

1. **Hero sekce** — velký watermark na pozadí (opacity ~0.06)
2. **Oddělovač sekcí** — elegantní SVG divider mezi sekcemi
3. **Hover micro-animace** — rotace/rozsvícení na interaktivních prvcích

### Typografie

```css
font-family headings: 'Playfair Display', serif
font-family body:     'Inter', sans-serif  (fallback: 'Montserrat')
```

---

## 5. SEO pravidla — ZÁVAZNÁ

### `<title>`
```
U Cerhů | Exkluzivní svatební místo a ubytování v Českém ráji
```

### `<meta name="description">`
Must highlight: volné termíny 2026, prémiový historický statek, dostupnost z Prahy a Mladé Boleslavi. Max 160 znaků.

### Target keywords — přirozeně zapracovat do H1–H3, alt tagů a `<strong>`:
- Svatby Český ráj
- Ubytování Český ráj
- Svatební místo Mladá Boleslav
- Svatba Turnov
- Svatební stodola Jičín
- Romantická svatba Sobotka
- Statek na svatbu Kněžmost
- Pronájem areálu na svatbu Mnichovo Hradiště

### Schema.org JSON-LD v `<head>`
Typy: `WeddingVenue` + `LocalBusiness`
Povinné fieldy: `name`, `address` (PostalAddress), `telephone`, `email`, `url`, `geo` (GeoCoordinates), `openingHours`, `sameAs` (Instagram, Facebook).

---

## 6. Povinné copy — NESMÍ BÝT MĚNĚNO

Tyto textové bloky musí být zachovány doslova při každé úpravě:

### Storytelling hook (sekce Příběh):
> „Přes čtyři staletí pevné zdi statku. Přes století vůně poctivé kuchyně a smích hostů. Od roku 1907 píšeme příběh rodinné pohostinnosti bez jediného přerušení. Vítejte U Cerhů – na místě, kde se historie prolíná s vaším novým začátkem."

### SEO lokální hub (footer):
> „Hledáte dokonalé svatební místo v Českém ráji? Historický statek U Cerhů v Kněžmostě je ideálně dostupný z Mladé Boleslavi (15 min), Mnichova Hradiště (12 min), Jičína (30 min), Sobotky (20 min), Turnova (30 min) i Prahy (55 min)."

### Valečov copy (sekce Okolí):
> „Statek U Cerhů leží na hranici Českého ráje – od hradu Valečov vás dělí jen 3 km pěší turistické trasy."

---

## 7. Kapacity & data — ZÁVAZNÁ referenční tabulka

### Ubytování — 25 lůžek celkem

| Název | Lůžka | Poznámka |
|---|---|---|
| Pokoj 1 (hlavní budova) | 4 | Vlastní sociální zařízení, prémiové vybavení |
| Pokoj 2 (hlavní budova) | 4 | Vlastní sociální zařízení, prémiové vybavení |
| Pokoj 3 (hlavní budova) | 5 | Vlastní sociální zařízení, prémiové vybavení |
| Apartmán 1 (prázdninový domek) | 5 | Plně vybavená kuchyňka, soc. zařízení — **NOVÉ** |
| Apartmán 2 (prázdninový domek) | 5 | Plně vybavená kuchyňka, soc. zařízení — **NOVÉ** |
| **Celkem** | **25** | Klient 10/2026 potvrdil 25 lůžek celkem — rozpis po pokojích výše zatím dává 23, [DOPLNIT: kde přibyla 2 lůžka] |

### Svatební kapacity

- Hosté: **max 100 osob**
- Exkluzivita: **1 svatba = celý víkend** (absolutní soukromí)
- Prostory: Hlavní sál, Stodola, Dvůr, Terasa, Ubytovací část

### Dostupnost z Kněžmostu

| Město | Vzdálenost | Čas |
|---|---|---|
| Mladá Boleslav | ~11 km | 15 min |
| Mnichovo Hradiště | ~10 km | 12 min |
| Sobotka | ~15 km | 20 min |
| Turnov | ~25 km | 30 min |
| Jičín | ~25 km | 30 min |
| Praha | ~75 km | 55 min |

---

## 8. JavaScript komponenty

### Komponenta: Kalendář volných termínů 2026

- Zobrazit: červen – září 2026
- Styl: vizuální grid s barevným kódováním
  - 🟥 Obsazeno (většina sobot)
  - 🟩 Volný termín (poslední 2–3 soboty)
- Urgency messaging: _„Poslední volné prázdninové termíny pro sezónu 2026"_
- Souboty jsou primární termíny, zobrazit všechny 4 měsíce.

### Komponenta: Navigace

- Sticky header s průhledností → solid po scrollu (JS scroll listener)
- Hamburger menu pro mobile (animace ≥ CSS transition)
- Hladký scroll na anchor sekce (`scroll-behavior: smooth` nebo JS)
- Aktivní stav nav položky dle aktuální sekce (IntersectionObserver)
- **Sticky CTA button**: `"Rezervovat termín 2026"` — vždy viditelný, barva zlatá/sage

---

## 9. UX & přístupnost — WCAG AA

- Všechny obrázky musí mít popisný `alt` text (v češtině, s target keywords).
- Kontrastní poměr textu: min 4.5:1 (AA standard).
- Keyboard navigace: fokus stavy na všech interaktivních prvcích.
- Semantické HTML5 elementy: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<address>`.
- `aria-label` na ikonách bez textu, hamburger menu, sociálních odkazech.
- Skip-to-content link jako první prvek v `<body>`.

---

## 10. Galerie — pravidla pro placeholder obrázky

Zdroj: **Unsplash** (svobodné licence, bez atribuce).
Query terms pro sémanticky relevantní obrázky:

| Slot | Unsplash query |
|---|---|
| Hero | `rustic-wedding-venue` |
| Příběh | `old-farmhouse-countryside` |
| Svatby | `wedding-barn-reception` |
| Ubytování | `cozy-countryside-room` |
| Galerie 1 | `wedding-ceremony-outdoor` |
| Galerie 2 | `rustic-wedding-decoration` |
| Galerie 3 | `wedding-banquet-table` |
| Galerie 4 | `bohemian-paradise-czech` |
| Okolí | `czech-paradise-rocks` |

Format URL: `https://images.unsplash.com/photo-{ID}?w=800&q=80`

---

## 11. Cenová politika — ZÁVAZNÉ zobrazení

Ceny se **nevymýšlí** a nový nepodložený údaj se nikdy nezobrazuje jako pevné číslo.
Výchozí forma je CTA varianta:

- Ubytování: _„Ceny na vyžádání — kontaktujte nás"_
- Pronájem areálu na svatbu: _„Cena pronájmu na vyžádání — rádi vám připravíme nabídku na míru"_

Výjimka: rozpětí **45 000 – 75 000 Kč** za pronájem areálu na svatbu je již veřejně zobrazené na homepage (sekce Svatby) i ve Schema.org JSON-LD (`priceRange`) — tuto existující, klientem potvrzenou hodnotu lze citovat i na nových stránkách jako referenci. Nejde o výjimku pro nové, neověřené částky.

---

## 12. Klíčové prodejní argumenty (USPs)

Vždy zobrazovat jako icon grid nebo bullet list v sekci Svatby:

1. **Exkluzivita** — 1 svatba = celý areál jen váš
2. **Ubytování přímo v areálu** (25 lůžek)
3. **Venkovní i vnitřní obřad**
4. **Historický statek s duší od r. 1590**
5. **3 generace rodinné pohostinnosti**
6. **Parkování zdarma** v areálu / u areálu
7. **WiFi v celém areálu** zdarma
8. **Plně bezbariérový přístup**
9. **Domácí mazlíčci vítáni**

---

## 13. Workflow pro změny

### Před každou úpravou:
1. Přečti tento `CLAUDE.md` celý.
2. Zkontroluj, zda úprava neporušuje povinné copy (sekce 6).
3. Zkontroluj, zda zůstávají správné kontaktní údaje (sekce 1).

### Při přidávání nové stránky/sekce/komponenty:
1. Drž se design systému (sekce 4) — barvy, fonty, logo.
2. Nová URL = nová složka `slozka/index.html`, ne nový soubor na homepage (viz sekce 3) — výjimkou jsou anchor sekce, které zůstávají jen na homepage (`#vitejte`, `#galerie`, `#kontakt`…).
3. Zkopíruj hlavičku/patičku/`<head>` boilerplate ze sdílené šablony (sekce 3), uprav jen title/meta/canonical/OG a zvýrazněnou nav položku — nevymýšlej novou strukturu nav/footeru.
4. Použij root-relative cesty (`/assets/images/...`, `/svatby/...`), nikdy relativní.
5. Přidej odpovídající nav item (header + footer) na **všech** stránkách, kde se sdílená hlavička/patička kopíruje, ne jen na nové stránce.
6. Zajisti, že nová stránka má odkaz na svůj pilíř a naopak (interní prolinkování) — žádná stránka nesmí zůstat „osiřelá".
7. Přidej novou URL do `sitemap.xml`.
8. Zkontroluj WCAG AA (sekce 9).

### Při SEO úpravách:
1. Title tag nesmí být zkracován ani přeformulován.
2. Schema.org JSON-LD vždy aktualizuj při změně kontaktů/kapacit — a to na **všech** stránkách, kde je zkopírované (pilíře + homepage).
3. Target keywords z sekce 5 musí zůstat zastoupeny v H1–H3.
4. Fráze „svatby", „svatby Český ráj", „svatební statek", „svatební místo", „prostory na svatbu" cílí výhradně na `/svatby/` — nikdy nevytvářet pro ně samostatnou konkurenční URL (kanibalizace klíčových slov).

### Zakázané operace:
- ❌ Nezavádět npm / node_modules, build systém ani SSG do projektu
- ❌ Vytvářet duplicitní obsah mezi homepage teaserem a pilířovou stránkou (homepage teaser `#svatby`/`#ubytovani` musí zůstat krátký, plný text patří na `/svatby/` a `/ubytovani/`)
- ❌ Neměnit povinné copy bloky (sekce 6)
- ❌ Uvádět u nového obsahu vymyšlené ceny/fakta bez `[DOPLNIT: ...]` značky (sekce 11 popisuje výchozí CTA formulace; existující zveřejněná cena 45 000–75 000 Kč z homepage/JSON-LD lze citovat jako referenci, nový nepodložený údaj ne)
- ❌ Neodstraňovat Schema.org JSON-LD
- ❌ Nepoužívat generické `alt=""` na obrázky
- ❌ Používat na nových stránkách relativní cesty k assetům/interním odkazům (viz sekce 3)

---

## 14. Git commit konvence

```
feat(sekce):  přidání nové sekce nebo komponenty
fix(copy):    oprava textu, překlepu
seo:          změna metadat, structured data, keywords
style:        vizuální úpravy bez změny funkce
content:      aktualizace termínů, kapacit, kontaktů
a11y:         úpravy přístupnosti (WCAG)
```

Příklad: `content(terminy): aktualizace volných sobot září 2026`

---

## 15. Kontextová poznámka pro Claude Code

Tento projekt je **marketingový web malého rodinného podniku**. Priorita je:

1. **Konverze** (kontaktní formulář, CTA tlačítko rezervace)
2. **Lokální SEO** (Kněžmost, Český ráj, okolní města)
3. **Důvěryhodnost** (historie, rodinné hodnoty, recenze)
4. **Mobilní UX** (většina návštěvníků přichází z mobilu)

Při pochybnostech vždy preferuj: jednoduchost, čitelnost, rychlost načítání.