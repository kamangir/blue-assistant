# @web

## @web fetch

```bash
@web fetch - https://ode.rsl.wustl.edu/ -
```



<details>
<summary>metadata</summary>

```yaml
blue_assistant-web:
  links:
  - https://ode.rsl.wustl.edu/venus/index.aspx
  - https://ode.rsl.wustl.edu/moon/index.aspx
  - https://ode.rsl.wustl.edu/mercury/index.aspx
  - https://ode.rsl.wustl.edu/mars/index.aspx
  text: 'PDS Geosciences Node Orbital Data Explorer (ODE) + NASA Homepage + NASA en
    Espaol + Contact NASA HOME DATA AND SERVICES TOOLS ABOUT US CONTACT US SITE MAP
    Welcome to the Orbital Data Explorer The PDS Geosciences Node Orbital Data Explorer
    (ODE) website is a cross-mission and instrument query, search, display, and download
    tool for locating and retrieving PDS orbital science data archives of Mars , Mercury
    , Venus , and the Moon . ODE provides a faceted product search and an interactive
    map-based search interface for finding desired orbital observations. A convenient
    user cart feature allows multiple PDS data products to be downloaded at one time.
    Individual data files may be downloaded directly from observation detail pages,
    as well. All data products are freely available. Questions can be directed to
    ode@wunder.wustl.edu . Orbital Data Explorer Targets: Mars Orbital Data Explorer
    The Mars Orbital Data Explorer (ODE) provides search, display, and download tools
    for selected PDS science data archives of the Mars Reconnaissance Orbiter (MRO),
    the 2001 Mars Odyssey, the Mars Global Surveyor (MGS), the Viking Orbiter 1 and
    2, and the European Space Agency''s Mars Express and ExoMars Trace Gas Orbiter
    missions. Supported Missions and Instruments: Mars Reconnaissance Orbiter (MRO):
    CRISM, CTX, Gravity/Radio Science, HiRISE, MCS, SHARAD ESA''s ExoMars Trace Gas
    Orbiter: ACS, CASSIS, NOMAD ESA''s Mars Express: HRSC, MARSIS, OMEGA, PFS, VMC
    2001 Mars Odyssey: GRS, THEMIS Mars Global Surveyor: MOC, MOLA, TES Viking Orbiter
    1 and 2: VISAB Lunar Orbital Data Explorer The Lunar Orbital Data Explorer (ODE)
    provides search, display, and download tools for the PDS science data archives
    of the Lunar Reconnaissance Orbiter (LRO), the Gravity Recovery and Interior Laboratory:(GRAIL),
    the Clementine, the Lunar Prospector, the Lunar Orbiter, the Japan Aerospace Exploration
    Agency''s SELENE mission, and the Indian Space Research Organisation''s Chandrayaan-1
    missions. Supported Missions and Instruments: Lunar Reconnaissance Orbiter (LRO):
    DLRE, LAMP, LEND, LOLA, LROC, MRFLRO ISRO''s Chandrayaan-1: M3, Mini-RF JAXA''s
    SELENE: ARD, GRS, HDTV, LALT, LMAG, LRS, MI, PACE, RSAT/VRAD, TC, UPI Gravity
    Recovery and Interior Laboratory (GRAIL): LGRS Clementine: HIRES, LIDAR, LWIR,
    NIR, RSS, UVVIS Lunar Prospector: ER, GRS, MAG, NS, RSS Lunar Orbiter: 24 Inch
    Focal Length Camera, 80mm Focal Length Camera Mercury Orbital Data Explorer The
    Mercury Orbital Data Explorer (ODE) provides search, display, and download tools
    for the PDS science data archives of the MESSENGER (Mercury Surface, Space Environment,
    Geochemistry, and Ranging) mission. Supported Missions and Instruments: MESSENGER:
    GRS, MASCS, MDIS-NAC, MDIS-WAC, MLA, NS, RSS, and XRS Venus Orbital Data Explorer
    The Venus Orbital Data Explorer (ODE) provides search, display, and download tools
    for the PDS science data archives of the Magellan mission, the MESSENGER mission''s
    Venus data, and ESA''s Venus Express mission. Supported Missions and Instruments:
    Magellan: RDRS, RSS MESSENGER (Venus Data): GRS, MASCS, MDIS-NAC, MDIS-WAC, MLA,
    NS, RSS, and XRS ESA''s Venus Express: MAG, VIRTIS + Freedom of Information Act
    + NASA Privacy Statement, Disclaimer, and Accessibility Certification + Copyright/Image
    Use Policy Curator: Jennifer Ward NASA Official: Paul Byrne Last Updated: + Comments
    and Questions 1'

```

</details>


## @web crawl

```bash
@select crawl-$(@@timestamp)

@web crawl cache \
    https://ode.rsl.wustl.edu/+https://oderest.rsl.wustl.edu/ . \
    --max_iterations 20

@publish tar .
```



<details>
<summary>metadata</summary>

```yaml
crawl_cache:
  https://ode.rsl.wustl.edu/: text/html
  https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/mercury/index.aspx: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
  https://oderest.rsl.wustl.edu/: text/html
  https://oderest.rsl.wustl.edu/#ODERESTInterface: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/GDSMOLAPEDR.html: text/html
  https://oderest.rsl.wustl.edu/GDS_REST_V2.0.pdf: application/pdf
  https://oderest.rsl.wustl.edu/LPSC45_ODE_Abstract.pdf: application/pdf
  https://oderest.rsl.wustl.edu/gdsweb/GDSDLRERDR.html: text/html
  https://oderest.rsl.wustl.edu/gdsweb/GDSLOLARDR.html: text/html
  https://oderest.rsl.wustl.edu/gdsweb/GDSMLARDR.html: text/html
  https://oderest.rsl.wustl.edu/live2/?query=featureclasses&odemetadb=mars: text/xml;
    charset=utf-8
  https://oderest.rsl.wustl.edu/live2/?query=featurenames&odemetadb=mars: text/xml;
    charset=utf-8
  https://oderest.rsl.wustl.edu/live2/?query=iipt: text/xml; charset=utf-8
  ? https://oderest.rsl.wustl.edu/live2?query=products&target=mars&results=c&ihid=MRO&iid=HiRISE&pt=RDRV11&minlat=0.0&maxlat=10.0&westernlon=1&easternlon=5&loc=b
  : text/xml; charset=utf-8
  https://oderest.rsl.wustl.edu/live2?target=mars&query=product&results=cm&output=XML&pt=RDR&iid=HiRISE&ihid=MRO: text/xml;
    charset=utf-8
  ? https://oderest.rsl.wustl.edu/livegds?query=divinerrdr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01&channel=tffffffff
  : unknown
  https://oderest.rsl.wustl.edu/livegds?query=lolardr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01: unknown

```

</details>


[crawl-2025-03-15-s8jrfg](https://kamangir-public.s3.ca-central-1.amazonaws.com/crawl-2025-03-15-s8jrfg.tar.gz)
