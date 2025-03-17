# orbital-data-explorer 🔥

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/).

```yaml
script:
  vars:
    crawl_seeds:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access

    context_prompt: |
      Our objective is to write Python code to access the Orbital Data Explorer, ODE for short,
      using STAC terminology. For this purpose, we consider ODE as a catalog and each separate
      dataset in ODE as a collection that contains items.

    extraction_prompt: |
      Extract the information relevant to this objective from the following text.

    summarize_prompt: |
      Summarize the following information in the context of this objective.

  nodes:
    web_crawl:
      action: web_crawl
      max_iterations: 100
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2

    expanding_the_extractions:
      action: expanding_the_extractions
      max_nodes: 10
      test_mode:
        max_nodes: 2
      depends-on: web_crawl

    extraction:
      action: generate_text
      prompt: >
        :::context_prompt
        :::extraction_prompt
        :::url_content
      depends-on: expanding_the_extractions

    generating_summary:
      runnable: false
      action: generate_text
      prompt: >
        :::context_prompt
        :::summarize_prompt
      depends-on: extraction

    writing_code:
      runnable: false
      action: generate_text
      depends-on: generating_summary

  versions:
    downloading_a_datacube:
      vars:
        context_prompt: |
          We want to write Python code to download data from the Orbital Data Explorer, ODE
          for short, using STAC terminology.
      nodes: {}

```
[metadata.yaml](../metadata.yaml)

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer,version=downloading_a_datacube .

@publish tar .

@assets publish extensions=png,push .
```



<details>
<summary>output</summary>

```yaml
script:
  nodes:
    expanding_the_extractions:
      action: expanding_the_extractions
      completed: true
      depends-on: web_crawl
      max_nodes: 10
      test_mode:
        max_nodes: 2
    extraction_001:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_12_11_2015_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology,\
        \ you will need to interact with the dataset's metadata and potentially the\
        \ API or interface it uses for data retrieval. Here's a breakdown of the relevant\
        \ information extracted from the provided text:\n\n1. **Data Products and\
        \ Missions**: The text lists several data products along with their missions,\
        \ instruments, number of products and files, file sizes, last added and synced\
        \ dates, orbit ranges, and observation ranges. For instance:\n   - **Mission**:\
        \ MEX (Mars Express), MGS (Mars Global Surveyor), MRO (Mars Reconnaissance\
        \ Orbiter), ODY (Mars Odyssey), etc.\n   - **Instrument/Product Types**: HRSC,\
        \ MARSIS, OMEGA, HIRISE, THEMIS, etc.\n\n2. **Observation Range**: Indicates\
        \ the period during which the observations were made. For example, \"2004-01-10\
        \ to 2010-03-26\" for some MEX HRSC data products.\n\n3. **Last Time Product\
        \ Added and Synced**: Dates showing when the last data products were added\
        \ to and synced with ODE. This ensures the ODE database reflects the current\
        \ state of the data products.\n\n4. **STAC Terminology**: While the STAC terminology\
        \ (SpatioTemporal Asset Catalog) isn't explicitly mentioned in the text, the\
        \ provided information aligns with key STAC metadata concepts such as:\n \
        \  - **Items**: The individual data entries (products) with associated metadata,\
        \ like observation periods, sensor types, etc.\n   - **Collections**: Could\
        \ correspond to the different missions or instruments.\n   - **Assets**: The\
        \ downloadable files themselves, including their size and number.\n\n5. **Metadata\
        \ Information**: Crucial elements that would be relevant for STAC collection,\
        \ such as:\n   - `product_type`\n   - `number_files`\n   - `file_size`\n \
        \  - `observation_range`\n   - `last_synced`\n\nTo automate the download of\
        \ this data using Python, consider interfacing with an API (if available)\
        \ or navigating the download pathways provided by the data management system\
        \ of ODE using libraries such as `requests` for HTTP requests, `pystac` for\
        \ handling STAC catalogs, and potentially `pandas` or `numpy` for data handling\
        \ and processing post-download."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2015-12-10T14:55 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range MEX HRSC DTMRDR 9,286 73,532
        616,779.10 2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEX HRSC
        RDR 42,325 253,950 4,513,168.59 2015-02-21 2015-07-18 10-13323 2004-01-10
        to 2014-06-29 MEX HRSC RDRV3 31,693 190,158 3,560,964.71 2015-12-07 2015-12-07
        10-7982 2004-01-10 to 2010-03-26 MEX HRSC REFDR 34,811 243,677 5,049,869.79
        2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29 MEX HRSC (MSL Landing
        Site Selection) Cale_D 4 12 32.86 2012-02-27 2014-08-22 - - MEX HRSC (MSL
        Landing Site Selection) Gwin_D 8 24 1,116.56 2012-02-27 2014-08-22 - - MEX
        MARSIS EDR 5,412 10,824 8,183.68 2015-04-30 2015-07-30 1885-3068 2005-07-04
        to 2006-05-31 MEX MARSIS RDRAIS 8,343 2,468,340 294,773.78 2015-06-16 2015-06-16
        1844-13649 2005-06-22 to 2014-10-02 MEX MARSIS RDRSS 730 1,460 3,893.74 2015-04-29
        2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEX OMEGA DDRGM 8 46 1,476.99
        2015-04-29 2015-04-29 6-8485 2004-01-08 to 2010-08-20 MEX OMEGA EDR 22,623
        84,364 929,426.86 2015-09-10 2015-09-10 -304-12797 2003-02-19 to 2014-01-27
        MEX PFS EDR 50,289 225,231 82,024.45 2015-04-30 2015-04-30 10-11451 2003-05-02
        to 2071-01-16 MGS MOC-NA/WA NADSDP 1,234 3,641 5,062.84 2013-11-05 2015-07-16
        - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802 191,485 204,048.94 2009-03-11
        2015-08-04 -97-33982 1999-02-28 to 2006-10-15 MGS MOC-NA/WA WADSDP 814 2,436
        634.66 2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WASDP
        145,676 291,340 60,892.12 2009-03-11 2015-08-04 -97-33998 1999-02-28 to 2006-10-17
        MGS MOLA MEGDR 89 267 12,497.36 2009-03-11 2015-08-19 3-20333 1997-09-15 to
        2001-06-30 MGS MOLA PEDR 771 7,710 23,968.75 2009-03-11 2015-06-03 1578-20327
        1999-02-28 to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,139.32 2009-03-11 2015-06-03
        - 1999-02-28 to 2006-11-02 MGS MOLA SHADR 1 2 0.52 2009-03-11 2015-06-03 -
        1997-09-15 to 1999-12-31 MGS TES TIMAP 4 20 162.32 2013-10-28 2015-06-03 -
        - MGS TES TSDR 326 23,702 198,114.76 2013-10-28 2015-07-06 - - MGS TES (MSL
        Landing Site Selection) Band_D 4 46 179.45 2012-02-27 2014-08-22 - - MISC
        SHAPE Cale_D 4 12 32.86 2012-02-27 2014-08-22 - - MRO CRISM ANCILL 4,675 9,350
        604.10 2015-11-24 2015-11-24 - 2006-09-27 to 2015-05-09 MRO CRISM CDR 2,394,178
        4,788,356 459,825.12 2015-11-24 2015-11-24 - 1980-01-01 to 2015-05-09 MRO
        CRISM DDR 869,199 1,738,398 3,174,548.95 2015-11-23 2015-11-23 - 2006-09-27
        to 2015-05-09 MRO CRISM EDR 1,964,887 11,780,553 15,383,339.63 2015-11-24
        2015-11-24 - 2006-09-27 to 2015-05-09 MRO CRISM LDR 4,404 8,808 9,141.36 2015-11-23
        2015-11-23 - 2009-07-10 to 2015-04-17 MRO CRISM MRDR 17,671 49,087 3,751,401.26
        2012-02-29 2014-08-22 - - MRO CRISM MTRDR 9 57 3,679.71 2012-03-16 2012-10-18
        - 2008-01-09 to 2011-12-06 MRO CRISM TER 6 21 1,972.84 2012-03-16 2012-10-18
        - 2008-01-09 to 2011-12-06 MRO CRISM TRDR 1,614,397 6,816,809 36,727,957.30
        2015-11-24 2015-11-24 - 2006-09-27 to 2015-05-09 MRO CRISM VALREP 280,501
        561,002 7,809.23 2015-11-24 2015-11-24 - 2006-09-27 to 2015-05-09 MRO CRISM
        (MSL Landing Site Selection) Mur_DL 170 4,930 1,199.04 2012-02-27 2014-08-22
        - - MRO CRISM (MSL Landing Site Selection) Mur_DS 171 3,931 1,439.53 2012-02-27
        2014-08-22 - - MRO CTX EDR 73,562 219,692 8,208,976.35 2015-12-01 2015-12-02
        -4242-41458 2005-08-30 to 2015-05-31 MRO CTX (MSL Landing Site Selection)
        MSSS_D 8 16 292.25 2012-02-27 2014-08-22 - - MRO HIRISE ANAGLY 4,474 13,422
        1,898,738.60 2015-12-02 2015-12-02 - - MRO HIRISE DTM 287 10,154 485,146.63
        2015-12-02 2015-12-02 - - MRO HIRISE EDR 1,076,299 5,341,954 33,097,547.17
        2015-12-02 2015-12-02 1-43443 2006-03-24 to 2015-11-02 MRO HIRISE RDR 11 223
        24,459.84 2012-02-24 2015-10-17 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE
        RDRV11 79,736 1,786,715 131,750,507.24 2015-12-02 2015-12-02 1-43443 2006-03-24
        to 2015-11-02 MRO HIRISE (MSL Landing Site Selection) Mcew_D 107 1,478 199,148.98
        2012-02-27 2012-10-19 - - MRO MCS DDR 17,584 70,336 131,864.23 2015-12-01
        2015-12-01 760-42242 2006-09-24 to 2015-07-31 MRO MCS EDR 18,126 54,378 287,943.94
        2015-11-30 2015-11-30 0-42242 2006-09-15 to 2015-07-31 MRO MCS RDR 18,121
        54,363 432,440.71 2015-11-30 2015-11-30 759-42242 2006-09-24 to 2015-07-31
        MRO RSS EDR 15,249 35,007 524,386.06 2015-11-30 2015-11-30 - 2006-01-01 to
        2017-01-02 MRO RSS RSDMAP 20 68 19.12 2012-03-01 2015-10-15 - 1998-03-27 to
        2008-10-31 MRO RSS SHADR 5 10 3.50 2012-03-01 2015-10-15 - 1998-03-27 to 2011-05-05
        MRO RSS SHBDR 2 4 946.92 2012-03-01 2015-10-15 - 2006-08-30 to 2008-10-31
        MRO SHARAD EDR 12,824 76,944 2,961,591.90 2015-05-29 2015-05-29 0-27071 2006-12-06
        to 2012-05-05 MRO SHARAD RDR 13,143 65,715 4,669,249.09 2015-05-29 2015-09-10
        1689-27431 2006-12-06 to 2012-06-02 MRO SHARAD USGEOM 16,276 32,552 5,599.47
        2015-10-01 2015-10-01 1689-41098 2006-12-06 to 2015-05-03 MRO SHARAD USRDR
        16,276 65,104 989,097.01 2015-10-02 2015-10-02 1689-41098 2006-12-06 to 2015-05-03
        Multiple Multiple (MSL Landing Site Selection) Cale_D 4 12 32.86 2012-02-27
        2014-08-22 - - Multiple Multiple (MSL Landing Site Selection) Golo_D 4 12
        6.10 2012-02-27 2014-08-22 - - Multiple Multiple (MSL Landing Site Selection)
        MXDMap 4 16 836.77 2012-02-27 2014-08-22 - - ODY GRS AHD 157 471 40.82 2015-10-13
        2015-10-13 - 2002-02-21 to 2015-03-27 ODY GRS AND 129 387 15.61 2015-10-13
        2015-10-13 - 2002-01-25 to 2015-03-27 ODY GRS CGS 28,918 86,754 675,993.58
        2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,572 10,716
        5,378.56 2015-07-01 2015-10-14 - 2001-04-25 to 2014-12-03 ODY GRS DHD 4,514
        13,542 2,089.01 2015-10-13 2015-10-13 - 2002-02-18 to 2015-03-31 ODY GRS DND
        3,178 9,534 3,250.53 2015-10-13 2015-10-13 - 2002-02-19 to 2015-03-31 ODY
        GRS EKERNL 302 1,206 4.86 2015-07-01 2015-10-14 - 2001-04-25 to 2014-12-03
        ODY GRS ELEMTS 24 163 212.34 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODY GRS GAMMAS 2,651 7,953 358,124.54 2012-03-30 2015-10-14 - 2001-05-02 to
        2009-09-30 ODY GRS GRSENG 10,012 456,280 40,651.77 2015-10-14 2015-10-14 -
        2001-04-25 to 2015-03-30 ODY GRS HENDS 4,738 14,214 16,864.78 2015-10-14 2015-10-14
        - 2001-05-02 to 2015-03-30 ODY GRS MESSLG 4,961 14,883 17,944.97 2015-10-14
        2015-10-14 - 2001-04-25 to 2015-03-30 ODY GRS NEUTNS 4,708 14,124 39,496.78
        2015-10-14 2015-10-14 - 2001-05-02 to 2015-03-30 ODY GRS PROFIL 2,365 7,095
        6,501.12 2012-03-30 2015-10-14 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621
        7,863 16,866.46 2012-03-30 2015-10-14 - 2001-05-02 to 2010-07-30 ODY GRS SGS
        2,733 8,199 25,478.17 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODY
        THEMIS IRBTR 185,290 662,569 444,045.50 2015-10-02 2015-10-02 816-58999 2002-02-19
        to 2015-04-02 ODY THEMIS IREDR 557,869 1,753,464 2,144,319.67 2015-10-02 2015-10-02
        816-58999 2002-02-19 to 2015-04-02 ODY THEMIS IRGEO1 68,063 461,143 2,217,907.58
        2014-10-30 2015-08-12 2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRGEO2
        46,563 294,992 2,165,588.98 2015-10-02 2015-10-02 52301-56799 2013-09-28 to
        2015-04-02 ODY THEMIS IRPBT1 67,829 135,658 300,874.95 2014-11-02 2015-08-12
        2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRPBT2 23,804 47,608 91,752.36
        2015-10-02 2015-10-02 52301-58999 2013-09-28 to 2015-04-02 ODY THEMIS IRRDR
        367,231 932,712 3,747,805.29 2015-10-02 2015-10-02 816-58999 2002-02-19 to
        2015-04-02 ODY THEMIS VGEO1 187,240 798,474 3,031,185.30 2014-11-19 2015-08-14
        816-52299 2002-02-19 to 2013-09-28 ODY THEMIS VGEO2 29,199 149,321 566,500.25
        2015-10-02 2015-10-02 52300-58999 2013-09-28 to 2015-04-02 ODY THEMIS VISABR
        205,972 686,885 1,077,127.30 2015-10-02 2015-10-02 816-58999 2002-02-19 to
        2015-04-02 ODY THEMIS VISALB 12,757 25,515 47,477.11 2015-10-02 2015-10-02
        52300-58998 2013-09-28 to 2015-04-02 ODY THEMIS VISEDR 206,514 681,264 1,116,289.57
        2015-10-02 2015-10-02 816-58999 2002-02-19 to 2015-04-02 ODY THEMIS VISRDR
        205,448 685,098 1,843,705.50 2015-10-02 2015-10-02 816-58999 2002-02-19 to
        2015-04-02 ODY THEMIS (MSL Landing Site Selection) Band_D 4 46 179.45 2012-02-27
        2014-08-22 - - ODY THEMIS (MSL Landing Site Selection) Ferg_D 16 100 1,152.61
        2012-02-27 2014-08-22 - - ODY THEMIS (MSL Landing Site Selection) Oste_D 8
        40 222.60 2012-02-27 2014-08-22 - - VO VISAB DTM 233 1,165 1,013.77 2012-09-14
        2014-08-22 - - VO VISAB EDR 50,506 353,542 95,216.20 2013-01-23 2014-08-24
        0-1485 1976-06-22 to 1980-07-30 VO VISAB MDIM 11,086 31,662 22,492.48 2013-11-05
        2014-08-22 169-1483 - Total 11,266,408 46,024,036 280,922,968.15 2015-12-07
        2015-12-07 - 1976-06-22 to 2071-01-16 Volume Table Volume Group Number Volumes
        Number Products Number Files File Size (MB) Last Time Product Added Last Time
        Synced Orbit Range Observation Range MEXHRS_1* 1 31,693 95,121 3,561,827.35
        2015-12-07 2015-12-07 10-7982 2004-01-10 to 2010-03-26 MEXHRS_2* 1 9,286 29,150
        611,336.64 2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEXHRSC_0*
        1 42,325 127,018 4,514,528.95 2015-02-21 2015-07-18 10-13323 2004-01-10 to
        2014-06-29 MEXHRSC_1* 1 34,811 104,470 5,050,302.40 2015-02-17 2015-08-01
        10-13323 2004-01-10 to 2014-06-29 MEXMDE_1* 2 5,412 11,528 8,443.02 2015-04-30
        2015-07-30 1885-3068 2005-07-04 to 2006-05-31 MEXMDI_1* 5 8,343 2,468,617
        295,762.04 2015-06-16 2015-06-16 1844-13649 2005-06-22 to 2014-10-02 MEXMDS_1*
        1 730 1,186 4,134.10 2015-04-29 2015-07-30 1885-2418 2005-07-04 to 2005-11-30
        MEXOMG_0* 5 22,623 22,909 929,297.52 2015-09-10 2015-09-10 -304-12797 2003-02-19
        to 2014-01-27 MEXOMG_2* 1 8 95 4,415.38 2015-04-29 2015-04-29 6-8485 2004-01-08
        to 2010-08-20 MEXPFS_1* 4 50,289 125,594 81,049.35 2015-04-30 2015-04-30 10-11451
        2003-05-02 to 2071-01-16 MGSL_2* 2 772 835 23,778.55 2009-03-11 2015-06-03
        0-20327 1997-09-15 to 2001-06-30 MGSL_3* 1 89 197 12,497.56 2009-03-11 2015-08-19
        3-20333 1997-09-15 to 2001-06-30 MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11
        2015-06-03 - 1999-02-28 to 2006-11-02 MGST_1* 326 326 52,004 202,080.67 2013-10-28
        2015-07-06 - - MGST_9* 1 4 31 162.43 2013-10-28 2015-06-03 - - MROCR_0* 8
        4,644,241 15,529,923 15,726,229.51 2015-11-24 2015-11-24 - 1980-01-01 to 2015-05-09
        MROCR_1* 7 869,199 1,740,185 3,175,755.23 2015-11-23 2015-11-23 - 2006-09-27
        to 2015-05-09 MROCR_2* 9 1,614,397 4,038,319 35,996,623.67 2015-11-24 2015-11-24
        - 2006-09-27 to 2015-05-09 MROCR_3* 4 17,671 36,258 3,751,632.75 2012-02-29
        2015-05-31 - - MROCR_4* 1 18 284 5,812.32 2012-03-16 2012-10-18 - 2008-01-09
        to 2011-12-06 MROCR_5* 6 4,404 10,170 9,574.83 2015-11-23 2015-11-23 - 2009-07-10
        to 2015-04-17 MROCR_6* 1 18 284 5,812.32 2012-03-16 2012-10-18 - 2008-01-09
        to 2011-12-06 MROHR_0* 1 1,160,807 4,446,823 146,540,305.59 2015-12-02 2015-12-02
        1-43443 2006-03-24 to 2015-11-02 MROM_0* 104 18,126 39,060 286,881.40 2015-11-30
        2015-11-30 0-42242 2006-09-15 to 2015-07-31 MROM_1* 103 18,121 41,097 431,338.05
        2015-11-30 2015-11-30 0-42242 2006-09-24 to 2015-07-31 MROM_2* 208 17,584
        38,912 133,084.93 2015-12-01 2015-12-01 0-42242 2006-09-24 to 2015-07-31 MRORS_0*
        1 15,249 30,618 524,157.20 2015-11-30 2015-11-30 - 2006-01-01 to 2017-01-02
        MRORS_1* 1 27 90 971.51 2012-03-01 2015-10-15 - 1998-03-27 to 2011-05-05 MROSH_0*
        3 12,824 39,105 2,960,781.44 2015-05-29 2015-05-29 0-27071 2006-12-06 to 2012-05-05
        MROSH_1* 3 13,143 53,205 4,668,481.07 2015-05-29 2015-09-10 1689-27431 2006-12-06
        to 2012-06-02 MROSH_2* 1 32,552 130,236 1,039,512.72 2015-10-02 2015-10-02
        1689-41098 2006-12-06 to 2015-05-03 MSL_0* 1 409 9,331 6,521.54 2012-02-27
        2014-08-22 - - VO_1* 46 50,506 254,044 92,585.84 2013-01-23 2014-08-24 0-1485
        1976-06-22 to 1980-07-30 VO_2* 22 11,319 34,771 20,117.24 2013-11-05 2014-08-22
        0-1483 - MGSC* 588 243,526 748,695 314,741.91 2013-11-05 2015-08-04 -97-33998
        1997-09-15 to 2006-10-17 MROX* 2,393 73,562 289,090 8,256,862.85 2015-12-01
        2015-12-02 -4242-41458 2005-08-30 to 2015-05-31 ODGC1* 1 28,918 57,867 675,600.75
        2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODGD1* 1 3,178 6,387 3,197.86
        2015-10-13 2015-10-13 - 2002-02-19 to 2015-03-31 ODGE1* 1 35,930 498,565 501,591.22
        2015-10-14 2015-10-14 - 2001-04-25 to 2015-03-30 ODGH1* 1 157 343 43.86 2015-10-13
        2015-10-13 - 2002-02-21 to 2015-03-27 ODGM* 1 24 99 71.59 2012-03-30 2015-10-13
        - 2002-06-04 to 2005-04-03 ODGN1* 1 129 287 18.76 2015-10-13 2015-10-13 -
        2002-01-25 to 2015-03-27 ODGR1* 1 4,514 9,057 2,067.37 2015-10-13 2015-10-13
        - 2002-02-18 to 2015-03-31 ODGS1* 1 2,733 5,496 25,446.75 2012-03-30 2015-10-13
        - 2002-06-08 to 2009-05-25 ODTH 2 2,163,779 4,028,472 17,478,420.07 2015-10-02
        2015-10-02 816-58999 2002-02-19 to 2015-04-02 Total 3,874 11,266,322 35,160,940
        257,973,945.65 2015-12-07 2015-12-07 - 1976-06-22 to 2071-01-16 Data Set /
        Product Type Product Files This is a count of the number of files for each
        product type. NOTE: This is largerthan the number of files in a volume since
        somes files (such as DSMAP.CAT) are included in each product even though they
        are only included once in a volume Data Set / Product Type Product File Sizes
        This is a sum of the sizes for each file for each product type. NOTE: This
        is largerthan the sum of the size of files in a volume since somes files (such
        as DSMAP.CAT) are included in each product even though they are only included
        once in a volume Last Time Product Added This is the last time any product
        in the given data set and product type or in the given volume was added to
        ODE Last Time Synced This is the last the volume or any volume containing
        the given data set with the given product type was synced with ODE. Syncing
        ensures that the contents of ODE matches the volume. This includes adding
        new products; updating metadata, browse, and location information; and removing
        any products listed in ODE that no longer appear in the volume (a rare event).
        Observation Range The observation range is taken from the products Utc Start
        and Stop time. There are a few products that have odd stop times (times later
        than the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_11_2015.html
    extraction_002:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_1_13_2022_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code for downloading data from the Orbital Data Explorer\
        \ (ODE) using STAC terminology, you need to identify key elements relevant\
        \ to accessing and navigating the data catalog. Here\u2019s a breakdown of\
        \ essential components for crafting your Python code:\n\n1. **Data Structure:**\n\
        \   - The data is organized by missions and instruments. Each entry is a combination\
        \ of a mission and an instrument, along with specific product types available\
        \ for that combination.\n\n2. **STAC Terminology:**\n   - **Collections:**\
        \ These could be mapped to combinations of missions and instruments. For instance,\
        \ \"EM16TGO CASSIS\" could be a collection name.\n   - **Items:** These may\
        \ represent individual product entries under each collection.\n   - **Assets:**\
        \ Each asset corresponds to the product files associated with a specific item.\n\
        \n3. **Key Attributes:**\n   - **Mission:** (e.g., EM16TGO, MEX, MRO)\n  \
        \ - **Instrument:** (e.g., CASSIS, HRSC, THEMIS)\n   - **Product Type:** (e.g.,\
        \ CALSC, RAWSC, EDR)\n   - **Number of Products:** Total products count for\
        \ that mission-instrument combination.\n   - **Number of Product Files:**\
        \ Total file counts per product type.\n   - **Product File Sizes (MB):** Total\
        \ file size in megabytes per product type.\n   - **Last Time Product Added:**\
        \ Date when a new product was last added for each entry.\n   - **Last Time\
        \ Synced:** Date when data was last synchronized with the ODE.\n   - **Orbit\
        \ Range and Observation Range:** Time frames or orbits when the data was collected\
        \ or observed.\n\n4. **Implementing STAC API Queries:**\n   - Use these attributes\
        \ to build queries against a STAC API endpoint. Organize collections by mission\
        \ and instrument, filter items by product type and date ranges, and retrieve\
        \ assets representing individual data files.\n\n5. **Example Python Code Skelton:**\n\
        \   - Set up a STAC client to interact with an ODE-like database (assuming\
        \ they provide a STAC-compliant API):\n   ```python\n   from pystac_client\
        \ import Client\n\n   # Initialize STAC client\n   stac_url = \"https://example.com/stac\"\
        \  # Replace with the actual endpoint\n   client = Client.open(stac_url)\n\
        \n   # Query for a specific collection\n   collection_id = \"EM16TGO_CASSIS_CALSC\"\
        \n   collection = client.get_collection(collection_id)\n\n   # Search items\
        \ within the collection and filter if necessary\n   search_results = client.search(\n\
        \       collections=[collection_id],\n       datetime=\"2018-04-28/2020-02-22\"\
        ,  # Example date range\n       max_items=10\n   )\n\n   for item in search_results.get_items():\n\
        \       print(item.id, item.datetime)\n       # Accessing assets (e.g., download\
        \ links) for each item\n       for asset_key, asset in item.assets.items():\n\
        \           print(asset.href)  # This is the URL to download the file\n  \
        \ ```\n   \nThese steps and considerations provide a conceptual guideline\
        \ for accessing and downloading data from the ODE using STAC terminology in\
        \ a Python environment. You may have to adapt the code based on actual ODE\
        \ API documentation and available libraries."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2022-01-13T12:51 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range EM16TGO CASSIS CALANC 2 4 67.11
        2021-03-09 2021-03-09 - - EM16TGO CASSIS CALSC 939,597 2,844,345 3,240,439.13
        2021-03-13 2021-04-19 1914-10034 2018-04-28 to 2020-02-22 EM16TGO CASSIS PARHK
        32,739 65,478 10,367.54 2021-11-05 2021-11-05 0-15390 2016-03-14 to 2021-05-05
        EM16TGO CASSIS RAWHK 59,153 118,306 12,688.32 2021-11-06 2021-11-12 0-15390
        2016-04-17 to 2021-05-05 EM16TGO CASSIS RAWSC 2,094,515 9,153,485 2,124,836.03
        2021-11-11 2021-11-12 0-15390 2016-04-07 to 2021-05-05 EM16TGO CASSIS TCHANC
        722 1,444 281.72 2021-02-26 2021-03-26 - 2016-04-07 to 2021-02-18 EM16TGO
        NOMAD CALSC 3,606 14,424 22,248.30 2021-02-13 2021-02-13 1829-0 2018-04-21
        to 2018-09-30 EM16TGO NOMAD PARHK 3,821 7,642 4,405.37 2021-11-05 2021-11-05
        9394-15390 2020-01-01 to 2021-05-05 EM16TGO NOMAD PARSC 11,952 23,904 2,665,543.59
        2021-11-05 2021-11-05 9408-15381 2020-01-02 to 2021-05-05 EM16TGO NOMAD RAWHK
        3,595 7,190 3,809.28 2021-11-05 2021-11-05 9394-15390 2020-01-01 to 2021-05-05
        EM16TGO NOMAD RAWSC 19,916 39,832 2,620,062.83 2021-11-05 2021-11-05 9395-15388
        2020-01-01 to 2021-05-05 EM16TGO NOMAD TCHANC 692 1,384 60.59 2021-02-13 2021-03-25
        - 2016-04-04 to 2021-01-07 MEX HRSC DTMRDR 9,286 73,532 616,779.10 2014-06-05
        2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEX HRSC RDR 42,325 253,950 4,513,168.59
        2015-02-21 2015-07-18 10-13323 2004-01-10 to 2014-06-29 MEX HRSC RDRV3 55,785
        334,710 5,694,647.08 2020-05-01 2020-05-01 10-19592 2004-01-10 to 2019-06-29
        MEX HRSC REFDR 34,811 243,677 5,049,869.79 2015-02-17 2015-08-01 10-13323
        2004-01-10 to 2014-06-29 MEX HRSC REFDR3 43,888 351,104 1,400,725.77 2020-05-18
        2020-05-18 10-19592 2004-01-10 to 2019-06-29 MEX MARSIS EDR 29,139 145,695
        116,795.97 2021-01-20 2021-01-20 1-20228 2003-06-16 to 2019-12-31 MEX MARSIS
        RDRAIS 11,273 3,846,404 463,738.95 2019-07-31 2019-07-31 1844-18349 2005-06-22
        to 2018-07-02 MEX MARSIS RDRSS 8,459 42,295 224,850.04 2021-01-21 2021-01-21
        1885-20221 2005-07-04 to 2019-12-29 MEX OMEGA DDRGM 8 46 1,476.99 2015-04-29
        2021-01-17 6-8485 2004-01-08 to 2010-08-20 MEX OMEGA EDR 30,739 116,828 1,611,909.18
        2021-11-19 2021-11-19 -304-21398 2003-02-19 to 2020-12-05 MEX PFS EDR 101,029
        383,657 141,480.66 2018-10-15 2021-01-18 20-17721 2003-06-23 to 2017-12-31
        MEX VMC EDR 54,791 161,056 21,619.72 2021-10-04 2021-10-04 -1-21486 2003-06-06
        to 2020-12-31 MEX VMC RDR 54,791 161,056 224,541.19 2021-10-04 2021-10-04
        -1-21486 2003-06-06 to 2020-12-31 MGS MOC-NA/WA NADSDP 1,234 3,641 5,062.84
        2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802
        191,485 204,048.94 2009-03-11 2015-08-04 -97-33982 1999-02-28 to 2006-10-15
        MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05 2015-07-16 - 1997-09-15 to
        1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340 60,892.12 2009-03-11 2015-08-04
        -97-33998 1999-02-28 to 2006-10-17 MGS MOLA MEGDR 89 445 12,514.18 2009-03-11
        2017-08-25 3-20333 1997-09-15 to 2001-06-30 MGS MOLA PEDR 771 7,710 23,968.75
        2009-03-11 2015-06-03 1578-20327 1999-02-28 to 2001-06-30 MGS MOLA PRDR 2,546
        7,638 40,139.32 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02 MGS MOLA
        SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15 to 1999-12-31 MGS TES TIMAP
        4 20 162.32 2013-10-28 2018-01-17 - - MGS TES TSDR 326 23,702 198,114.76 2013-10-28
        2015-07-06 - - MRO CRISM ANCILL 7,233 14,466 671.96 2021-11-30 2021-11-30
        - 2006-09-27 to 2021-08-08 MRO CRISM CDR 2,742,101 5,484,202 646,912.55 2021-11-30
        2021-11-30 - 1980-01-01 to 2021-08-09 MRO CRISM DDR 1,020,829 2,041,658 6,593,806.14
        2021-12-01 2021-12-01 - 2006-09-27 to 2021-08-08 MRO CRISM EDR 2,556,250 15,309,309
        28,199,609.26 2021-12-01 2021-12-01 - 2006-09-27 to 2021-08-08 MRO CRISM LDR
        5,928 11,856 12,307.65 2017-08-28 2021-02-10 - 2009-07-10 to 2017-04-29 MRO
        CRISM MRDR 17,671 49,087 3,751,401.26 2012-02-29 2014-08-22 - - MRO CRISM
        MTRDR 9,677 890,263 12,993,787.45 2021-09-27 2021-09-27 840-27269 2006-09-30
        to 2012-05-21 MRO CRISM TER 9,676 1,267,544 6,389,785.71 2021-09-27 2021-09-27
        840-27269 2006-09-30 to 2012-05-21 MRO CRISM TRDR 1,755,312 7,175,983 46,361,858.85
        2021-12-01 2021-12-01 - 2006-09-27 to 2021-08-08 MRO CRISM VALREP 405,424
        810,848 9,538.64 2021-12-01 2021-12-01 - 2006-09-27 to 2021-08-08 MRO CTX
        EDR 127,052 372,078 14,116,574.30 2021-12-01 2021-12-01 -4242-69593 2005-08-30
        to 2021-06-01 MRO HIRISE ANAGLY 7,183 21,549 2,636,495.20 2021-12-02 2021-12-02
        - - MRO HIRISE DTM 829 30,066 1,325,564.90 2021-12-02 2021-12-02 - - MRO HIRISE
        EDR 1,891,149 9,409,090 52,268,298.15 2021-12-03 2021-12-03 1-71597 2006-03-24
        to 2021-11-04 MRO HIRISE RDR 10 199 23,890.50 2012-02-24 2021-01-16 2-7519
        2006-03-25 to 2008-03-04 MRO HIRISE RDRV11 141,356 3,157,691 210,568,505.24
        2021-12-02 2021-12-02 1-71597 2006-03-24 to 2021-11-04 MRO MCS DDR 29,957
        119,828 224,885.75 2021-12-01 2021-12-01 760-70376 2006-09-24 to 2021-07-31
        MRO MCS EDR 30,686 92,058 485,263.91 2021-12-01 2021-12-01 0-70376 2006-09-15
        to 2021-07-31 MRO MCS RDR 30,680 92,040 729,908.96 2021-12-01 2021-12-01 759-70376
        2006-09-24 to 2021-07-31 MRO RSS EDR 26,930 61,187 877,946.40 2020-11-30 2020-11-30
        - 2006-01-01 to 2021-02-02 MRO RSS RSDMAP 30 98 593.09 2016-05-27 2020-10-30
        - 1998-03-27 to 2015-04-30 MRO RSS SHADR 8 16 6.25 2020-10-30 2020-10-30 -
        1998-03-27 to 2019-08-05 MRO RSS SHBDR 4 8 2,285.01 2017-02-27 2020-10-30
        - 1998-03-27 to 2015-04-30 MRO SHARAD EDR 30,574 183,444 7,489,066.27 2021-12-01
        2021-12-01 0-69294 2006-12-06 to 2021-05-08 MRO SHARAD RDR 30,570 152,850
        11,157,814.34 2021-12-01 2021-12-01 1689-69294 2006-12-06 to 2021-05-08 MRO
        SHARAD SHARAD3D 2 662 315,906.17 2021-11-03 2021-11-12 - 2006-12-06 to 2015-09-10
        MRO SHARAD USGEOM 25,853 51,706 8,807.13 2021-12-01 2021-12-01 1689-69450
        2006-12-06 to 2021-05-20 MRO SHARAD USGEOMV2 28,584 57,168 9,845.96 2021-12-07
        2021-12-07 1689-69498 2006-12-06 to 2021-05-24 MRO SHARAD USRDR 25,853 103,412
        1,555,441.95 2021-12-01 2021-12-01 1689-69450 2006-12-06 to 2021-05-20 MRO
        SHARAD USRDRV2 28,584 114,336 1,739,194.91 2021-12-08 2021-12-08 1689-69498
        2006-12-06 to 2021-05-24 ODY GRS AHD 234 702 60.84 2022-01-04 2022-01-04 -
        2002-02-21 to 2021-06-18 ODY GRS AND 422 1,266 51.06 2022-01-04 2022-01-04
        - 2002-01-25 to 2021-06-18 ODY GRS CGS 28,918 86,754 675,993.58 2012-03-30
        2015-10-13 - 2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,583 10,749 5,378.69
        2022-01-05 2022-01-05 - 2001-04-25 to 2021-05-12 ODY GRS DHD 6,721 20,163
        3,129.31 2022-01-04 2022-01-04 - 2002-02-18 to 2021-06-30 ODY GRS DND 10,857
        32,571 11,266.50 2022-01-04 2022-01-04 - 2002-02-19 to 2021-06-29 ODY GRS
        EKERNL 310 1,238 4.99 2022-01-05 2022-01-05 - 2001-04-25 to 2021-05-12 ODY
        GRS ELEMTS 24 163 212.34 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODY GRS GAMMAS 2,651 7,953 358,124.54 2018-10-03 2022-01-04 - 2001-05-02 to
        2009-09-30 ODY GRS GRSENG 14,530 627,555 52,539.77 2022-01-05 2022-01-05 -
        2001-04-25 to 2021-06-30 ODY GRS HENDS 6,974 20,922 25,068.46 2022-01-05 2022-01-05
        - 2001-05-02 to 2021-06-30 ODY GRS MESSLG 7,213 21,639 18,067.00 2022-01-05
        2022-01-05 - 2001-04-25 to 2021-06-30 ODY GRS NEUTNS 6,941 20,823 58,782.13
        2022-01-05 2022-01-05 - 2001-05-02 to 2021-06-30 ODY GRS PROFIL 2,365 7,095
        6,501.12 2018-10-03 2022-01-04 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621
        7,863 16,866.46 2018-10-03 2022-01-04 - 2001-05-02 to 2010-07-30 ODY GRS SGS
        2,733 8,199 25,478.17 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODY
        THEMIS IRBTR 303,782 1,136,489 678,435.72 2022-01-04 2022-01-04 816-86299
        2002-02-19 to 2021-05-29 ODY THEMIS IREDR 916,306 3,097,052 3,636,893.27 2022-01-04
        2022-01-04 816-86299 2002-02-19 to 2021-05-29 ODY THEMIS IRGEO1 68,063 461,143
        2,218,038.47 2014-10-30 2021-02-02 2400-52299 2002-06-30 to 2013-09-28 ODY
        THEMIS IRGEO2 282,605 1,857,258 11,551,487.81 2022-01-04 2022-01-04 - 2013-04-01
        to 2021-05-29 ODY THEMIS IRPBT1 67,829 135,658 301,010.61 2014-11-02 2021-02-07
        2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRPBT2 144,493 433,477 1,876,153.59
        2022-01-05 2022-01-05 50114-86299 2013-04-01 to 2021-05-29 ODY THEMIS IRRDR
        604,198 1,643,857 6,405,006.52 2022-01-04 2022-01-04 816-86299 2002-02-19
        to 2021-05-29 ODY THEMIS VGEO1 187,241 798,478 3,031,301.96 2016-11-03 2021-02-13
        816-52299 2002-02-19 to 2013-09-28 ODY THEMIS VGEO2 131,903 699,901 3,001,180.30
        2022-01-04 2022-01-04 50100-86296 2013-03-31 to 2021-05-28 ODY THEMIS VISABR
        264,221 919,877 1,248,850.88 2022-01-04 2022-01-04 816-86296 2002-02-19 to
        2021-05-28 ODY THEMIS VISALB 57,542 172,625 684,971.55 2022-01-04 2022-01-04
        50100-86296 2013-03-31 to 2021-05-28 ODY THEMIS VISEDR 264,869 921,998 1,382,807.92
        2022-01-04 2022-01-04 816-86296 2002-02-19 to 2021-05-28 ODY THEMIS VISRDR
        263,695 918,178 2,320,879.10 2022-01-04 2022-01-04 816-86296 2002-02-19 to
        2021-05-28 VO VISAB DTM 233 1,165 1,013.77 2012-09-14 2021-01-22 - - VO VISAB
        EDR 50,506 353,542 95,216.20 2013-01-23 2021-01-22 0-1485 1976-06-22 to 1980-07-30
        VO VISAB MDIM 5,137 6,125 4,657.36 2017-02-17 2021-01-22 - - VO VISAB MDIMC
        3,826 3,826 3,827.60 2013-11-05 2021-01-22 169-1483 1977-02-07 to 1980-07-27
        VO VISAB MDIMH 2,116 2,116 3,221.25 2012-09-14 2021-01-22 - - Total 18,595,554
        80,432,989 481,530,403.86 2022-01-05 2022-01-05 - 1976-06-22 to 2021-11-04
        Volume Table Volume Group Number Volumes Number Products Number Files File
        Size (MB) Last Time Product Added Last Time Synced Orbit Range Observation
        Range em16_t* 2 3,170,310 13,960,781 11,260,047.69 2021-11-11 2021-11-12 0-15390
        2016-03-14 to 2021-05-05 MEXHRS_1* 2 99,673 386,875 12,992,205.60 2020-05-18
        2020-05-18 10-19592 2004-01-10 to 2019-06-29 MEXHRS_2* 1 9,286 29,150 611,336.64
        2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEXHRS_5* 1 42,325
        127,018 4,514,528.95 2015-02-21 2015-04-30 10-13323 2004-01-10 to 2014-06-29
        MEXMDE_1* 1 1,818 4,132 2,920.77 2015-04-29 2015-07-30 1885-2418 2005-07-04
        to 2005-11-30 MEXMDI_1* 7 11,273 3,845,848 465,338.61 2019-07-31 2019-07-31
        1844-18349 2005-06-22 to 2018-07-02 MEXME_1* 8 29,139 87,951 116,948.62 2021-01-20
        2021-01-20 1-20228 2003-06-16 to 2019-12-31 MEXMRS_1* 8 8,459 34,504 226,401.36
        2021-01-21 2021-01-21 1885-20221 2005-07-04 to 2019-12-29 MEXOMG_0* 8 30,739
        31,216 1,611,765.01 2021-11-19 2021-11-19 -304-21398 2003-02-19 to 2020-12-05
        MEXOMG_2* 1 8 95 4,415.38 2015-04-29 2021-01-17 6-8485 2004-01-08 to 2010-08-20
        MEXPFS_1* 7 101,029 202,751 139,801.03 2018-10-15 2021-01-18 20-17721 2003-06-23
        to 2017-12-31 MEXVMC_L* 16 109,582 438,888 255,897.49 2021-10-04 2021-10-04
        -1-21486 2003-06-06 to 2020-12-31 MGSL_2* 2 772 835 23,778.55 2009-03-11 2015-06-03
        0-20327 1997-09-15 to 2001-06-30 MGSL_3* 1 89 290 12,497.94 2009-03-11 2017-08-25
        3-20333 1997-09-15 to 2001-06-30 MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11
        2015-06-03 - 1999-02-28 to 2006-11-02 MGST_1* 326 326 52,004 202,080.67 2013-10-28
        2015-07-06 - - MGST_9* 1 4 31 162.43 2013-10-28 2018-01-17 - - MROCR_0* 14
        5,711,008 19,662,412 28,704,303.93 2021-12-01 2021-12-01 - 1980-01-01 to 2021-08-09
        MROCR_1* 13 1,020,829 2,044,549 6,595,234.60 2021-12-01 2021-12-01 - 2006-09-27
        to 2021-08-08 MROCR_2* 15 1,755,312 4,545,989 45,520,959.65 2021-12-01 2021-12-01
        - 2006-09-27 to 2021-08-08 MROCR_3* 4 17,671 35,990 3,751,409.79 2012-02-29
        2021-02-11 - - MROCR_4* 1 9,677 870,873 12,934,553.66 2021-09-27 2021-09-27
        840-27269 2006-09-30 to 2012-05-21 MROCR_5* 8 5,928 13,136 12,440.17 2017-08-28
        2021-02-10 - 2009-07-10 to 2017-04-29 MROCR_6* 1 9,676 1,257,752 6,332,444.09
        2021-09-27 2021-09-27 840-27269 2006-09-30 to 2012-05-21 MROHR_0* 1 2,040,527
        7,863,286 232,777,857.25 2021-12-03 2021-12-03 1-71597 2006-03-24 to 2021-11-04
        MROM_0* 176 30,686 66,124 483,657.32 2021-12-01 2021-12-01 0-70376 2006-09-15
        to 2021-07-31 MROM_1* 174 30,680 69,722 728,241.47 2021-12-01 2021-12-01 0-70376
        2006-09-24 to 2021-07-31 MROM_2* 349 29,957 66,331 227,195.61 2021-12-01 2021-12-01
        0-70376 2006-09-24 to 2021-07-31 MRORS_0* 1 26,930 54,012 877,572.26 2020-11-30
        2020-11-30 - 2006-01-01 to 2021-02-02 MRORS_1* 1 42 1,121 3,343.77 2020-10-30
        2020-10-30 - 1998-03-27 to 2019-08-05 MROSH_0* 4 30,574 92,566 7,487,112.74
        2021-12-01 2021-12-01 0-69294 2006-12-06 to 2021-05-08 MROSH_1* 4 30,570 123,124
        11,156,008.68 2021-12-01 2021-12-01 1689-69294 2006-12-06 to 2021-05-08 MROSH_2*
        2 108,660 434,696 3,452,846.57 2021-12-08 2021-12-08 1689-69498 2006-12-06
        to 2021-05-24 MROSH_3* 1 2 720 580,261.43 2021-11-03 2021-11-12 - 2006-12-06
        to 2015-09-10 VO_1* 46 50,506 254,044 92,585.84 2013-01-23 2021-01-22 0-1485
        1976-06-22 to 1980-07-30 VO_2* 22 11,312 19,920 12,984.82 2017-02-17 2021-01-22
        0-1483 1977-02-07 to 1980-07-27 MGSC* 588 243,526 748,695 314,741.91 2013-11-05
        2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX* 4,098 127,052 490,924
        14,259,419.41 2021-12-01 2021-12-01 -4242-69593 2005-08-30 to 2021-06-01 ODGC1*
        1 28,918 57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07
        ODGD1* 1 5,925 11,881 6,129.73 2022-01-04 2022-01-04 - 2002-02-19 to 2021-06-29
        ODGE1* 1 47,188 678,810 540,999.92 2022-01-05 2022-01-05 - 2001-04-25 to 2021-06-30
        ODGH1* 1 234 497 63.38 2022-01-04 2022-01-04 - 2002-02-21 to 2021-06-18 ODGM*
        1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03 ODGN1* 1 227
        485 37.04 2022-01-04 2022-01-04 - 2002-01-25 to 2021-06-18 ODGR1* 1 6,721
        13,471 3,095.12 2022-01-04 2022-01-04 - 2002-02-18 to 2021-06-30 ODGS1* 1
        2,733 5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH
        2 3,556,747 6,511,265 36,415,871.13 2022-01-05 2022-01-05 816-86299 2002-02-19
        to 2021-05-29 Total 5,926 18,557,220 65,203,338 446,452,704.68 2022-01-05
        2022-01-05 - 1976-06-22 to 2021-11-04 Data Set / Product Type Product Files
        This is a count of the number of files for each product type. NOTE: This is
        largerthan the number of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Data Set / Product Type Product File Sizes This is a sum of the sizes
        for each file for each product type. NOTE: This is largerthan the sum of the
        size of files in a volume since somes files (such as DSMAP.CAT) are included
        in each product even though they are only included once in a volume Last Time
        Product Added This is the last time any product in the given data set and
        product type or in the given volume was added to ODE Last Time Synced This
        is the last the volume or any volume containing the given data set with the
        given product type was synced with ODE. Syncing ensures that the contents
        of ODE matches the volume. This includes adding new products; updating metadata,
        browse, and location information; and removing any products listed in ODE
        that no longer appear in the volume (a rare event). Observation Range The
        observation range is taken from the products Utc Start and Stop time. There
        are a few products that have odd stop times (times later than the current
        date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_13_2022.html
    extraction_003:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_1_15_2017_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology,\
        \ you will need to focus on identifying the elements that are relevant to\
        \ constructing a search query for the data sets. Here's a breakdown of the\
        \ relevant parts of the provided text, organized to facilitate building STAC\
        \ search queries:\n\n1. **Missions and Instruments**: \n   - Missions: MEX\
        \ (Mars Express), MGS (Mars Global Surveyor), MRO (Mars Reconnaissance Orbiter),\
        \ ODY (Mars Odyssey), VO (Viking Orbiter).\n   - Instruments: HRSC, MARSIS,\
        \ OMEGA, PFS, MOC-NA/WA, MOLA, TES, CRISM, CTX, HIRISE, MCS, RSS, SHARAD,\
        \ THEMIS, GRS.\n\n2. **Product Types**: Examples include DTMRDR, RDR, EDR,\
        \ NADSDP, MEGDR, VALREP, THEMIS IRBTR, VISAB EDR, etc. Each product type may\
        \ correspond to different types of data or processing levels.\n\n3. **File\
        \ Information**:\n   - `Product Files`: The count of files for each product\
        \ type.\n   - `Product File Size (MB)`: The aggregated size of files for each\
        \ product type.\n\n4. **Temporal Information**:\n   - `Last Time Product Added`:\
        \ The date when the last product was added to the ODE for a specific dataset\
        \ and product type.\n   - `Observation Range`: Specifies the time period during\
        \ which the data was observed (e.g., 2004-01-10 to 2009-02-12).\n\n5. **Spatial\
        \ Information (Orbit Range)**:\n   - The range of orbits covered by the dataset,\
        \ for example, `10-6567` for MEX HRSC DTMRDR.\n\n6. **Additional Considerations**:\
        \ \n   - Make note of the last time the dataset was synchronized with ODE\
        \ (`Last Time Synced`).\n\nWith these elements in mind, you can write queries\
        \ or scripts to interact with an API (should it exist for ODE) or process\
        \ datasets that fit certain criteria (e.g., collected by MEX using HRSC between\
        \ specific observation dates). An example Python script could look somewhat\
        \ like this pseudocode:\n\n```python\nimport requests\n\ndef fetch_data_from_ode(mission,\
        \ instrument, product_type, start_date, end_date):\n    base_url = \"http://api.ode.url/stac/search\"\
        \  # Hypothetical URL\n    query_params = {\n        \"mission\": mission,\n\
        \        \"instrument\": instrument,\n        \"product_type\": product_type,\n\
        \        \"datetime\": f\"{start_date}/{end_date}\",\n    }\n    response\
        \ = requests.get(base_url, params=query_params)\n    if response.status_code\
        \ == 200:\n        data = response.json()\n        return data.get('features',\
        \ [])\n    else:\n        print(\"Error fetching data:\", response.status_code)\n\
        \        return []\n\n# Example usage\ndata = fetch_data_from_ode('MEX', 'HRSC',\
        \ 'DTMRDR', '2004-01-10', '2009-02-12')\n```\n\nThis pseudocode defines a\
        \ function that forms and sends a query based on mission, instrument, product\
        \ type, and observation date range. It assumes there is an accessible API\
        \ endpoint accepting STAC-like queries. You'll need to adapt this example\
        \ to match the specifics of ODE's data access capabilities."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2017-01-15T08:20 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range MEX HRSC DTMRDR 9,286 73,532
        616,779.10 2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEX HRSC
        RDR 42,325 253,950 4,513,168.59 2015-02-21 2015-07-18 10-13323 2004-01-10
        to 2014-06-29 MEX HRSC RDRV3 47,726 286,356 4,989,519.30 2017-01-13 2017-01-13
        10-15836 2004-01-10 to 2016-06-30 MEX HRSC REFDR 34,811 243,677 5,049,869.79
        2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29 MEX HRSC REFDR3 31,960
        255,680 1,047,298.75 2017-01-03 2017-01-03 10-10694 2004-01-10 to 2012-05-24
        MEX MARSIS EDR 5,412 10,824 8,183.68 2015-04-30 2015-07-30 1885-3068 2005-07-04
        to 2006-05-31 MEX MARSIS EDRV2 5,412 10,824 8,183.68 2015-04-19 2015-04-19
        1885-3068 2005-07-04 to 2006-05-31 MEX MARSIS RDRAIS 9,761 3,120,276 373,209.22
        2016-09-14 2016-09-14 1844-15519 2005-06-22 to 2016-03-30 MEX MARSIS RDRSS
        730 1,460 3,893.74 2015-04-29 2015-07-30 1885-2418 2005-07-04 to 2005-11-30
        MEX MARSIS RDRSS2 730 1,460 3,893.17 2012-02-24 2012-10-20 1885-2418 2005-07-04
        to 2005-11-30 MEX OMEGA DDRGM 8 46 1,476.99 2015-04-29 2015-04-29 6-8485 2004-01-08
        to 2010-08-20 MEX OMEGA EDR 24,939 93,628 1,103,947.47 2016-12-01 2016-12-01
        -304-15198 2003-02-19 to 2015-12-27 MEX PFS EDR 77,551 294,463 107,827.05
        2016-10-28 2016-11-16 20-13959 2003-06-23 to 2014-12-31 MGS MOC-NA/WA NADSDP
        1,234 3,641 5,062.84 2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS
        MOC-NA/WA NASDP 95,802 191,485 204,048.94 2009-03-11 2015-08-04 -97-33982
        1999-02-28 to 2006-10-15 MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05
        2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340
        60,892.12 2009-03-11 2015-08-04 -97-33998 1999-02-28 to 2006-10-17 MGS MOLA
        MEGDR 89 267 12,497.36 2009-03-11 2015-08-19 3-20333 1997-09-15 to 2001-06-30
        MGS MOLA PEDR 771 7,710 23,968.75 2009-03-11 2015-06-03 1578-20327 1999-02-28
        to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,139.32 2009-03-11 2015-06-03 -
        1999-02-28 to 2006-11-02 MGS MOLA SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15
        to 1999-12-31 MGS TES TIMAP 4 20 162.32 2013-10-28 2015-06-03 - - MGS TES
        TSDR 326 23,702 198,114.76 2013-10-28 2015-07-06 - - MRO CRISM ANCILL 5,286
        10,572 624.18 2016-11-29 2016-11-29 - 2006-09-27 to 2016-08-08 MRO CRISM CDR
        2,501,952 5,003,904 503,125.47 2016-11-29 2016-11-29 - 1980-01-01 to 2016-08-09
        MRO CRISM DDR 903,293 1,806,586 3,823,036.77 2016-11-29 2016-11-29 - 2006-09-27
        to 2016-08-08 MRO CRISM EDR 2,101,503 12,599,347 17,978,345.95 2016-11-30
        2016-11-30 - 2006-09-27 to 2016-08-08 MRO CRISM LDR 5,304 10,608 11,012.40
        2016-11-29 2016-11-29 - 2009-07-10 to 2016-07-06 MRO CRISM MRDR 17,671 49,087
        3,751,401.26 2012-02-29 2014-08-22 - - MRO CRISM MTRDR 1,232 113,344 1,566,859.01
        2016-11-07 2016-11-07 1360-9527 2006-11-10 to 2008-08-07 MRO CRISM TER 1,232
        161,392 812,042.81 2016-11-07 2016-11-22 1360-9527 2006-11-10 to 2008-08-07
        MRO CRISM TRDR 1,655,961 6,977,140 39,727,973.93 2016-11-30 2016-11-30 - 2006-09-27
        to 2016-08-08 MRO CRISM VALREP 308,747 617,494 8,478.54 2016-11-30 2016-11-30
        - 2006-09-27 to 2016-08-08 MRO CTX EDR 81,196 242,594 8,918,220.95 2016-12-02
        2016-12-02 -4242-46156 2005-08-30 to 2016-05-31 MRO HIRISE ANAGLY 4,936 14,808
        2,041,128.95 2017-01-06 2017-01-06 - - MRO HIRISE DTM 367 12,909 605,988.25
        2017-01-06 2017-01-06 - - MRO HIRISE EDR 1,256,874 6,243,121 37,496,172.91
        2017-01-06 2017-01-06 1-48599 2006-03-24 to 2016-12-08 MRO HIRISE RDR 11 223
        24,459.84 2012-02-24 2015-10-17 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE
        RDRV11 93,592 2,097,325 149,782,456.31 2017-01-06 2017-01-06 1-48599 2006-03-24
        to 2016-12-08 MRO MCS DDR 19,685 78,740 145,603.67 2016-11-30 2016-11-30 760-46939
        2006-09-24 to 2016-07-31 MRO MCS EDR 20,234 60,702 320,978.50 2016-11-30 2016-11-30
        0-46939 2006-09-15 to 2016-07-31 MRO MCS RDR 20,228 60,684 482,266.06 2016-11-30
        2016-11-30 759-46939 2006-09-24 to 2016-07-31 MRO RSS EDR 17,308 39,635 589,585.57
        2016-11-30 2016-11-30 - 2006-01-01 to 2017-01-29 MRO RSS RSDMAP 30 98 593.09
        2016-05-27 2016-11-29 - 1998-03-27 to 2015-04-30 MRO RSS SHADR 7 14 5.33 2016-05-27
        2016-11-29 - 1998-03-27 to 2015-04-30 MRO RSS SHBDR 3 6 1,427.61 2016-02-26
        2016-11-29 - 1998-03-27 to 2015-03-30 MRO SHARAD EDR 12,824 76,944 2,961,591.90
        2015-05-29 2015-05-29 0-27071 2006-12-06 to 2012-05-05 MRO SHARAD RDR 13,143
        65,715 4,669,249.09 2015-05-29 2015-09-10 1689-27431 2006-12-06 to 2012-06-02
        MRO SHARAD USGEOM 17,041 34,082 5,805.15 2016-08-26 2016-08-26 1689-44699
        2006-12-06 to 2016-02-08 MRO SHARAD USRDR 17,041 68,164 1,025,229.42 2016-08-26
        2016-08-26 1689-44699 2006-12-06 to 2016-02-08 ODY GRS AHD 171 513 44.46 2016-12-22
        2016-12-22 - 2002-02-21 to 2016-06-08 ODY GRS AND 143 429 17.42 2016-12-22
        2016-12-22 - 2002-01-25 to 2016-06-08 ODY GRS CGS 28,918 86,754 675,993.58
        2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,575 10,725
        5,378.60 2016-12-23 2016-12-23 - 2001-04-25 to 2016-04-04 ODY GRS DHD 4,964
        14,892 2,301.06 2016-12-22 2016-12-22 - 2002-02-18 to 2016-06-30 ODY GRS DND
        3,620 10,860 3,714.17 2016-12-22 2016-12-22 - 2002-02-19 to 2016-06-30 ODY
        GRS EKERNL 305 1,218 4.92 2016-12-23 2016-12-23 - 2001-04-25 to 2016-04-04
        ODY GRS ELEMTS 24 163 212.34 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODY GRS GAMMAS 2,651 7,953 358,124.54 2012-03-30 2016-12-23 - 2001-05-02 to
        2009-09-30 ODY GRS GRSENG 10,919 490,746 43,037.56 2016-12-23 2016-12-23 -
        2001-04-25 to 2016-06-30 ODY GRS HENDS 5,188 15,564 18,514.08 2016-12-23 2016-12-23
        - 2001-05-02 to 2016-06-30 ODY GRS MESSLG 5,418 16,254 17,969.58 2016-12-23
        2016-12-23 - 2001-04-25 to 2016-06-30 ODY GRS NEUTNS 5,157 15,471 43,361.86
        2016-12-23 2016-12-23 - 2001-05-02 to 2016-06-30 ODY GRS PROFIL 2,365 7,095
        6,501.12 2012-03-30 2016-12-23 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621
        7,863 16,866.46 2012-03-30 2016-12-23 - 2001-05-02 to 2010-07-30 ODY GRS SGS
        2,733 8,199 25,478.17 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODY
        THEMIS IRBTR 207,155 750,029 494,115.70 2017-01-04 2017-01-04 816-64499 2002-02-19
        to 2016-06-28 ODY THEMIS IREDR 624,096 2,026,022 2,457,286.91 2017-01-04 2017-01-04
        816-64499 2002-02-19 to 2016-06-28 ODY THEMIS IRGEO1 68,063 461,143 2,217,907.58
        2014-10-30 2016-11-04 2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRGEO2
        86,324 550,858 4,017,489.55 2017-01-05 2017-01-05 52301-54499 2013-09-28 to
        2016-06-28 ODY THEMIS IRPBT1 67,829 135,658 300,874.95 2014-11-02 2016-11-05
        2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRPBT2 43,964 87,928 180,550.66
        2017-01-05 2017-01-05 52301-64499 2013-09-28 to 2016-06-28 ODY THEMIS IRRDR
        410,944 1,063,743 4,309,451.38 2017-01-04 2017-01-04 816-64499 2002-02-19
        to 2016-06-28 ODY THEMIS VGEO1 187,241 798,478 3,031,198.02 2016-11-03 2016-11-09
        816-52299 2002-02-19 to 2013-09-28 ODY THEMIS VGEO2 51,324 270,776 1,103,059.02
        2017-01-04 2017-01-04 52300-64496 2013-09-28 to 2016-06-28 ODY THEMIS VISABR
        219,164 739,652 1,115,678.79 2017-01-04 2017-01-04 816-64496 2002-02-19 to
        2016-06-28 ODY THEMIS VISALB 18,476 36,953 58,787.28 2017-01-04 2017-01-04
        52300-64496 2013-09-28 to 2016-06-28 ODY THEMIS VISEDR 219,708 741,351 1,176,752.98
        2017-01-04 2017-01-04 816-64496 2002-02-19 to 2016-06-28 ODY THEMIS VISRDR
        218,639 737,862 1,952,155.44 2017-01-04 2017-01-04 816-64496 2002-02-19 to
        2016-06-28 VO VISAB DTM 233 1,165 1,013.77 2012-09-14 2014-08-22 - - VO VISAB
        EDR 50,506 353,542 95,216.20 2013-01-23 2014-08-24 0-1485 1976-06-22 to 1980-07-30
        VO VISAB MDIM 11,086 31,662 22,492.48 2013-11-05 2014-08-22 169-1483 - Total
        12,178,139 51,101,176 319,377,985.60 2017-01-13 2017-01-13 - 1976-06-22 to
        2017-01-29 Volume Table Volume Group Number Volumes Number Products Number
        Files File Size (MB) Last Time Product Added Last Time Synced Orbit Range
        Observation Range MEXHRS_1* 2 79,686 303,058 10,813,156.75 2017-01-13 2017-01-13
        10-15836 2004-01-10 to 2016-06-30 MEXHRS_2* 1 9,286 29,150 611,336.64 2014-06-05
        2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEXHRS_5* 1 42,325 127,018 4,514,528.95
        2015-02-21 2015-04-30 10-13323 2004-01-10 to 2014-06-29 MEXHRSC_1* 1 34,811
        104,470 5,050,302.40 2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29
        MEXMDE_1* 2 5,412 11,528 8,443.02 2015-04-30 2015-07-30 1885-3068 2005-07-04
        to 2006-05-31 MEXMDI_1* 6 9,761 3,120,792 374,488.71 2016-09-14 2016-09-14
        1844-15519 2005-06-22 to 2016-03-30 MEXMDS_1* 1 730 1,186 4,134.10 2015-04-29
        2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEXOMG_0* 6 24,939 25,285 1,103,812.56
        2016-12-01 2016-12-01 -304-15198 2003-02-19 to 2015-12-27 MEXOMG_2* 1 8 95
        4,415.38 2015-04-29 2015-04-29 6-8485 2004-01-08 to 2010-08-20 MEXPFS_1* 5
        77,551 155,597 106,546.33 2016-10-28 2016-11-16 20-13959 2003-06-23 to 2014-12-31
        MGSL_2* 2 772 835 23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30
        MGSL_3* 1 89 197 12,497.56 2009-03-11 2015-08-19 3-20333 1997-09-15 to 2001-06-30
        MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02
        MGST_1* 326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31
        162.43 2013-10-28 2015-06-03 - - MROCR_0* 9 4,917,488 16,531,757 18,357,784.13
        2016-11-30 2016-11-30 - 1980-01-01 to 2016-08-09 MROCR_1* 8 903,293 1,808,561
        3,824,286.00 2016-11-29 2016-11-29 - 2006-09-27 to 2016-08-08 MROCR_2* 10
        1,655,961 4,161,979 38,948,228.94 2016-11-30 2016-11-30 - 2006-09-27 to 2016-08-08
        MROCR_3* 4 17,671 36,258 3,751,632.75 2012-02-29 2015-05-31 - - MROCR_4* 1
        1,232 111,133 1,566,486.98 2016-11-07 2016-11-07 1360-9527 2006-11-10 to 2008-08-07
        MROCR_5* 7 5,304 12,130 11,462.77 2016-11-29 2016-11-29 - 2009-07-10 to 2016-07-06
        MROCR_6* 1 1,232 160,412 811,694.40 2016-11-07 2016-11-22 1360-9527 2006-11-10
        to 2008-08-07 MROHR_0* 1 1,355,780 5,205,754 166,177,510.20 2017-01-06 2017-01-06
        1-48599 2006-03-24 to 2016-12-08 MROM_0* 116 20,234 43,600 319,813.10 2016-11-30
        2016-11-30 0-46939 2006-09-15 to 2016-07-31 MROM_1* 115 20,228 45,875 481,053.38
        2016-11-30 2016-11-30 0-46939 2006-09-24 to 2016-07-31 MROM_2* 232 19,685
        43,546 146,984.65 2016-11-30 2016-11-30 0-46939 2006-09-24 to 2016-07-31 MRORS_0*
        1 17,308 34,744 589,330.33 2016-11-30 2016-11-30 - 2006-01-01 to 2017-01-29
        MRORS_1* 1 40 1,117 2,485.46 2016-05-27 2016-11-29 - 1998-03-27 to 2015-04-30
        MROSH_0* 3 12,824 39,105 2,960,781.44 2015-05-29 2015-05-29 0-27071 2006-12-06
        to 2012-05-05 MROSH_1* 3 13,143 53,205 4,668,481.07 2015-05-29 2015-09-10
        1689-27431 2006-12-06 to 2012-06-02 MROSH_2* 1 34,082 136,356 1,077,485.93
        2016-08-26 2016-08-26 1689-44699 2006-12-06 to 2016-02-08 MSL_0* 1 409 9,331
        6,521.54 2012-02-27 2014-08-22 - - VO_1* 46 50,506 254,044 92,585.84 2013-01-23
        2014-08-24 0-1485 1976-06-22 to 1980-07-30 VO_2* 22 11,319 34,771 20,117.24
        2013-11-05 2014-08-22 0-1483 - MGSC* 588 243,526 748,695 314,741.91 2013-11-05
        2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX* 2,598 81,196 317,937 8,974,876.33
        2016-12-02 2016-12-02 -4242-46156 2005-08-30 to 2016-05-31 ODGC1* 1 28,918
        57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODGD1*
        1 3,620 7,271 3,653.69 2016-12-22 2016-12-22 - 2002-02-19 to 2016-06-30 ODGE1*
        1 38,199 534,851 509,497.84 2016-12-23 2016-12-23 - 2001-04-25 to 2016-06-30
        ODGH1* 1 171 371 47.42 2016-12-22 2016-12-22 - 2002-02-21 to 2016-06-08 ODGM*
        1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03 ODGN1* 1 143
        315 20.54 2016-12-22 2016-12-22 - 2002-01-25 to 2016-06-08 ODGR1* 1 4,964
        9,957 2,276.87 2016-12-22 2016-12-22 - 2002-02-18 to 2016-06-30 ODGS1* 1 2,733
        5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH 2 2,422,927
        4,492,202 21,008,681.98 2017-01-05 2017-01-05 816-64499 2002-02-19 to 2016-06-28
        Total 4,135 12,172,406 38,835,097 298,199,413.42 2017-01-13 2017-01-13 - 1976-06-22
        to 2017-01-29 Data Set / Product Type Product Files This is a count of the
        number of files for each product type. NOTE: This is largerthan the number
        of files in a volume since somes files (such as DSMAP.CAT) are included in
        each product even though they are only included once in a volume Data Set
        / Product Type Product File Sizes This is a sum of the sizes for each file
        for each product type. NOTE: This is largerthan the sum of the size of files
        in a volume since somes files (such as DSMAP.CAT) are included in each product
        even though they are only included once in a volume Last Time Product Added
        This is the last time any product in the given data set and product type or
        in the given volume was added to ODE Last Time Synced This is the last the
        volume or any volume containing the given data set with the given product
        type was synced with ODE. Syncing ensures that the contents of ODE matches
        the volume. This includes adding new products; updating metadata, browse,
        and location information; and removing any products listed in ODE that no
        longer appear in the volume (a rare event). Observation Range The observation
        range is taken from the products Utc Start and Stop time. There are a few
        products that have odd stop times (times later than the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_15_2017.html
    extraction_004:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_1_21_2025_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code for downloading data from the Orbital Data Explorer\
        \ (ODE) using STAC (SpatioTemporal Asset Catalog) terminology, the relevant\
        \ information to extract from the provided text includes the following:\n\n\
        1. **Missions and Instruments**: Recognize the different missions and instruments\
        \ available in the data. The data includes various missions like EM16TGO,\
        \ MEX, MGS, MRO, ODY, and VO, with instruments such as ACS, CASSIS, NOMAD,\
        \ HRSC, MARSIS, OMEGA, PFS, VMC, and others.\n\n2. **Product Types**: Each\
        \ mission and instrument combination has various product types associated\
        \ with it, such as RAWHK, RAWSC, CALANC, CALSC, DERSC, PARHK, TCHANC, ANAGLY,\
        \ DTM, EDR, RDR, TER, etc.\n\n3. **Product Information**: For each product\
        \ type, there are details about:\n   - The number of products.\n   - The number\
        \ of product files.\n   - The total file size of the products.\n   - The last\
        \ time a product was added.\n   - The last time the data was synced.\n   -\
        \ The orbit range and the observation range.\n\n4. **STAC Terminology Integration**:\n\
        \   - **Collections**: Define each mission as a collection in the STAC catalog.\n\
        \   - **Items**: Each product type can be an item within the collection.\n\
        \   - **Assets**: The actual downloadable files and their metadata could be\
        \ considered as assets within each item.\n   - **Temporal and Spatial Metadata**:\
        \ Incorporate the observation range and orbit range within the STAC metadata.\n\
        \n5. **Example STAC Fields**:\n   - `id`: A unique identifier for each collection,\
        \ item, and asset.\n   - `bbox`: The bounding box (if spatial extent is available).\n\
        \   - `datetime`: The date-time derived from the observation range start.\n\
        \   - `properties`: Additional metadata like product type, number of files,\
        \ file size, etc.\n   - `links`: Links to the actual downloadable data.\n\n\
        Based on this structure, you can draft a Python script that builds a STAC\
        \ catalog from the provided data, integrating each piece of relevant metadata.\n\
        If you provide code, make sure to structure it to define collection, items,\
        \ and assets, and fill each with metadata appropriately. This approach ensures\
        \ the data is discoverable using STAC APIs or libraries such as PySTAC."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2025-01-21T13:33 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range EM16TGO ACS RAWHK 48,864 97,728
        4,988.58 2025-01-19 2025-01-19 0-29692 2016-03-14 to 2024-07-19 EM16TGO ACS
        RAWSC 262 1,139 40,723.64 2024-08-16 2025-01-19 0-51 2016-04-05 to 2017-03-07
        EM16TGO ACS TCHANC 2,063 4,126 225.07 2025-01-19 2025-01-19 - 2016-04-05 to
        2025-01-11 EM16TGO CASSIS CALANC 2 4 64.01 2021-03-09 2024-01-12 - - EM16TGO
        CASSIS CALSC 5,571,818 20,896,718 21,242,531.77 2025-01-19 2025-01-19 1742-28158
        2018-04-14 to 2024-03-16 EM16TGO CASSIS DERSC 1,917 3,834 366,529.64 2024-01-19
        2024-01-19 1914-0 2018-04-28 to 2019-01-02 EM16TGO CASSIS PARHK 47,777 95,554
        14,353.13 2025-01-18 2025-01-18 1-29692 2016-03-14 to 2024-07-19 EM16TGO CASSIS
        RAWHK 82,745 165,490 17,482.20 2025-01-20 2025-01-20 0-29692 2016-03-14 to
        2024-07-19 EM16TGO CASSIS RAWSC 6,881,655 31,764,521 7,469,223.31 2025-01-20
        2025-01-20 0-29691 2016-04-07 to 2024-07-19 EM16TGO CASSIS TCHANC 1,987 3,974
        605.36 2025-01-18 2025-01-18 - 2016-04-07 to 2025-01-11 EM16TGO NOMAD CALSC
        117,203 299,464 859,927.82 2025-01-21 2025-01-21 1829-0 2018-04-21 to 2024-07-20
        EM16TGO NOMAD PARHK 21,242 42,484 23,226.95 2025-01-21 2025-01-21 0-29701
        2016-04-04 to 2024-07-20 EM16TGO NOMAD PARSC 91,176 182,352 12,469,425.54
        2025-01-21 2025-01-21 0-29697 2016-04-04 to 2024-07-20 EM16TGO NOMAD RAWHK
        21,012 42,024 21,215.08 2025-01-21 2025-01-21 0-29701 2016-04-04 to 2024-07-20
        EM16TGO NOMAD RAWSC 151,852 303,704 12,423,834.26 2025-01-21 2025-01-21 0-29697
        2016-04-04 to 2024-07-20 EM16TGO NOMAD TCHANC 2,057 4,114 120.71 2025-01-21
        2025-01-21 - 2016-04-04 to 2025-01-19 MEX HRSC DTMRDR 9,286 73,532 616,779.10
        2014-06-05 2022-08-19 10-6567 2004-01-10 to 2009-02-12 MEX HRSC PHOBOS 198
        1,386 3,509.76 2016-06-16 2022-08-19 - 2004-08-22 to 2011-07-03 MEX HRSC RDRV4
        70,737 424,422 7,329,375.02 2024-09-30 2024-09-30 10-26000 2004-01-10 to 2024-08-06
        MEX HRSC REFDR3 43,888 394,992 7,295,562.96 2020-05-18 2023-05-13 10-19592
        2004-01-10 to 2019-06-29 MEX HRSC REFDR4 41,446 373,014 10,624,829.18 2024-02-23
        2024-02-26 2419-24380 2005-12-01 to 2023-04-22 MEX MARSIS CLUTTER 8,811 176,220
        1,007,633.39 2023-11-17 2023-11-17 - - MEX MARSIS EDR 29,139 145,695 116,795.97
        2021-01-20 2024-07-16 1-20228 2003-06-16 to 2019-12-31 MEX MARSIS GEOM 8,811
        17,622 1,314.42 2023-11-17 2024-07-16 - 2005-06-29 to 2022-05-05 MEX MARSIS
        IONOSPH 8,811 70,488 9,767.64 2023-11-17 2024-02-02 - 2005-06-29 to 2022-05-05
        MEX MARSIS RADARCH 17,622 299,574 2,545,153.55 2023-11-18 2024-07-17 - 2005-06-29
        to 2022-05-05 MEX MARSIS RADAROP 17,622 616,770 7,638,921.00 2023-11-18 2024-07-17
        - 2005-06-29 to 2022-05-05 MEX MARSIS RADARUN 17,622 299,574 2,567,909.57
        2023-11-18 2024-07-17 - 2005-06-29 to 2022-05-05 MEX MARSIS RDRAIS 11,620
        3,964,241 476,161.57 2024-02-20 2024-02-20 1844-22106 2005-06-22 to 2021-06-29
        MEX MARSIS RDRSS 8,459 42,295 224,850.04 2021-01-21 2024-07-16 1885-20221
        2005-07-04 to 2019-12-29 MEX OMEGA DDRGM 8 46 1,476.99 2015-04-29 2021-01-17
        6-8485 2004-01-08 to 2010-08-20 MEX OMEGA EDR 35,539 136,028 2,177,174.63
        2024-10-14 2024-10-14 -304-25199 2003-02-19 to 2023-12-16 MEX PFS EDR 110,829
        420,837 158,710.27 2023-04-13 2023-04-13 20-18975 2003-06-23 to 2018-12-31
        MEX VMC EDR 102,944 353,668 45,022.88 2024-10-14 2024-10-14 -1-25246 2003-06-06
        to 2023-12-30 MEX VMC RDR 102,935 353,632 426,686.76 2024-10-14 2024-10-14
        -1-25246 2003-06-06 to 2023-12-30 MGS MOC-NA/WA NADSDP 1,234 3,641 5,062.84
        2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802
        191,485 204,048.94 2009-03-11 2015-08-04 -97-33982 1999-02-28 to 2006-10-15
        MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05 2015-07-16 - 1997-09-15 to
        1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340 60,892.12 2009-03-11 2015-08-04
        -97-33998 1999-02-28 to 2006-10-17 MGS MOLA MEGDR 89 445 12,514.18 2009-03-11
        2017-08-25 3-20333 1997-09-15 to 2001-06-30 MGS MOLA PEDR 771 7,710 23,968.75
        2009-03-11 2015-06-03 1578-20327 1999-02-28 to 2001-06-30 MGS MOLA PRDR 2,546
        7,638 40,139.32 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02 MGS MOLA
        SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15 to 1999-12-31 MGS MOLA TOPONAT
        8,811 88,110 76,182.73 2023-11-18 2024-07-17 - 1997-09-15 to 2001-06-30 MGS
        MOLA TOPORES 8,811 88,110 798,591.91 2023-11-18 2024-07-17 - 1997-09-15 to
        2001-06-30 MGS TES TIMAP 4 20 162.32 2013-10-28 2018-01-17 - - MGS TES TSDR
        326 23,702 198,114.76 2013-10-28 2015-07-06 - - MRO CRISM ANCILL 7,458 14,916
        674.34 2023-06-03 2023-08-30 - 2006-09-27 to 2022-05-07 MRO CRISM CDR 3,177,211
        6,354,422 707,838.04 2023-08-30 2023-08-30 - 1980-01-01 to 2023-04-04 MRO
        CRISM DDR 1,025,382 2,050,764 6,733,033.81 2022-05-27 2022-05-27 - 2006-09-27
        to 2022-02-08 MRO CRISM EDR 2,588,671 15,503,825 29,087,771.39 2022-09-01
        2023-08-30 - 2006-09-27 to 2022-05-07 MRO CRISM LDR 5,928 11,856 12,307.65
        2017-08-28 2022-06-05 - 2009-07-10 to 2017-04-29 MRO CRISM LML 302 906 11,630.00
        2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM LMLP 302 1,510
        25,975.06 2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM LMLPAR
        302 906 1,901.15 2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM
        LMLPPAR 302 2,114 4,363.78 2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08
        MRO CRISM MRDR 24,727 221,959 6,585,733.96 2023-08-14 2023-08-14 - - MRO CRISM
        MRDR4 7,056 218,736 2,835,092.98 2025-01-14 2025-01-14 - - MRO CRISM MTRDR
        10,403 1,206,748 13,643,212.59 2024-09-29 2024-09-29 840-27269 2006-09-30
        to 2012-05-21 MRO CRISM NLML 302 906 11,630.00 2023-10-23 2023-10-26 - 2010-07-23
        to 2021-07-08 MRO CRISM NLMLP 302 906 25,904.53 2023-10-23 2023-10-26 - 2010-07-23
        to 2021-07-08 MRO CRISM TER 10,407 1,363,305 6,716,621.04 2022-01-28 2022-06-07
        840-27269 2006-09-30 to 2012-05-21 MRO CRISM TRDR 1,985,070 8,106,703 98,312,484.04
        2023-01-02 2023-01-02 - 2006-09-27 to 2022-05-07 MRO CRISM VALREP 412,010
        824,020 9,575.78 2022-09-01 2023-08-30 - 2006-09-27 to 2022-05-07 MRO CTX
        EDR 150,973 443,841 17,077,636.69 2024-11-26 2024-11-26 -4242-83659 2005-08-30
        to 2024-06-01 MRO HIRISE ANAGLY 9,231 27,693 3,131,443.58 2025-01-09 2025-01-09
        - - MRO HIRISE DTM 1,313 44,943 1,907,111.65 2025-01-09 2025-01-09 - - MRO
        HIRISE EDR 2,451,529 12,182,334 61,694,731.56 2025-01-10 2025-01-10 1-85999
        2006-03-24 to 2024-11-30 MRO HIRISE RDR 10 199 23,890.50 2012-02-24 2021-01-16
        2-7519 2006-03-25 to 2008-03-04 MRO HIRISE RDRV11 182,564 4,079,269 252,732,502.50
        2025-01-09 2025-01-09 1-85999 2006-03-24 to 2024-11-30 MRO MCS DDR 35,827
        143,307 282,876.60 2024-12-02 2024-12-02 760-84441 2006-09-24 to 2024-07-31
        MRO MCS EDR 37,100 111,300 585,865.11 2024-12-02 2024-12-02 0-84441 2006-09-15
        to 2024-07-31 MRO MCS RDR 37,095 111,285 881,245.05 2024-12-02 2024-12-02
        759-84441 2006-09-24 to 2024-07-31 MRO RSS EDR 33,904 77,165 1,114,713.86
        2024-11-25 2024-11-25 - 2006-01-01 to 2025-02-04 MRO RSS RSDMAP 30 98 593.09
        2016-05-27 2020-10-30 - 1998-03-27 to 2015-04-30 MRO RSS SHADR 8 16 6.25 2020-10-30
        2020-10-30 - 1998-03-27 to 2019-08-05 MRO RSS SHBDR 4 8 2,285.01 2017-02-27
        2020-10-30 - 1998-03-27 to 2015-04-30 MRO SHARAD EDR 37,216 223,296 8,840,971.57
        2024-11-27 2024-11-27 0-83311 2006-12-06 to 2024-05-04 MRO SHARAD RDR 37,193
        185,965 13,091,954.03 2024-11-29 2024-11-29 0-83311 2006-12-06 to 2024-05-04
        MRO SHARAD SHARAD3D 2 662 315,906.17 2021-11-03 2021-11-12 - 2006-12-06 to
        2015-09-10 MRO SHARAD SHSIMU 34,862 453,206 6,586,231.38 2024-11-28 2024-11-28
        - 2006-12-06 to 2024-05-11 MRO SHARAD USGEOMV2 34,861 104,583 12,456.13 2024-11-26
        2024-11-26 1689-83397 2006-12-06 to 2024-05-11 MRO SHARAD USRDRV2 34,861 209,166
        2,120,970.62 2024-11-28 2024-11-28 1689-83397 2006-12-06 to 2024-05-11 ODY
        GRS AHD 272 816 70.72 2024-12-26 2024-12-26 - 2002-02-21 to 2024-06-08 ODY
        GRS AND 460 1,380 55.66 2024-12-26 2024-12-26 - 2002-01-25 to 2024-06-08 ODY
        GRS CGS 28,918 86,754 675,993.58 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07
        ODY GRS CMDLST 3,587 10,761 5,378.73 2023-09-30 2024-12-28 - 2001-04-25 to
        2023-01-02 ODY GRS DHD 7,778 23,334 3,615.82 2024-12-26 2024-12-26 - 2002-02-18
        to 2024-06-01 ODY GRS DND 11,847 35,541 12,275.12 2024-12-26 2024-12-26 -
        2002-02-19 to 2024-06-30 ODY GRS EKERNL 312 1,246 5.01 2023-09-30 2024-12-28
        - 2001-04-25 to 2023-01-02 ODY GRS ELEMTS 24 163 212.34 2012-03-30 2015-10-13
        - 2002-06-04 to 2005-04-03 ODY GRS GAMMAS 2,651 7,953 358,124.54 2018-10-03
        2024-12-27 - 2001-05-02 to 2009-09-30 ODY GRS GRSENG 16,712 710,248 58,217.74
        2024-12-28 2024-12-28 - 2001-04-25 to 2024-06-30 ODY GRS HENDS 8,060 24,180
        28,961.91 2024-12-28 2024-12-28 - 2001-05-02 to 2024-06-30 ODY GRS IDND 75
        150 20.40 2022-08-05 2022-08-19 - 2002-02-22 to 2020-12-31 ODY GRS MESSLG
        8,298 24,894 18,125.48 2024-12-28 2024-12-28 - 2001-04-25 to 2024-06-30 ODY
        GRS NEUTNS 8,026 24,078 67,891.95 2024-12-28 2024-12-28 - 2001-05-02 to 2024-06-30
        ODY GRS PROFIL 2,365 7,095 6,501.12 2018-10-03 2024-12-27 - 2001-06-27 to
        2009-09-07 ODY GRS PULSRS 2,621 7,863 16,866.46 2018-10-03 2024-12-27 - 2001-05-02
        to 2010-07-30 ODY GRS SGS 2,733 8,199 25,478.17 2012-03-30 2015-10-13 - 2002-06-08
        to 2009-05-25 ODY THEMIS IRBTR 342,319 1,294,093 762,665.33 2024-10-02 2024-10-02
        816-98498 2002-02-19 to 2024-02-27 ODY THEMIS IRBTR4 207,468 794,394 440,978.37
        2020-06-16 2020-06-16 13724-79699 2005-01-17 to 2019-12-02 ODY THEMIS IREDR
        1,023,347 3,505,797 4,149,674.72 2024-10-02 2024-10-02 816-98499 2002-02-19
        to 2024-02-27 ODY THEMIS IREDR4 704,624 2,384,897 2,793,213.02 2020-06-16
        2020-06-16 1547-79699 2002-04-20 to 2019-12-02 ODY THEMIS IRGEO1 63,999 431,314
        2,106,417.79 2014-10-30 2021-02-02 2400-50098 2002-06-30 to 2013-03-31 ODY
        THEMIS IRGEO2 363,106 2,381,305 15,496,652.72 2024-10-02 2024-10-02 96300-98498
        2002-02-19 to 2024-02-27 ODY THEMIS IRGEO4 216,309 1,408,642 8,601,182.78
        2020-06-16 2020-06-22 - 2013-09-28 to 2019-12-02 ODY THEMIS IRPBT1 63,765
        127,530 291,848.96 2014-11-02 2021-02-07 2400-50098 2002-06-30 to 2013-03-31
        ODY THEMIS IRPBT2 185,366 556,096 2,519,942.41 2024-10-02 2024-10-02 816-98498
        2002-02-19 to 2024-02-27 ODY THEMIS IRPBT4 110,362 328,718 1,419,459.94 2020-06-16
        2020-06-16 52301-79699 2013-09-28 to 2019-12-02 ODY THEMIS IRRDR 681,471 1,882,126
        7,320,728.18 2024-10-02 2024-10-02 816-98498 2002-02-19 to 2024-02-27 ODY
        THEMIS IRRDR4 578,955 1,574,816 6,093,609.91 2020-06-16 2020-06-22 816-79699
        2002-02-19 to 2019-12-02 ODY THEMIS VGEO1 182,376 775,775 2,978,463.21 2016-11-03
        2021-02-13 2400-50097 2002-06-30 to 2013-03-31 ODY THEMIS VGEO2 164,325 882,014
        3,764,900.58 2024-10-02 2024-10-02 816-98496 2002-02-19 to 2024-02-27 ODY
        THEMIS VGEO4 72,834 390,771 1,693,523.33 2020-06-16 2020-06-22 55600-79699
        2014-06-26 to 2019-12-02 ODY THEMIS VISABR 282,315 993,895 1,286,647.53 2024-10-02
        2024-10-02 816-98496 2002-02-19 to 2024-02-27 ODY THEMIS VISABR4 212,511 733,555
        1,034,001.95 2020-06-16 2020-06-16 6523-79699 2003-06-04 to 2019-12-02 ODY
        THEMIS VISALB 70,969 212,906 802,184.04 2024-10-02 2024-10-02 816-98496 2002-02-19
        to 2024-02-27 ODY THEMIS VISALB4 32,224 96,671 360,739.55 2020-06-16 2020-06-16
        56800-79699 2014-10-03 to 2019-12-02 ODY THEMIS VISEDR 283,293 997,336 1,462,356.36
        2024-10-02 2024-10-02 816-98496 2002-02-19 to 2024-02-27 ODY THEMIS VISEDR4
        212,791 734,745 1,122,049.09 2020-06-16 2020-06-16 6584-79699 2003-06-09 to
        2019-12-02 ODY THEMIS VISRDR 281,789 992,196 2,465,182.71 2024-10-02 2024-10-02
        816-98496 2002-02-19 to 2024-02-27 ODY THEMIS VISRDR4 240,946 833,545 2,133,238.88
        2020-06-16 2020-06-22 816-79699 2002-02-19 to 2019-12-02 VO VISAB DTM 233
        1,165 1,013.77 2012-09-14 2024-10-30 - - VO VISAB EDR 50,506 353,542 95,216.20
        2013-01-23 2021-01-22 0-1485 1976-06-22 to 1980-07-30 VO VISAB MDIM 5,100
        5,988 4,529.67 2024-10-30 2024-10-30 - - VO VISAB MDIMC 3,700 3,700 3,685.32
        2013-11-05 2024-10-30 169-1483 1977-02-07 to 1980-07-27 VO VISAB MDIMH 2,116
        2,116 3,221.25 2012-09-14 2024-10-30 - - Total 33,073,420 142,713,046 707,256,688.54
        2025-01-21 2025-01-21 - 1976-06-22 to 2025-02-04 Volume Table Volume Group
        Number Volumes Number Products Number Files File Size (MB) Last Time Product
        Added Last Time Synced Orbit Range Observation Range crism_a* 1 1,812 7,277
        81,407.49 2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 em16_t* 3 13,043,632
        55,516,278 57,618,120.47 2025-01-21 2025-01-21 0-29701 2016-03-14 to 2025-01-19
        mex_m* 1 96,921 1,427,415 14,608,244.27 2023-11-18 2024-07-17 - 1997-09-15
        to 2022-05-05 MEXHRS_1* 1 43,888 219,478 7,296,098.79 2020-05-18 2023-05-13
        10-19592 2004-01-10 to 2019-06-29 MEXHRS_2* 1 9,286 29,150 611,336.64 2014-06-05
        2022-08-19 10-6567 2004-01-10 to 2009-02-12 mexhrs_4* 10 70,737 212,561 7,331,444.35
        2024-09-30 2024-09-30 10-26000 2004-01-10 to 2024-08-06 MEXHRS_5* 1 198 1,027
        3,507.39 2016-06-16 2022-08-19 - 2004-08-22 to 2011-07-03 mexhrs_6* 8 39,934
        201,014 9,878,243.44 2023-10-31 2023-10-31 2419-23498 2005-12-01 to 2022-08-08
        MEXHRS_6* 1 1,512 7,596 778,870.78 2024-02-23 2024-02-26 23998-24380 2023-01-01
        to 2023-04-22 MEXMDE_1* 1 1,818 4,132 2,920.77 2015-04-29 2015-07-30 1885-2418
        2005-07-04 to 2005-11-30 MEXMDI_1* 8 11,620 3,963,381 477,818.40 2024-02-20
        2024-02-20 1844-22106 2005-06-22 to 2021-06-29 MEXME_1* 8 29,139 87,951 116,948.62
        2021-01-20 2024-07-16 1-20228 2003-06-16 to 2019-12-31 MEXMRS_1* 8 8,459 34,504
        226,401.36 2021-01-21 2024-07-16 1885-20221 2005-07-04 to 2019-12-29 MEXOMG_0*
        9 33,667 34,208 1,942,824.44 2024-09-07 2024-09-07 -304-23991 2003-02-19 to
        2022-12-30 MEXOMG_2* 1 8 95 4,415.38 2015-04-29 2021-01-17 6-8485 2004-01-08
        to 2010-08-20 MEXPFS_1* 7 110,829 222,351 156,827.43 2023-04-13 2023-04-13
        20-18975 2003-06-23 to 2018-12-31 MEXVMC_L* 20 205,879 824,216 481,535.95
        2024-10-14 2024-10-14 -1-25246 2003-06-06 to 2023-12-30 MGSL_2* 2 772 835
        23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30 MGSL_3* 1
        89 290 12,497.94 2009-03-11 2017-08-25 3-20333 1997-09-15 to 2001-06-30 MGSLR_X*
        1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02 MGST_1*
        326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31 162.43
        2013-10-28 2018-01-17 - - mro_c* 1 7,056 185,408 2,779,036.17 2025-01-14 2025-01-14
        - - MROCR_0* 15 6,185,350 20,722,471 29,653,829.16 2023-08-30 2023-08-30 -
        1980-01-01 to 2023-04-04 MROCR_1* 14 1,025,382 2,053,829 6,734,493.03 2022-05-27
        2022-05-27 - 2006-09-27 to 2022-02-08 MROCR_2* 16 1,985,070 5,132,298 96,784,487.82
        2023-01-02 2023-01-02 - 2006-09-27 to 2022-05-07 MROCR_3* 2 5,886 12,100 1,080,318.89
        2012-02-29 2022-05-27 - - MROCR_4* 1 10,403 1,186,484 13,577,110.55 2024-09-29
        2024-09-29 840-27269 2006-09-30 to 2012-05-21 MROCR_5* 8 5,928 13,152 12,522.59
        2017-08-28 2022-06-05 - 2009-07-10 to 2017-04-29 MROCR_6* 1 10,407 1,352,792
        6,649,923.35 2022-01-28 2022-06-07 840-27269 2006-09-30 to 2012-05-21 MROHR_0*
        1 2,644,647 10,178,552 277,192,396.85 2025-01-10 2025-01-10 1-85999 2006-03-24
        to 2024-11-30 MROM_0* 212 37,100 79,924 584,033.91 2024-12-02 2024-12-02 0-84441
        2006-09-15 to 2024-07-31 MROM_1* 192 37,095 84,172 879,317.07 2024-12-02 2024-12-02
        0-84441 2006-09-24 to 2024-07-31 MROM_2* 384 35,827 79,253 285,724.32 2024-12-02
        2024-12-02 0-84441 2006-09-24 to NULL MRORS_0* 1 33,904 67,966 1,114,234.72
        2024-11-25 2024-11-25 - 2006-01-01 to 2025-02-04 MRORS_1* 1 42 1,121 3,343.77
        2020-10-30 2020-10-30 - 1998-03-27 to 2019-08-05 MROSH_0* 4 37,216 112,492
        8,838,579.06 2024-11-27 2024-11-27 0-83311 2006-12-06 to 2024-05-04 MROSH_1*
        4 37,193 149,616 13,089,744.50 2024-11-29 2024-11-29 0-83311 2006-12-06 to
        2024-05-04 MROSH_2* 1 69,722 418,388 2,227,693.50 2024-11-28 2024-11-28 1689-83397
        2006-12-06 to 2024-05-11 MROSH_3* 1 2 720 580,261.43 2021-11-03 2021-11-12
        - 2006-12-06 to 2015-09-10 mrosh_s* 1 34,862 453,227 6,586,294.76 2024-11-28
        2024-11-28 - 2006-12-06 to 2024-05-11 VO_1* 46 50,506 254,044 92,585.84 2013-01-23
        2021-01-22 0-1485 1976-06-22 to 1980-07-30 VO_2* 22 11,149 19,920 12,984.82
        2024-10-30 2024-10-30 0-1483 1977-02-07 to 1980-07-27 MGSC* 588 243,526 748,695
        314,741.91 2013-11-05 2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX*
        4,947 150,973 587,308 17,284,610.78 2024-11-26 2024-11-26 -4242-83659 2005-08-30
        to 2024-06-01 ODGC1* 1 28,918 57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19
        to 2009-09-07 ODGD1* 1 6,915 13,861 7,120.84 2024-12-26 2024-12-26 - 2002-02-19
        to 2024-06-30 ODGE1* 1 52,632 765,847 559,695.74 2024-12-28 2024-12-28 - 2001-04-25
        to 2024-06-30 ODGH1* 1 272 573 73.01 2024-12-26 2024-12-26 - 2002-02-21 to
        2024-06-08 ODGM* 1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODGN1* 2 340 729 3,405.59 2024-12-26 2024-12-26 - 2002-01-25 to 2024-06-08
        ODGR1* 1 7,778 15,585 3,575.62 2024-12-26 2024-12-26 - 2002-02-18 to 2024-06-01
        ODGS1* 1 2,733 5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25
        ODTH 4 4,968,251 10,687,337 59,948,082.04 2024-10-02 2024-10-02 816-98499
        2002-02-19 to 2024-02-27 Total 6,896 31,440,185 118,292,232 649,476,913.86
        2025-01-21 2025-01-21 - 1976-06-22 to NULL Data Set / Product Type Product
        Files This is a count of the number of files for each product type. NOTE:
        This is largerthan the number of files in a volume since somes files (such
        as DSMAP.CAT) are included in each product even though they are only included
        once in a volume Data Set / Product Type Product File Sizes This is a sum
        of the sizes for each file for each product type. NOTE: This is largerthan
        the sum of the size of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Last Time Product Added This is the last time any product in the given
        data set and product type or in the given volume was added to ODE Last Time
        Synced This is the last the volume or any volume containing the given data
        set with the given product type was synced with ODE. Syncing ensures that
        the contents of ODE matches the volume. This includes adding new products;
        updating metadata, browse, and location information; and removing any products
        listed in ODE that no longer appear in the volume (a rare event). Observation
        Range The observation range is taken from the products Utc Start and Stop
        time. There are a few products that have odd stop times (times later than
        the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_21_2025.html
    extraction_005:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_1_3_2014_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write a Python script to download data from the Orbital Data Explorer\
        \ (ODE) using STAC (SpatioTemporal Asset Catalog) terminology, we need to\
        \ focus on some relevant fields. Based on our objective and the data provided,\
        \ we can extract key metadata and necessary components for constructing queries\
        \ or download requests. Key information for such a task would typically include:\n\
        \n1. **Dataset/Product Identification**:\n   - Mission: e.g., MEX, MRO, ODY,\
        \ etc.\n   - Instrument: e.g., HRSC, MARSIS, CRISM, etc.\n   - Product Type:\
        \ e.g., RDR, EDR, TRDR, etc.\n\n2. **Temporal Information**:\n   - Observation\
        \ Range: Start and end dates of the data product's observations.\n   - Last\
        \ Time Product Added: Indicates the most recent addition of data.\n\n3. **Data\
        \ Volume and File Details**:\n   - Number of Products and Product Files: Provides\
        \ an idea of data volume.\n   - Product File mySize (MB): Size of data in\
        \ megabytes.\n\n4. **Status and Sync Information**:\n   - Last Time Synced:\
        \ When the data was last synced with ODE.\n\nUsing this information, a script\
        \ could leverage an API or other data retrieval methods through STAC queries\
        \ to identify datasets, filter by date ranges, and download the necessary\
        \ data products.\n\nHere is a broader conceptual structure of a Python script\
        \ using libraries like `requests` or STAC-specific libraries (e.g., `pystac-client`):\n\
        \n```python\nimport requests\nfrom datetime import datetime\n\n# Example function\
        \ to query a STAC API\ndef query_stac_api(mission, instrument, product_type,\
        \ start_date, end_date):\n    # Example should be updated with real API URL\
        \ and parameters\n    stac_api_url = \"https://api.planetarydata.com/stac/search\"\
        \n\n    params = {\n        \"collections\": f\"{mission}-{instrument}-{product_type}\"\
        ,\n        \"datetime\": f\"{start_date}/{end_date}\",\n    }\n\n    response\
        \ = requests.get(stac_api_url, params=params)\n    \n    if response.status_code\
        \ == 200:\n        return response.json()\n    else:\n        response.raise_for_status()\n\
        \n# Function to download a product based on STAC metadata\ndef download_product(stac_item):\n\
        \    asset_url = stac_item[\"assets\"][\"data\"][\"href\"]\n    response =\
        \ requests.get(asset_url)\n    \n    if response.status_code == 200:\n   \
        \     file_name = f\"downloads/{stac_item['id']}.dat\"\n        with open(file_name,\
        \ \"wb\") as file:\n            file.write(response.content)\n        print(f\"\
        Downloaded: {file_name}\")\n    else:\n        response.raise_for_status()\n\
        \n# Example usage\nmission = \"MRO\"\ninstrument = \"CRISM\"\nproduct_type\
        \ = \"RDR\"\nstart_date = \"2006-09-27\"\nend_date = \"2013-05-08\"\n\n# Query\
        \ the STAC API\nstac_items = query_stac_api(mission, instrument, product_type,\
        \ start_date, end_date)\n\n# Download each product\nfor item in stac_items['features']:\n\
        \    download_product(item)\n```\n\nThis conceptual framework assumes the\
        \ presence of a STAC-compliant API that provides access to ODE datasets. Note\
        \ that the example URLs and keys are placeholders and would need actual valid\
        \ endpoints and field names. Additionally, robust error handling, authentication\
        \ (if required), and potential pagination handling would be essential for\
        \ practical implementation."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2013-12-17T15:31 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File mySize (MB)* Last Time Product
        Added Last Time Synced Orbit Range Observation Range MEX HRSC RDR 38,048 228,288
        4,216,253.56 2013-07-23 2013-11-02 10-11453 2004-01-10 to 2012-12-31 MEX HRSC
        DTMRDR 8,785 69,433 580,868.27 2013-08-27 2013-11-01 10-6398 2004-01-10 to
        2008-12-26 MEX HRSC REFDR 32,387 226,709 4,831,396.59 2013-07-24 2013-11-07
        10-11453 2004-01-10 to 2012-12-31 MEX MARSIS EDREx1 3,594 7,188 5,422.25 2013-11-04
        2013-11-04 2419-3068 2005-12-01 to 2006-05-31 MEX MARSIS EDRNom 1,818 3,636
        2,761.43 2012-02-24 2013-11-04 1885-2418 2005-07-04 to 2005-11-30 MEX MARSIS
        RDRAISE1 1,190 273,380 32,745.41 2012-02-23 2013-11-04 2540-4598 2006-01-03
        to 2007-08-03 MEX MARSIS RDRAISE2 2,016 481,952 58,074.80 2012-02-23 2013-11-04
        4800-7669 2007-09-28 to 2009-12-26 MEX MARSIS RDRAISE3 2,841 872,516 104,189.50
        2013-12-17 2013-12-17 7695-11449 2010-01-02 to 2012-12-30 MEX MARSIS RDRAIS
        438 127,160 15,566.81 2012-02-23 2012-10-19 1844-2539 2005-06-22 to 2006-01-03
        MEX MARSIS RDRSS 730 1,460 3,893.74 2012-02-24 2013-11-04 1885-2418 2005-07-04
        to 2005-11-30 MEX OMEGA EDREx1 4,662 16,317 173,459.38 2012-02-23 2013-11-01
        2607-4890 2006-01-22 to 2007-10-23 MEX OMEGA EDREx2 4,770 19,080 167,023.49
        2012-02-23 2013-11-01 4931-7697 2007-11-04 to 2010-01-03 MEX OMEGA EDREx3
        3,974 15,896 177,131.91 2013-12-17 2013-12-17 0-9931 2010-01-04 to 2012-10-17
        MEX OMEGA EDRNom 7,641 26,767 285,277.73 2012-02-23 2013-11-01 -304-2595 2003-02-19
        to 2006-01-19 MEX OMEGA DDRGM 8 46 1,476.66 2013-09-09 2013-11-01 6-8485 2004-01-08
        to 2010-08-20 MEX PFS EDREx1 11,038 49,056 18,204.72 2012-02-23 2013-12-17
        2530-5135 2003-05-02 to 2007-12-31 MEX PFS EDREx2 13,862 62,340 21,662.06
        2012-02-23 2013-12-17 2604-7689 2007-10-01 to 2009-12-31 MEX PFS EDREx3 18,082
        81,246 28,542.54 2013-12-16 2013-12-16 2604-11451 2010-01-01 to 2012-12-31
        MEX PFS EDRNom 7,307 32,589 13,615.13 2012-02-23 2013-12-17 10-2593 2003-06-23
        to 2071-01-16 MGS MOC-NA/WA NADSDP 1,234 3,642 5,062.86 2013-11-05 2013-11-05
        - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05
        2013-11-05 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802 191,485 204,048.94
        2009-03-11 2013-11-08 -97-33982 1999-02-28 to 2006-10-15 MGS MOC-NA/WA WASDP
        145,676 291,340 60,892.12 2009-03-11 2013-11-08 -97-33998 1999-02-28 to 2006-10-17
        MGS MOLA PEDR 771 7,710 23,968.75 2009-03-11 2013-11-05 1578-20327 1999-02-28
        to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,139.32 2009-03-11 2013-11-05 -
        1999-02-28 to 2006-11-02 MGS MOLA MEGDR 89 267 12,497.36 2009-03-11 2013-11-05
        3-20333 1997-09-15 to 2001-06-30 MGS MOLA SHADR 1 2 0.52 2009-03-11 2013-11-05
        - 1997-09-15 to 1999-12-31 MGS TES TSDR 326 23,702 198,114.76 2013-10-28 2013-10-28
        - - MGS TES TIMAP 4 20 162.32 2013-10-28 2013-10-28 - - MRO CRISM EDR 1,683,969
        10,098,597 10,655,949.15 2013-11-29 2013-11-29 - 2006-09-27 to 2013-05-08
        MRO CRISM VALREP 218,384 436,768 5,950.56 2013-11-29 2013-11-29 - 2006-09-27
        to 2013-05-08 MRO CRISM TRDR 1,515,706 6,082,975 30,452,089.05 2013-12-02
        2013-12-02 - 2006-09-27 to 2013-05-08 MRO CRISM L4TRDR 6 21 1,972.86 2012-03-16
        2013-10-29 - 2008-01-09 to 2011-12-06 MRO CRISM ANCILL 3,564 7,128 560.64
        2013-11-29 2013-11-29 - 2006-09-27 to 2013-05-08 MRO CRISM CDR 2,134,938 4,269,876
        381,392.49 2013-11-29 2013-11-29 - 1980-01-01 to 2014-01-09 MRO CRISM MPDDR
        3 9 94.92 2012-03-16 2013-10-29 - 2008-01-09 to 2011-12-06 MRO CRISM MTRDR
        9 57 3,679.73 2012-03-16 2013-10-29 - 2008-01-09 to 2011-12-06 MRO CRISM MRDR
        17,671 49,087 3,751,401.26 2012-02-29 2013-11-01 - - MRO CRISM DDR 796,341
        1,592,682 1,970,999.95 2013-12-01 2013-12-01 - 2006-09-27 to 2013-05-08 MRO
        CRISM LDR 3,151 6,302 6,545.82 2013-11-28 2013-11-28 - 2009-07-10 to 2013-03-07
        MRO CTX EDR 54,040 161,126 6,202,740.75 2013-11-07 2013-11-07 -4242-30909
        2005-08-30 to 2013-02-28 MRO HIRISE EDR 819,557 4,065,352 26,010,668.92 2013-12-05
        2013-12-12 1-33902 2006-03-24 to 2013-10-20 MRO HIRISE RDR 11 193 23,445.53
        2012-02-24 2013-11-07 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE ANAGLY 3,198
        9,594 1,406,801.29 2013-12-02 2013-12-02 - - MRO HIRISE RDRV11 60,933 1,323,197
        101,929,876.42 2013-12-02 2013-12-02 1-33902 2006-03-24 to 2013-10-20 MRO
        HIRISE DTM 161 4,327 269,014.50 2013-11-19 2013-12-02 - - MRO MCS EDR 12,712
        38,136 198,116.89 2013-10-29 2013-12-02 0-30550 2006-09-15 to 2013-01-31 MRO
        MCS RDR 12,707 38,121 300,415.41 2013-09-03 2013-12-02 759-30550 2006-09-24
        to 2013-01-31 MRO RSS EDR 11,399 26,262 388,918.17 2013-11-28 2013-11-28 -
        2006-01-01 to 2017-01-02 MRO RSS RSDMAP 20 68 19.12 2012-03-01 2013-10-28
        - 1998-03-27 to 2008-10-31 MRO RSS SHADR 5 10 3.50 2012-03-01 2013-10-28 -
        1998-03-27 to 2011-05-05 MRO RSS SHBDR 2 4 946.92 2012-03-01 2013-10-28 -
        2006-08-30 to 2008-10-31 MRO SHARAD EDR 11,809 70,854 2,717,619.84 2012-11-28
        2013-11-05 0-25993 2006-12-06 to 2012-02-11 MRO SHARAD RDR 11,807 59,035 4,170,478.49
        2012-11-28 2013-11-05 1689-25993 2006-12-06 to 2012-02-11 ODY THEMIS (MSL
        Landing Site Selection) Band_D 4 46 179.43 2012-02-27 2012-10-19 - - MGS TES
        (MSL Landing Site Selection) Band_D 4 46 179.43 2012-02-27 2012-10-19 - -
        Multiple Multiple (MSL Landing Site Selection) Cale_D 4 12 32.85 2012-02-27
        2012-10-19 - - MISC SHAPE Cale_D 4 12 32.85 2012-02-27 2012-10-19 - - MEX
        HRSC (MSL Landing Site Selection) Cale_D 4 12 32.85 2012-02-27 2012-10-19
        - - ODY THEMIS (MSL Landing Site Selection) Ferg_D 16 100 1,152.57 2012-02-27
        2012-10-19 - - Multiple Multiple (MSL Landing Site Selection) Golo_D 4 12
        6.09 2012-02-27 2012-10-19 - - MEX HRSC (MSL Landing Site Selection) Gwin_D
        8 24 1,116.54 2012-02-27 2012-10-19 - - MRO HIRISE (MSL Landing Site Selection)
        Mcew_D 107 1,478 199,148.98 2012-02-27 2012-10-19 - - MRO CTX (MSL Landing
        Site Selection) MSSS_D 8 16 292.23 2012-02-27 2012-10-19 - - MRO CRISM (MSL
        Landing Site Selection) Mur_DL 170 4,930 1,195.94 2012-02-27 2012-10-19 -
        - MRO CRISM (MSL Landing Site Selection) Mur_DS 171 3,931 1,436.99 2012-02-27
        2012-10-19 - - Multiple Multiple (MSL Landing Site Selection) MXDMap 4 16
        836.76 2012-02-27 2012-10-19 - - ODY THEMIS (MSL Landing Site Selection) Oste_D
        8 40 222.57 2012-02-27 2012-10-19 - - ODY GRS CMDLST 3,564 10,692 5,378.47
        2013-06-27 2013-11-02 - 2001-04-25 to 2012-11-16 ODY GRS EKERNL 294 1,174
        4.75 2013-06-27 2013-11-02 - 2001-04-25 to 2012-11-16 ODY GRS GAMMAS 2,651
        7,953 358,124.54 2012-03-30 2013-11-02 - 2001-05-02 to 2009-09-30 ODY GRS
        GRSENG 8,586 404,303 36,906.06 2013-09-27 2013-11-02 - 2001-04-25 to 2013-03-30
        ODY GRS HENDS 4,035 12,105 14,272.84 2013-09-27 2013-11-02 - 2001-05-02 to
        2013-03-30 ODY GRS MESSLG 4,242 12,726 17,905.82 2013-09-27 2013-11-02 - 2001-04-25
        to 2013-03-30 ODY GRS NEUTNS 4,005 12,015 33,416.24 2013-09-27 2013-11-02
        - 2001-05-02 to 2013-03-30 ODY GRS PROFIL 2,365 7,095 6,501.12 2012-03-30
        2013-11-02 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621 7,863 16,866.46
        2012-03-30 2013-11-02 - 2001-05-02 to 2010-07-30 ODY GRS CGS 28,918 86,754
        675,993.58 2012-03-30 2013-11-01 - 2002-02-19 to 2009-09-07 ODY GRS DHD 3,811
        11,433 1,756.61 2013-09-27 2013-11-02 - 2002-02-18 to 2013-03-30 ODY GRS DND
        2,625 7,875 2,687.45 2012-12-23 2013-11-01 - 2002-02-19 to 2012-06-29 ODY
        GRS AHD 133 399 34.58 2013-09-27 2013-11-02 - 2002-02-21 to 2013-03-20 ODY
        GRS AND 109 327 13.19 2012-12-23 2013-11-02 - 2002-01-25 to 2012-06-05 ODY
        GRS ELEMTS 24 163 212.34 2012-03-30 2013-11-02 - 2002-06-04 to 2005-04-03
        ODY GRS SGS 2,733 8,199 25,478.17 2012-03-30 2013-11-02 - 2002-06-08 to 2009-05-25
        ODY THEMIS IREDR 462,226 1,413,674 1,763,832.37 2013-11-27 2013-11-27 816-50099
        2002-02-19 to 2013-03-31 ODY THEMIS VISEDR 185,182 603,250 1,003,883.88 2013-11-14
        2013-11-28 816-50097 2002-02-19 to 2013-03-31 ODY THEMIS IRBTR 153,787 516,964
        370,073.26 2013-11-11 2013-11-11 816-50098 2002-02-19 to 2013-03-31 ODY THEMIS
        IRRDR 304,242 724,635 3,086,459.91 2013-11-24 2013-11-24 816-50098 2002-02-19
        to 2013-03-31 ODY THEMIS VISABR 184,684 601,732 971,488.10 2013-10-03 2013-11-25
        816-50097 2002-02-19 to 2013-03-31 ODY THEMIS VISRDR 184,159 600,035 1,656,120.93
        2013-11-14 2013-11-25 816-50097 2002-02-19 to 2013-03-31 VO VISAB EDR 50,506
        353,542 95,216.20 2013-01-23 2013-11-08 0-1485 1976-06-22 to 1980-07-30 VO
        VISAB MDIM 11,086 31,662 22,492.48 2013-11-05 2013-11-05 169-1483 - VO VISAB
        DTM 233 1,165 1,013.77 2012-09-14 2013-11-05 - - Total 9,389,894 36,911,492
        212,504,788.97 2013-12-17 2013-12-17 - 1976-06-22 to 2071-01-16 Volume Table
        Volume Group Number Volumes Number Products Number Files File mySize (MB)
        Last Time Product Added Last Time Synced Orbit Range Observation Range MEXHRS_2*
        1 8,785 27,560 575,769.03 2013-08-27 2013-11-01 10-6398 2004-01-10 to 2008-12-26
        MEXHRSC_0* 1 38,048 114,187 4,217,510.09 2013-07-23 2013-11-02 10-11453 2004-01-10
        to 2012-12-31 MEXHRSC_1* 1 32,387 97,198 4,831,784.54 2013-07-24 2013-11-07
        10-11453 2004-01-10 to 2012-12-31 MEXMDE_1* 2 5,412 11,528 8,443.02 2013-11-04
        2013-11-04 1885-3068 2005-07-04 to 2006-05-31 MEXMDI_1* 4 6,485 1,755,470
        211,371.15 2013-12-17 2013-12-17 1844-11449 2005-06-22 to 2012-12-30 MEXMDS_1*
        1 730 1,186 4,134.10 2012-02-24 2013-11-04 1885-2418 2005-07-04 to 2005-11-30
        MEXOMG_0* 4 21,047 21,269 802,754.89 2013-12-17 2013-12-17 -304-9931 2003-02-19
        to 2012-10-17 MEXOMG_2* 1 8 95 4,413.88 2013-09-09 2013-11-01 6-8485 2004-01-08
        to 2010-08-20 MEXPFS_1* 4 50,289 125,594 81,049.35 2013-12-16 2013-12-17 10-11451
        2003-05-02 to 2071-01-16 MGSL_2* 2 772 839 23,921.20 2009-03-11 2013-11-05
        0-20327 1997-09-15 to 2001-06-30 MGSL_3* 1 89 197 12,497.56 2009-03-11 2013-11-05
        3-20333 1997-09-15 to 2001-06-30 MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11
        2013-11-05 - 1999-02-28 to 2006-11-02 MGST_1* 326 326 52,004 202,080.67 2013-10-28
        2013-10-28 - - MGST_9* 1 4 31 162.43 2013-10-28 2013-10-28 - - MROCR_0* 6
        4,040,855 13,423,434 10,989,817.88 2013-11-29 2013-11-29 - 1980-01-01 to 2014-01-09
        MROCR_1* 5 796,341 1,593,963 1,972,002.84 2013-12-01 2013-12-01 - 2006-09-27
        to 2013-05-08 MROCR_2* 7 1,515,706 3,791,060 29,926,351.98 2013-12-02 2013-12-02
        - 2006-09-27 to 2013-05-08 MROCR_3* 4 17,671 36,258 3,751,632.75 2012-02-29
        2013-11-01 - - MROCR_5* 4 3,151 7,210 6,834.70 2013-11-28 2013-11-28 - 2009-07-10
        to 2013-03-07 MROCR_6* 1 18 284 5,812.32 2012-03-16 2013-10-29 - 2008-01-09
        to 2011-12-06 MROHR_0* 1 883,770 3,364,918 114,057,309.43 2013-12-05 2013-12-12
        1-33902 2006-03-24 to 2013-10-20 MROM_0* 74 12,712 27,422 197,343.00 2013-10-29
        2013-12-02 0-30550 2006-09-15 to 2013-01-31 MROM_1* 74 12,708 28,904 299,627.51
        2013-09-03 2013-12-02 0-30550 2006-09-24 to 2013-01-31 MRORS_0* 1 11,399 22,906
        388,804.38 2013-11-28 2013-11-28 - 2006-01-01 to 2017-01-02 MRORS_1* 1 27
        90 971.51 2012-03-01 2013-10-28 - 1998-03-27 to 2011-05-05 MROSH_0* 2 11,809
        35,849 2,716,861.79 2012-11-28 2013-11-05 0-25993 2006-12-06 to 2012-02-11
        MROSH_1* 2 11,807 47,650 4,169,773.78 2012-11-28 2013-11-05 1689-25993 2006-12-06
        to 2012-02-11 MSL_0* 1 606 10,922 210,385.74 2012-02-27 2012-10-19 18056-24300
        2010-06-03 to 2011-10-02 VO_1* 46 50,506 254,044 92,585.84 2013-01-23 2013-11-08
        0-1485 1976-06-22 to 1980-07-30 VO_2* 22 11,319 34,771 20,117.24 2013-11-05
        2013-11-05 0-1483 - MGSC* 588 243,526 748,695 314,741.91 2013-11-05 2013-11-08
        -97-33998 1997-09-15 to 2006-10-17 MROX* 1,810 54,040 213,616 6,229,899.07
        2013-11-07 2013-11-07 -4242-30909 2005-08-30 to 2013-02-28 ODGC1* 1 28,918
        57,867 675,600.75 2012-03-30 2013-11-01 - 2002-02-19 to 2009-09-07 ODGD1*
        1 2,625 5,281 2,644.56 2012-12-23 2013-11-01 - 2002-02-19 to 2012-06-29 ODGE1*
        1 32,363 443,724 489,162.23 2013-09-27 2013-11-02 - 2001-04-25 to 2013-03-30
        ODGH1* 1 133 295 37.77 2013-09-27 2013-11-02 - 2002-02-21 to 2013-03-20 ODGM*
        1 24 99 71.59 2012-03-30 2013-11-02 - 2002-06-04 to 2005-04-03 ODGN1* 1 109
        247 16.39 2012-12-23 2013-11-02 - 2002-01-25 to 2012-06-05 ODGR1* 1 3,811
        7,651 1,738.98 2013-09-27 2013-11-02 - 2002-02-18 to 2013-03-30 ODGS1* 1 2,733
        5,496 25,446.75 2012-03-30 2013-11-02 - 2002-06-08 to 2009-05-25 ODTH 1 1,474,280
        2,971,968 13,080,233.09 2013-11-27 2013-11-28 816-50099 2002-02-19 to 2013-03-31
        Total 3,008 9,389,895 29,346,894 200,641,805.24 2013-12-17 2013-12-17 - 1976-06-22
        to 2071-01-16 Data Set / Product Type Product Files This is a myCount of the
        number of files for each product type. NOTE: This is largerthan the number
        of files in a volume since somes files (such as DSMAP.CAT) are included in
        each product even though they are only included once in a volume Data Set
        / Product Type Product File Sizes This is a sum of the sizes for each file
        for each product type. NOTE: This is largerthan the sum of the size of files
        in a volume since somes files (such as DSMAP.CAT) are included in each product
        even though they are only included once in a volume Last Time Product Added
        This is the last time any product in the given data set and product type or
        in the given volume was added to ODE Last Time Synced This is the last the
        volume or any volume containing the given data set with the given product
        type was synced with ODE. Syncing ensures that the contents of ODE matches
        the volume. This includes adding new products; updating metadata, browse,
        and location information; and removing any products listed in ODE that no
        longer appear in the volume (a rare event). Observation Range The observation
        range is taken from the products Utc Start and Stop time. There are a few
        products that have odd stop times (times later than the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_3_2014.html
    extraction_006:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_1_5_2017_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code for downloading data from the Orbital Data Explorer\
        \ (ODE) using STAC (SpatioTemporal Asset Catalog) terminology, we need to\
        \ focus on identifying relevant information such as the dataset structure,\
        \ product types, and data availability. From the provided text, the essential\
        \ elements to extract for this objective are:\n\n1. **Product Types**: These\
        \ refer to different categories or classifications of data, as listed in the\
        \ data table. Examples include `MEX HRSC RDR`, `MRO CRISM EDR`, and `ODY THEMIS\
        \ VISRDR`.\n\n2. **Number of Products and Files**: Each product type has associated\
        \ data with attributes such as the number of products and files. For example,\
        \ `MRO CRISM EDR` has 2,101,503 products and 12,599,347 files.\n\n3. **Product\
        \ File Size**: This indicates the size of the files. For instance, `MRO CRISM\
        \ EDR` has a total product file size of 17,978,345.95 MB.\n\n4. **Last Time\
        \ Product Added**: This field shows the most recent date any product was added.\
        \ This is significant for understanding data updates. For instance, `MRO CRISM\
        \ EDR` last had a product added on 2016-11-30.\n\n5. **Observation Range**:\
        \ Represents the time window for which the observations were made, crucial\
        \ for determining the temporal aspect of the data set. For example, `MRO CRISM\
        \ EDR` has an observation range from 2006-09-27 to 2016-08-08.\n\nThe Python\
        \ code should include functions to query each of these attributes using a\
        \ STAC-like structure. Here's a conceptual example of how you might start\
        \ this:\n\n```python\nimport requests\n\n# Example dictionary for STAC collections\n\
        stac_collections = {\n    \"MRO_CRISM_EDR\": {\n        \"number_of_products\"\
        : 2_101_503,\n        \"number_of_files\": 12_599_347,\n        \"product_file_size_mb\"\
        : 17_978_345.95,\n        \"last_product_added\": \"2016-11-30\",\n      \
        \  \"observation_range\": (\"2006-09-27\", \"2016-08-08\"),\n    },\n    #\
        \ Define other product types similarly\n}\n\ndef query_stac(collection_name):\n\
        \    \"\"\"\n    Function to query and download data from ODE\n    based on\
        \ the given collection name\n    \"\"\"\n    if collection_name in stac_collections:\n\
        \        collection_info = stac_collections[collection_name]\n        # Construct\
        \ STAC compliant query here\n        # For example, querying a mock API endpoint\
        \ similar to STAC\n        mock_stac_api = \"http://example.com/stac\"\n \
        \       response = requests.get(f\"{mock_stac_api}/{collection_name}\")\n\
        \        \n        if response.status_code == 200:\n            # Process\
        \ data, e.g., download data assets\n            print(\"Data downloaded for\"\
        , collection_name)\n        else:\n            print(\"Error accessing ODE\
        \ data\")\n    else:\n        print(f\"No data available for {collection_name}\"\
        )\n\n# Example usage\nquery_stac(\"MRO_CRISM_EDR\")\n```\n\nThis code snippet\
        \ is a starting template for interfacing with a STAC-based API. It includes\
        \ a basic structure for maintaining information on product types and querying\
        \ them, with placeholders for making requests and processing the data. You\
        \ would need to replace the mock URL and enhance this with actual data retrieval\
        \ and processing logic based on the desired data and available services."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2017-01-04T12:20 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range MEX HRSC DTMRDR 9,286 73,532
        616,779.10 2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEX HRSC
        RDR 42,325 253,950 4,513,168.59 2015-02-21 2015-07-18 10-13323 2004-01-10
        to 2014-06-29 MEX HRSC RDRV3 46,013 276,078 4,821,791.00 2016-06-06 2016-06-06
        10-15202 2004-01-10 to 2015-12-28 MEX HRSC REFDR 34,811 243,677 5,049,869.79
        2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29 MEX HRSC REFDR3 31,960
        255,680 1,047,298.75 2017-01-03 2017-01-03 10-10694 2004-01-10 to 2012-05-24
        MEX MARSIS EDR 5,412 10,824 8,183.68 2015-04-30 2015-07-30 1885-3068 2005-07-04
        to 2006-05-31 MEX MARSIS EDRV2 5,412 10,824 8,183.68 2015-04-19 2015-04-19
        1885-3068 2005-07-04 to 2006-05-31 MEX MARSIS RDRAIS 9,761 3,120,276 373,209.22
        2016-09-14 2016-09-14 1844-15519 2005-06-22 to 2016-03-30 MEX MARSIS RDRSS
        730 1,460 3,893.74 2015-04-29 2015-07-30 1885-2418 2005-07-04 to 2005-11-30
        MEX MARSIS RDRSS2 730 1,460 3,893.17 2012-02-24 2012-10-20 1885-2418 2005-07-04
        to 2005-11-30 MEX OMEGA DDRGM 8 46 1,476.99 2015-04-29 2015-04-29 6-8485 2004-01-08
        to 2010-08-20 MEX OMEGA EDR 24,939 93,628 1,103,947.47 2016-12-01 2016-12-01
        -304-15198 2003-02-19 to 2015-12-27 MEX PFS EDR 77,551 294,463 107,827.05
        2016-10-28 2016-11-16 20-13959 2003-06-23 to 2014-12-31 MGS MOC-NA/WA NADSDP
        1,234 3,641 5,062.84 2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS
        MOC-NA/WA NASDP 95,802 191,485 204,048.94 2009-03-11 2015-08-04 -97-33982
        1999-02-28 to 2006-10-15 MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05
        2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340
        60,892.12 2009-03-11 2015-08-04 -97-33998 1999-02-28 to 2006-10-17 MGS MOLA
        MEGDR 89 267 12,497.36 2009-03-11 2015-08-19 3-20333 1997-09-15 to 2001-06-30
        MGS MOLA PEDR 771 7,710 23,968.75 2009-03-11 2015-06-03 1578-20327 1999-02-28
        to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,139.32 2009-03-11 2015-06-03 -
        1999-02-28 to 2006-11-02 MGS MOLA SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15
        to 1999-12-31 MGS TES TIMAP 4 20 162.32 2013-10-28 2015-06-03 - - MGS TES
        TSDR 326 23,702 198,114.76 2013-10-28 2015-07-06 - - MRO CRISM ANCILL 5,286
        10,572 624.18 2016-11-29 2016-11-29 - 2006-09-27 to 2016-08-08 MRO CRISM CDR
        2,501,952 5,003,904 503,125.47 2016-11-29 2016-11-29 - 1980-01-01 to 2016-08-09
        MRO CRISM DDR 903,293 1,806,586 3,823,036.77 2016-11-29 2016-11-29 - 2006-09-27
        to 2016-08-08 MRO CRISM EDR 2,101,503 12,599,347 17,978,345.95 2016-11-30
        2016-11-30 - 2006-09-27 to 2016-08-08 MRO CRISM LDR 5,304 10,608 11,012.40
        2016-11-29 2016-11-29 - 2009-07-10 to 2016-07-06 MRO CRISM MRDR 17,671 49,087
        3,751,401.26 2012-02-29 2014-08-22 - - MRO CRISM MTRDR 1,232 113,344 1,566,859.01
        2016-11-07 2016-11-07 1360-9527 2006-11-10 to 2008-08-07 MRO CRISM TER 1,232
        161,392 812,042.81 2016-11-07 2016-11-22 1360-9527 2006-11-10 to 2008-08-07
        MRO CRISM TRDR 1,655,961 6,977,140 39,727,973.93 2016-11-30 2016-11-30 - 2006-09-27
        to 2016-08-08 MRO CRISM VALREP 308,747 617,494 8,478.54 2016-11-30 2016-11-30
        - 2006-09-27 to 2016-08-08 MRO CTX EDR 81,196 242,594 8,918,220.95 2016-12-02
        2016-12-02 -4242-46156 2005-08-30 to 2016-05-31 MRO HIRISE ANAGLY 4,918 14,754
        2,036,194.26 2016-12-02 2016-12-02 - - MRO HIRISE DTM 354 12,498 590,604.92
        2016-12-02 2016-12-02 - - MRO HIRISE EDR 1,244,751 6,182,946 37,176,078.03
        2016-12-02 2016-12-02 1-48199 2006-03-24 to 2016-11-07 MRO HIRISE RDR 11 223
        24,459.84 2012-02-24 2015-10-17 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE
        RDRV11 92,702 2,077,323 148,547,604.38 2016-12-02 2016-12-02 1-48199 2006-03-24
        to 2016-11-07 MRO MCS DDR 19,685 78,740 145,603.67 2016-11-30 2016-11-30 760-46939
        2006-09-24 to 2016-07-31 MRO MCS EDR 20,234 60,702 320,978.50 2016-11-30 2016-11-30
        0-46939 2006-09-15 to 2016-07-31 MRO MCS RDR 20,228 60,684 482,266.06 2016-11-30
        2016-11-30 759-46939 2006-09-24 to 2016-07-31 MRO RSS EDR 17,308 39,635 589,585.57
        2016-11-30 2016-11-30 - 2006-01-01 to 2017-01-29 MRO RSS RSDMAP 30 98 593.09
        2016-05-27 2016-11-29 - 1998-03-27 to 2015-04-30 MRO RSS SHADR 7 14 5.33 2016-05-27
        2016-11-29 - 1998-03-27 to 2015-04-30 MRO RSS SHBDR 3 6 1,427.61 2016-02-26
        2016-11-29 - 1998-03-27 to 2015-03-30 MRO SHARAD EDR 12,824 76,944 2,961,591.90
        2015-05-29 2015-05-29 0-27071 2006-12-06 to 2012-05-05 MRO SHARAD RDR 13,143
        65,715 4,669,249.09 2015-05-29 2015-09-10 1689-27431 2006-12-06 to 2012-06-02
        MRO SHARAD USGEOM 17,041 34,082 5,805.15 2016-08-26 2016-08-26 1689-44699
        2006-12-06 to 2016-02-08 MRO SHARAD USRDR 17,041 68,164 1,025,229.42 2016-08-26
        2016-08-26 1689-44699 2006-12-06 to 2016-02-08 ODY GRS AHD 171 513 44.46 2016-12-22
        2016-12-22 - 2002-02-21 to 2016-06-08 ODY GRS AND 143 429 17.42 2016-12-22
        2016-12-22 - 2002-01-25 to 2016-06-08 ODY GRS CGS 28,918 86,754 675,993.58
        2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,575 10,725
        5,378.60 2016-12-23 2016-12-23 - 2001-04-25 to 2016-04-04 ODY GRS DHD 4,964
        14,892 2,301.06 2016-12-22 2016-12-22 - 2002-02-18 to 2016-06-30 ODY GRS DND
        3,620 10,860 3,714.17 2016-12-22 2016-12-22 - 2002-02-19 to 2016-06-30 ODY
        GRS EKERNL 305 1,218 4.92 2016-12-23 2016-12-23 - 2001-04-25 to 2016-04-04
        ODY GRS ELEMTS 24 163 212.34 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODY GRS GAMMAS 2,651 7,953 358,124.54 2012-03-30 2016-12-23 - 2001-05-02 to
        2009-09-30 ODY GRS GRSENG 10,919 490,746 43,037.56 2016-12-23 2016-12-23 -
        2001-04-25 to 2016-06-30 ODY GRS HENDS 5,188 15,564 18,514.08 2016-12-23 2016-12-23
        - 2001-05-02 to 2016-06-30 ODY GRS MESSLG 5,418 16,254 17,969.58 2016-12-23
        2016-12-23 - 2001-04-25 to 2016-06-30 ODY GRS NEUTNS 5,157 15,471 43,361.86
        2016-12-23 2016-12-23 - 2001-05-02 to 2016-06-30 ODY GRS PROFIL 2,365 7,095
        6,501.12 2012-03-30 2016-12-23 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621
        7,863 16,866.46 2012-03-30 2016-12-23 - 2001-05-02 to 2010-07-30 ODY GRS SGS
        2,733 8,199 25,478.17 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODY
        THEMIS IRBTR 200,501 723,413 470,807.12 2016-10-04 2016-11-01 816-63399 2002-02-19
        to 2016-03-30 ODY THEMIS IREDR 603,990 1,952,280 2,312,019.82 2016-10-04 2016-10-30
        816-63399 2002-02-19 to 2016-03-30 ODY THEMIS IRGEO1 68,063 461,143 2,217,907.58
        2014-10-30 2016-11-04 2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRGEO2
        73,507 473,924 3,135,641.60 2016-10-04 2016-11-06 52301-54499 2013-09-28 to
        2016-03-30 ODY THEMIS IRPBT1 67,829 135,658 300,874.95 2014-11-02 2016-11-05
        2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS IRPBT2 37,311 74,622 132,722.62
        2016-10-04 2016-11-07 52301-63399 2013-09-28 to 2016-03-30 ODY THEMIS IRRDR
        397,644 1,023,835 4,042,183.95 2016-10-04 2016-11-02 816-63399 2002-02-19
        to 2016-03-30 ODY THEMIS VGEO1 187,241 798,478 3,031,198.02 2016-11-03 2016-11-09
        816-52299 2002-02-19 to 2013-09-28 ODY THEMIS VGEO2 44,478 233,947 922,781.41
        2016-10-04 2016-11-06 52300-63399 2013-09-28 to 2016-03-30 ODY THEMIS VISABR
        215,164 723,652 1,104,833.67 2016-10-04 2016-11-03 816-63399 2002-02-19 to
        2016-03-30 ODY THEMIS VISALB 15,617 31,235 49,983.66 2016-10-04 2016-11-06
        52300-63399 2013-09-28 to 2016-03-30 ODY THEMIS VISEDR 215,708 725,351 1,158,742.06
        2016-10-04 2016-11-02 816-63399 2002-02-19 to 2016-03-30 ODY THEMIS VISRDR
        214,639 721,862 1,919,612.44 2016-10-04 2016-11-02 816-63399 2002-02-19 to
        2016-03-30 VO VISAB DTM 233 1,165 1,013.77 2012-09-14 2014-08-22 - - VO VISAB
        EDR 50,506 353,542 95,216.20 2013-01-23 2014-08-24 0-1485 1976-06-22 to 1980-07-30
        VO VISAB MDIM 11,086 31,662 22,492.48 2013-11-05 2014-08-22 169-1483 - Total
        12,082,147 50,689,203 316,018,993.12 2017-01-03 2017-01-03 - 1976-06-22 to
        2017-01-29 Volume Table Volume Group Number Volumes Number Products Number
        Files File Size (MB) Last Time Product Added Last Time Synced Orbit Range
        Observation Range MEXHRS_1* 2 77,973 297,919 10,645,389.98 2017-01-03 2017-01-03
        10-15202 2004-01-10 to 2015-12-28 MEXHRS_2* 1 9,286 29,150 611,336.64 2014-06-05
        2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEXHRS_5* 1 42,325 127,018 4,514,528.95
        2015-02-21 2015-04-30 10-13323 2004-01-10 to 2014-06-29 MEXHRSC_1* 1 34,811
        104,470 5,050,302.40 2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29
        MEXMDE_1* 2 5,412 11,528 8,443.02 2015-04-30 2015-07-30 1885-3068 2005-07-04
        to 2006-05-31 MEXMDI_1* 6 9,761 3,120,792 374,488.71 2016-09-14 2016-09-14
        1844-15519 2005-06-22 to 2016-03-30 MEXMDS_1* 1 730 1,186 4,134.10 2015-04-29
        2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEXOMG_0* 6 24,939 25,285 1,103,812.56
        2016-12-01 2016-12-01 -304-15198 2003-02-19 to 2015-12-27 MEXOMG_2* 1 8 95
        4,415.38 2015-04-29 2015-04-29 6-8485 2004-01-08 to 2010-08-20 MEXPFS_1* 5
        77,551 155,597 106,546.33 2016-10-28 2016-11-16 20-13959 2003-06-23 to 2014-12-31
        MGSL_2* 2 772 835 23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30
        MGSL_3* 1 89 197 12,497.56 2009-03-11 2015-08-19 3-20333 1997-09-15 to 2001-06-30
        MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02
        MGST_1* 326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31
        162.43 2013-10-28 2015-06-03 - - MROCR_0* 9 4,917,488 16,531,757 18,357,784.13
        2016-11-30 2016-11-30 - 1980-01-01 to 2016-08-09 MROCR_1* 8 903,293 1,808,561
        3,824,286.00 2016-11-29 2016-11-29 - 2006-09-27 to 2016-08-08 MROCR_2* 10
        1,655,961 4,161,979 38,948,228.94 2016-11-30 2016-11-30 - 2006-09-27 to 2016-08-08
        MROCR_3* 4 17,671 36,258 3,751,632.75 2012-02-29 2015-05-31 - - MROCR_4* 1
        1,232 111,133 1,566,486.98 2016-11-07 2016-11-07 1360-9527 2006-11-10 to 2008-08-07
        MROCR_5* 7 5,304 12,130 11,462.77 2016-11-29 2016-11-29 - 2009-07-10 to 2016-07-06
        MROCR_6* 1 1,232 160,412 811,694.40 2016-11-07 2016-11-22 1360-9527 2006-11-10
        to 2008-08-07 MROHR_0* 1 1,342,736 5,155,583 164,789,168.71 2016-12-02 2016-12-02
        1-48199 2006-03-24 to 2016-11-07 MROM_0* 116 20,234 43,600 319,813.10 2016-11-30
        2016-11-30 0-46939 2006-09-15 to 2016-07-31 MROM_1* 115 20,228 45,875 481,053.38
        2016-11-30 2016-11-30 0-46939 2006-09-24 to 2016-07-31 MROM_2* 232 19,685
        43,546 146,984.65 2016-11-30 2016-11-30 0-46939 2006-09-24 to 2016-07-31 MRORS_0*
        1 17,308 34,744 589,330.33 2016-11-30 2016-11-30 - 2006-01-01 to 2017-01-29
        MRORS_1* 1 40 1,117 2,485.46 2016-05-27 2016-11-29 - 1998-03-27 to 2015-04-30
        MROSH_0* 3 12,824 39,105 2,960,781.44 2015-05-29 2015-05-29 0-27071 2006-12-06
        to 2012-05-05 MROSH_1* 3 13,143 53,205 4,668,481.07 2015-05-29 2015-09-10
        1689-27431 2006-12-06 to 2012-06-02 MROSH_2* 1 34,082 136,356 1,077,485.93
        2016-08-26 2016-08-26 1689-44699 2006-12-06 to 2016-02-08 MSL_0* 1 409 9,331
        6,521.54 2012-02-27 2014-08-22 - - VO_1* 46 50,506 254,044 92,585.84 2013-01-23
        2014-08-24 0-1485 1976-06-22 to 1980-07-30 VO_2* 22 11,319 34,771 20,117.24
        2013-11-05 2014-08-22 0-1483 - MGSC* 588 243,526 748,695 314,741.91 2013-11-05
        2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX* 2,598 81,196 317,937 8,974,876.33
        2016-12-02 2016-12-02 -4242-46156 2005-08-30 to 2016-05-31 ODGC1* 1 28,918
        57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07 ODGD1*
        1 3,620 7,271 3,653.69 2016-12-22 2016-12-22 - 2002-02-19 to 2016-06-30 ODGE1*
        1 38,199 534,851 509,497.84 2016-12-23 2016-12-23 - 2001-04-25 to 2016-06-30
        ODGH1* 1 171 371 47.42 2016-12-22 2016-12-22 - 2002-02-21 to 2016-06-08 ODGM*
        1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03 ODGN1* 1 143
        315 20.54 2016-12-22 2016-12-22 - 2002-01-25 to 2016-06-08 ODGR1* 1 4,964
        9,957 2,276.87 2016-12-22 2016-12-22 - 2002-02-18 to 2016-06-30 ODGS1* 1 2,733
        5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH 2 2,341,692
        4,348,606 19,423,817.48 2016-11-03 2016-11-09 816-63399 2002-02-19 to 2016-03-30
        Total 4,135 12,076,414 38,636,191 295,058,440.66 2017-01-03 2017-01-03 - 1976-06-22
        to 2017-01-29 Data Set / Product Type Product Files This is a count of the
        number of files for each product type. NOTE: This is largerthan the number
        of files in a volume since somes files (such as DSMAP.CAT) are included in
        each product even though they are only included once in a volume Data Set
        / Product Type Product File Sizes This is a sum of the sizes for each file
        for each product type. NOTE: This is largerthan the sum of the size of files
        in a volume since somes files (such as DSMAP.CAT) are included in each product
        even though they are only included once in a volume Last Time Product Added
        This is the last time any product in the given data set and product type or
        in the given volume was added to ODE Last Time Synced This is the last the
        volume or any volume containing the given data set with the given product
        type was synced with ODE. Syncing ensures that the contents of ODE matches
        the volume. This includes adding new products; updating metadata, browse,
        and location information; and removing any products listed in ODE that no
        longer appear in the volume (a rare event). Observation Range The observation
        range is taken from the products Utc Start and Stop time. There are a few
        products that have odd stop times (times later than the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_5_2017.html
    extraction_007:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_2_2_2024_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology,\
        \ you need to focus on the metadata provided within the document. Here's a\
        \ breakdown of the relevant information:\n\n1. **Data Organization**:\n  \
        \ - The data is organized by missions, instruments, and product types.\n \
        \  - Each row represents a set of products characterized by a mission, instrument,\
        \ and product type.\n\n2. **Relevant Fields**:\n   - **Mission**: Identifier\
        \ for the space mission (e.g., `EM16TGO`, `MEX`, `MRO`).\n   - **Instrument**:\
        \ Name of the instrument used (e.g., `ACS`, `CASSIS`, `CRISM`).\n   - **Product\
        \ Type**: The type of product data (e.g., `RAWHK`, `RAWSC`, `TCHANC`).\n \
        \  - **Number Products**: Number of product entries available for a combination.\n\
        \   - **Number Product Files**: Total number of files associated with the\
        \ product type.\n   - **Product File Size (MB)**: Total size of all product\
        \ files (`in MB`).\n   - **Last Time Product Added**: Date indicating the\
        \ last time a product was added.\n   - **Last Time Synced**: Date indicating\
        \ the last time the data was synchronized with ODE.\n   - **Observation Range**:\
        \ The temporal range of the data, given in Utc Start and Stop time.\n\n3.\
        \ **Example Use Cases**:\n   - **Filter Data by Latest Sync**: Identify the\
        \ most recently synced data.\n   - **Filter by Observation Range**: Fetch\
        \ data from a specific observation period.\n   - **Download Specific Product\
        \ Types**: Use the mission, instrument, and product type to target specific\
        \ datasets for download.\n\n4. **Integration with STAC**:\n   - Construct\
        \ STAC Item objects using the metadata provided for each data entry.\n   -\
        \ Items should include datetime or temporal range fields derived from \"Observation\
        \ Range.\"\n   - Use `Number Product Files` and `Product File Size` for additional\
        \ item properties.\n   - Include links for asset downloads using endpoints\
        \ to fetch product files based on the mission, instrument, and product type\
        \ values.\n\nBy structuring the data accordingly and leveraging STAC utilities,\
        \ you can efficiently script a system to download and manage Mars holdings\
        \ from ODE."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2024-02-01T15:03 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range EM16TGO ACS RAWHK 42,152 84,304
        4,165.01 2024-01-13 2024-01-13 2-25149 2016-03-14 to 2023-07-13 EM16TGO ACS
        RAWSC 262 1,139 40,564.44 2022-04-27 2024-01-12 0-51 2016-04-05 to 2017-03-07
        EM16TGO ACS TCHANC 1,707 3,414 194.98 2024-01-12 2024-01-12 - 2016-04-05 to
        2024-01-10 EM16TGO CASSIS CALANC 2 4 67.11 2021-03-09 2021-03-09 - - EM16TGO
        CASSIS CALSC 4,050,316 12,497,956 14,704,677.82 2023-11-02 2023-11-02 1742-21320
        2018-04-14 to 2022-09-03 EM16TGO CASSIS DERSC 4,050,316 12,497,956 14,704,677.82
        2023-11-02 2023-11-02 1742-21320 2018-04-14 to 2022-09-03 EM16TGO CASSIS PARHK
        45,768 91,536 14,601.27 2023-11-01 2023-11-01 0-24257 2016-03-14 to 2023-05-01
        EM16TGO CASSIS RAWHK 79,442 158,884 17,218.44 2023-11-01 2023-11-01 0-24257
        2016-03-14 to 2023-05-01 EM16TGO CASSIS RAWSC 4,786,973 23,735,533 5,582,073.22
        2023-11-01 2023-11-01 0-24257 2016-04-07 to 2023-05-01 EM16TGO CASSIS TCHANC
        1,596 3,192 500.17 2023-10-30 2023-10-30 - 2016-04-07 to 2023-10-27 EM16TGO
        NOMAD CALSC 90,077 283,776 659,619.54 2023-10-21 2023-10-21 1829-19786 2018-04-21
        to 2022-04-30 EM16TGO NOMAD PARHK 14,575 29,150 16,763.55 2023-11-01 2023-11-01
        8-24257 2016-04-04 to 2023-05-01 EM16TGO NOMAD PARSC 73,088 146,176 11,699,154.53
        2023-11-01 2023-11-01 0-24256 2016-04-04 to 2023-05-01 EM16TGO NOMAD RAWHK
        14,575 29,150 15,425.96 2023-11-01 2023-11-01 8-24257 2016-04-04 to 2023-05-01
        EM16TGO NOMAD RAWSC 119,198 238,396 11,677,856.22 2023-11-01 2023-11-01 0-24256
        2016-04-04 to 2023-05-01 EM16TGO NOMAD TCHANC 1,668 3,336 104.54 2023-11-01
        2023-11-01 - 2016-04-04 to 2023-10-30 MEX HRSC DTMRDR 9,286 73,532 616,779.10
        2014-06-05 2022-08-19 10-6567 2004-01-10 to 2009-02-12 MEX HRSC PHOBOS 198
        1,386 3,509.76 2016-06-16 2022-08-19 - 2004-08-22 to 2011-07-03 MEX HRSC RDRV4
        67,527 405,162 6,997,089.35 2023-11-08 2023-11-08 10-24799 2004-01-10 to 2023-08-22
        MEX HRSC REFDR3 43,888 394,992 7,295,562.96 2020-05-18 2023-05-13 10-19592
        2004-01-10 to 2019-06-29 MEX HRSC REFDR4 39,934 359,406 9,845,986.05 2023-10-31
        2023-10-31 2419-23498 2005-12-01 to 2022-08-08 MEX MARSIS CLUTTER 8,811 176,220
        1,007,633.39 2023-11-17 2023-11-17 - - MEX MARSIS EDR 29,139 145,695 116,795.97
        2021-01-20 2021-01-20 1-20228 2003-06-16 to 2019-12-31 MEX MARSIS GEOM 8,811
        17,622 1,314.42 2023-11-17 2024-01-31 - 2005-06-29 to 2022-05-05 MEX MARSIS
        IONOSPH 8,811 35,244 3,145.07 2023-11-17 2023-11-17 - 2005-06-29 to 2022-05-05
        MEX MARSIS RADARCH 17,622 140,976 1,181,926.11 2023-11-18 2024-01-31 - 2005-06-29
        to 2022-05-05 MEX MARSIS RADAROP 17,622 246,708 1,219,883.40 2023-11-18 2024-01-31
        - 2005-06-29 to 2022-05-05 MEX MARSIS RADARUN 17,622 140,976 1,183,248.23
        2023-11-18 2024-01-31 - 2005-06-29 to 2022-05-05 MEX MARSIS RDRAIS 11,273
        3,846,404 463,738.95 2019-07-31 2023-04-13 1844-18349 2005-06-22 to 2018-07-02
        MEX MARSIS RDRSS 8,459 42,295 224,850.04 2021-01-21 2022-08-19 1885-20221
        2005-07-04 to 2019-12-29 MEX OMEGA DDRGM 8 46 1,476.99 2015-04-29 2021-01-17
        6-8485 2004-01-08 to 2010-08-20 MEX OMEGA EDR 32,489 123,828 1,816,052.84
        2023-05-02 2023-05-02 -304-23299 2003-02-19 to 2022-06-11 MEX PFS EDR 110,829
        420,837 158,710.27 2023-04-13 2023-04-13 20-18975 2003-06-23 to 2018-12-31
        MEX VMC EDR 70,062 222,140 29,208.45 2022-12-15 2022-12-15 -1-22741 2003-06-06
        to 2021-12-31 MEX VMC RDR 70,062 222,140 288,662.44 2022-12-15 2022-12-15
        -1-22741 2003-06-06 to 2021-12-31 MGS MOC-NA/WA NADSDP 1,234 3,641 5,062.84
        2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802
        191,485 204,048.94 2009-03-11 2015-08-04 -97-33982 1999-02-28 to 2006-10-15
        MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05 2015-07-16 - 1997-09-15 to
        1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340 60,892.12 2009-03-11 2015-08-04
        -97-33998 1999-02-28 to 2006-10-17 MGS MOLA MEGDR 89 445 12,514.18 2009-03-11
        2017-08-25 3-20333 1997-09-15 to 2001-06-30 MGS MOLA PEDR 771 7,710 23,968.75
        2009-03-11 2015-06-03 1578-20327 1999-02-28 to 2001-06-30 MGS MOLA PRDR 2,546
        7,638 40,139.32 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02 MGS MOLA
        SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15 to 1999-12-31 MGS MOLA TOPO
        17,622 70,488 329,270.71 2023-11-18 2023-11-18 - 1997-09-15 to 2001-06-30
        MGS TES TIMAP 4 20 162.32 2013-10-28 2018-01-17 - - MGS TES TSDR 326 23,702
        198,114.76 2013-10-28 2015-07-06 - - MRO CRISM ANCILL 7,458 14,916 674.34
        2023-06-03 2023-08-30 - 2006-09-27 to 2022-05-07 MRO CRISM CDR 3,177,211 6,354,422
        707,838.04 2023-08-30 2023-08-30 - 1980-01-01 to 2023-04-04 MRO CRISM DDR
        1,025,382 2,050,764 6,733,033.81 2022-05-27 2022-05-27 - 2006-09-27 to 2022-02-08
        MRO CRISM EDR 2,588,671 15,503,825 29,087,771.39 2022-09-01 2023-08-30 - 2006-09-27
        to 2022-05-07 MRO CRISM LDR 5,928 11,856 12,307.65 2017-08-28 2022-06-05 -
        2009-07-10 to 2017-04-29 MRO CRISM LML 302 906 11,630.00 2023-10-23 2023-10-26
        - 2010-07-23 to 2021-07-08 MRO CRISM LMLP 302 1,510 25,975.06 2023-10-23 2023-10-26
        - 2010-07-23 to 2021-07-08 MRO CRISM LMLPAR 302 906 1,901.15 2023-10-23 2023-10-26
        - 2010-07-23 to 2021-07-08 MRO CRISM LMLPPAR 302 2,114 4,363.78 2023-10-23
        2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM MRDR 24,727 221,959 6,585,733.96
        2023-08-14 2023-08-14 - - MRO CRISM MTRDR 10,408 957,515 13,640,386.43 2022-01-27
        2022-06-06 840-27269 2006-09-30 to 2012-05-21 MRO CRISM NLML 302 906 11,630.00
        2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM NLMLP 302 906 25,904.53
        2023-10-23 2023-10-26 - 2010-07-23 to 2021-07-08 MRO CRISM TER 10,407 1,363,305
        6,716,621.04 2022-01-28 2022-06-07 840-27269 2006-09-30 to 2012-05-21 MRO
        CRISM TRDR 1,985,070 8,106,703 98,312,484.04 2023-01-02 2023-01-02 - 2006-09-27
        to 2022-05-07 MRO CRISM VALREP 412,010 824,020 9,575.78 2022-09-01 2023-08-30
        - 2006-09-27 to 2022-05-07 MRO CTX EDR 145,085 426,177 16,422,327.61 2023-11-29
        2023-11-29 -4242-78961 2005-08-30 to 2023-05-31 MRO HIRISE ANAGLY 8,692 26,076
        3,026,795.53 2023-12-03 2023-12-03 - - MRO HIRISE DTM 1,057 37,711 1,602,987.18
        2024-01-10 2024-01-10 - - MRO HIRISE EDR 2,232,733 11,096,816 59,069,449.70
        2023-12-03 2023-12-03 1-80975 2006-03-24 to 2023-11-04 MRO HIRISE RDR 10 199
        23,890.50 2012-02-24 2021-01-16 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE
        RDRV11 165,746 3,703,568 240,534,045.37 2023-12-02 2023-12-02 1-80975 2006-03-24
        to 2023-11-04 MRO MCS DDR 34,074 136,296 262,741.54 2023-12-01 2023-12-01
        760-79744 2006-09-24 to 2023-07-31 MRO MCS EDR 34,904 104,712 551,351.45 2023-12-01
        2023-12-01 0-79744 2006-09-15 to 2023-07-31 MRO MCS RDR 34,899 104,697 829,375.83
        2023-12-01 2023-12-01 759-79744 2006-09-24 to 2023-07-31 MRO RSS EDR 32,168
        73,168 1,054,428.05 2023-11-29 2023-11-29 - 2006-01-01 to 2023-11-01 MRO RSS
        RSDMAP 30 98 593.09 2016-05-27 2020-10-30 - 1998-03-27 to 2015-04-30 MRO RSS
        SHADR 8 16 6.25 2020-10-30 2020-10-30 - 1998-03-27 to 2019-08-05 MRO RSS SHBDR
        4 8 2,285.01 2017-02-27 2020-10-30 - 1998-03-27 to 2015-04-30 MRO SHARAD EDR
        34,819 208,914 8,318,811.13 2023-12-06 2023-12-06 0-77561 2006-12-06 to 2023-02-11
        MRO SHARAD RDR 34,809 174,045 12,342,487.06 2023-12-06 2023-12-07 1689-77561
        2006-12-06 to 2023-02-11 MRO SHARAD SHARAD3D 2 662 315,906.17 2021-11-03 2021-11-12
        - 2006-12-06 to 2015-09-10 MRO SHARAD SHSIMU 32,691 424,983 6,172,445.24 2023-11-30
        2023-11-30 - 2006-12-06 to 2023-02-14 MRO SHARAD USGEOMV2 33,126 66,252 11,432.14
        2023-11-29 2023-11-29 1689-78698 2006-12-06 to 2023-05-11 MRO SHARAD USRDRV2
        33,126 132,504 2,019,506.22 2023-11-30 2023-11-30 1689-78698 2006-12-06 to
        2023-05-11 ODY GRS AHD 260 780 67.60 2024-01-25 2024-01-25 - 2002-02-21 to
        2023-07-13 ODY GRS AND 448 1,344 54.21 2024-01-05 2024-01-05 - 2002-01-25
        to 2023-07-13 ODY GRS CGS 28,918 86,754 675,993.58 2012-03-30 2015-10-13 -
        2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,587 10,761 5,378.73 2023-09-30 2024-01-06
        - 2001-04-25 to 2023-01-02 ODY GRS DHD 7,445 22,335 3,464.13 2024-01-25 2024-01-25
        - 2002-02-18 to 2023-06-30 ODY GRS DND 11,552 34,656 11,972.03 2024-01-05
        2024-01-05 - 2002-02-19 to 2023-06-30 ODY GRS EKERNL 312 1,246 5.01 2023-09-30
        2024-01-06 - 2001-04-25 to 2023-01-02 ODY GRS ELEMTS 24 163 212.34 2012-03-30
        2015-10-13 - 2002-06-04 to 2005-04-03 ODY GRS GAMMAS 2,651 7,953 358,124.54
        2018-10-03 2024-01-06 - 2001-05-02 to 2009-09-30 ODY GRS GRSENG 15,984 682,693
        56,328.11 2024-01-06 2024-01-06 - 2001-04-25 to 2023-06-30 ODY GRS HENDS 7,698
        23,094 27,672.51 2024-01-06 2024-01-06 - 2001-05-02 to 2023-06-30 ODY GRS
        IDND 75 150 20.40 2022-08-05 2022-08-19 - 2002-02-22 to 2020-12-31 ODY GRS
        MESSLG 7,937 23,811 18,106.02 2024-01-06 2024-01-06 - 2001-04-25 to 2023-06-30
        ODY GRS NEUTNS 7,665 22,995 64,863.26 2024-01-06 2024-01-06 - 2001-05-02 to
        2023-06-30 ODY GRS PROFIL 2,365 7,095 6,501.12 2018-10-03 2024-01-06 - 2001-06-27
        to 2009-09-07 ODY GRS PULSRS 2,621 7,863 16,866.46 2018-10-03 2024-01-06 -
        2001-05-02 to 2010-07-30 ODY GRS SGS 2,733 8,199 25,478.17 2012-03-30 2015-10-13
        - 2002-06-08 to 2009-05-25 ODY THEMIS IRBTR 336,043 1,268,989 755,142.79 2024-01-03
        2024-01-03 816-95191 2002-02-19 to 2023-05-31 ODY THEMIS IREDR 1,004,220 3,435,724
        4,111,707.50 2024-01-03 2024-01-03 816-95199 2002-02-19 to 2023-05-31 ODY
        THEMIS IRGEO1 63,999 431,314 2,106,417.79 2014-10-30 2021-02-02 2400-50098
        2002-06-30 to 2013-03-31 ODY THEMIS IRGEO2 352,094 2,321,644 15,021,464.93
        2024-01-03 2024-01-03 - 2002-02-19 to 2023-05-31 ODY THEMIS IRPBT1 63,765
        127,530 291,848.96 2014-11-02 2021-02-07 2400-50098 2002-06-30 to 2013-03-31
        ODY THEMIS IRPBT2 179,750 539,248 2,479,524.27 2024-01-03 2024-01-04 816-95191
        2002-02-19 to 2023-05-31 ODY THEMIS IRRDR 668,894 1,844,378 7,260,859.97 2024-01-03
        2024-01-03 816-95191 2002-02-19 to 2023-05-31 ODY THEMIS VGEO1 182,376 775,775
        2,978,463.21 2016-11-03 2021-02-13 2400-50097 2002-06-30 to 2013-03-31 ODY
        THEMIS VGEO2 160,513 861,033 3,667,235.00 2024-01-04 2024-01-04 816-95191
        2002-02-19 to 2023-05-31 ODY THEMIS VISABR 280,121 985,119 1,281,617.19 2024-01-03
        2024-01-03 816-95191 2002-02-19 to 2023-05-31 ODY THEMIS VISALB 69,169 207,506
        783,898.56 2024-01-04 2024-01-04 816-95175 2002-02-19 to 2023-05-30 ODY THEMIS
        VISEDR 281,098 988,556 1,452,714.44 2024-01-03 2024-01-03 816-95191 2002-02-19
        to 2023-05-31 ODY THEMIS VISRDR 279,595 983,420 2,447,521.43 2024-01-03 2024-01-03
        816-95191 2002-02-19 to 2023-05-31 VO VISAB DTM 233 1,165 1,013.77 2012-09-14
        2021-01-22 - - VO VISAB EDR 50,506 353,542 95,216.20 2013-01-23 2021-01-22
        0-1485 1976-06-22 to 1980-07-30 VO VISAB MDIM 5,137 6,125 4,657.36 2017-02-17
        2021-01-22 - - VO VISAB MDIMC 3,826 3,826 3,827.60 2013-11-05 2021-01-22 169-1483
        1977-02-07 to 1980-07-27 VO VISAB MDIMH 2,116 2,116 3,221.25 2012-09-14 2021-01-22
        - - Total 30,401,850 125,630,755 652,934,203.95 2024-01-25 2024-01-31 - 1976-06-22
        to 2024-01-10 Volume Table Volume Group Number Volumes Number Products Number
        Files File Size (MB) Last Time Product Added Last Time Synced Orbit Range
        Observation Range crism_a* 1 1,812 7,277 81,407.49 2023-10-23 2023-10-26 -
        2010-07-23 to 2021-07-08 em16_t* 3 9,321,399 37,226,109 51,261,743.06 2024-01-13
        2024-01-13 0-25149 2016-03-14 to 2024-01-10 mex_m* 1 96,921 599,171 4,889,167.27
        2023-11-18 2024-01-31 - 1997-09-15 to 2022-05-05 MEXHRS_1* 1 43,888 219,478
        7,296,098.79 2020-05-18 2023-05-13 10-19592 2004-01-10 to 2019-06-29 MEXHRS_2*
        1 9,286 29,150 611,336.64 2014-06-05 2022-08-19 10-6567 2004-01-10 to 2009-02-12
        mexhrs_4* 10 67,527 202,931 6,999,064.91 2023-11-08 2023-11-08 10-24799 2004-01-10
        to 2023-08-22 MEXHRS_5* 1 198 1,027 3,507.39 2016-06-16 2022-08-19 - 2004-08-22
        to 2011-07-03 mexhrs_6* 8 39,934 201,014 9,878,243.44 2023-10-31 2023-10-31
        2419-23498 2005-12-01 to 2022-08-08 MEXMDE_1* 1 1,818 4,132 2,920.77 2015-04-29
        2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEXMDI_1* 7 11,273 3,845,848
        465,338.61 2019-07-31 2023-04-13 1844-18349 2005-06-22 to 2018-07-02 MEXME_1*
        8 29,139 87,951 116,948.62 2021-01-20 2021-01-20 1-20228 2003-06-16 to 2019-12-31
        MEXMRS_1* 8 8,459 34,504 226,401.36 2021-01-21 2022-08-19 1885-20221 2005-07-04
        to 2019-12-29 MEXOMG_0* 9 32,489 33,030 1,815,912.76 2023-05-02 2023-05-02
        -304-23299 2003-02-19 to 2022-06-11 MEXOMG_2* 1 8 95 4,415.38 2015-04-29 2021-01-17
        6-8485 2004-01-08 to 2010-08-20 MEXPFS_1* 7 110,829 222,351 156,827.43 2023-04-13
        2023-04-13 20-18975 2003-06-23 to 2018-12-31 MEXVMC_L* 18 140,124 561,126
        327,647.17 2022-12-15 2022-12-15 -1-22741 2003-06-06 to 2021-12-31 MGSL_2*
        2 772 835 23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30
        MGSL_3* 1 89 290 12,497.94 2009-03-11 2017-08-25 3-20333 1997-09-15 to 2001-06-30
        MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02
        MGST_1* 326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31
        162.43 2013-10-28 2018-01-17 - - MROCR_0* 15 6,185,350 20,722,471 29,653,829.16
        2023-08-30 2023-08-30 - 1980-01-01 to 2023-04-04 MROCR_1* 14 1,025,382 2,053,829
        6,734,493.03 2022-05-27 2022-05-27 - 2006-09-27 to 2022-02-08 MROCR_2* 16
        1,985,070 5,132,298 96,784,487.82 2023-01-02 2023-01-02 - 2006-09-27 to 2022-05-07
        MROCR_3* 3 12,942 158,678 3,858,675.36 2023-08-14 2023-08-14 - - MROCR_4*
        1 10,408 936,673 13,571,782.06 2022-01-27 2022-06-06 840-27269 2006-09-30
        to 2012-05-21 MROCR_5* 8 5,928 13,152 12,522.59 2017-08-28 2022-06-05 - 2009-07-10
        to 2017-04-29 MROCR_6* 1 10,407 1,352,792 6,649,923.35 2022-01-28 2022-06-07
        840-27269 2006-09-30 to 2012-05-21 MROHR_0* 1 2,408,238 9,264,973 264,705,631.78
        2024-01-10 2024-01-10 1-80975 2006-03-24 to 2023-11-04 MROM_0* 200 34,904
        75,208 549,595.40 2023-12-01 2023-12-01 0-79744 2006-09-15 to 2023-07-31 MROM_1*
        186 34,899 79,240 827,535.32 2023-12-01 2023-12-01 0-79744 2006-09-24 to 2023-07-31
        MROM_2* 373 34,074 75,357 265,403.35 2023-12-01 2023-12-01 0-79744 2006-09-24
        to 2023-07-31 MRORS_0* 1 32,168 64,494 1,053,975.89 2023-11-29 2023-11-29
        - 2006-01-01 to 2024-01-30 MRORS_1* 1 42 1,121 3,343.77 2020-10-30 2020-10-30
        - 1998-03-27 to 2019-08-05 MROSH_0* 4 34,819 105,301 8,316,577.64 2023-12-06
        2023-12-06 0-77561 2006-12-06 to 2023-02-11 MROSH_1* 4 34,809 140,080 12,340,425.29
        2023-12-06 2023-12-07 1689-77561 2006-12-06 to 2023-02-11 MROSH_2* 1 66,252
        265,036 2,120,417.06 2023-11-30 2023-11-30 1689-78698 2006-12-06 to 2023-05-11
        MROSH_3* 1 2 720 580,261.43 2021-11-03 2021-11-12 - 2006-12-06 to 2015-09-10
        mrosh_s* 1 32,691 425,004 6,172,504.94 2023-11-30 2023-11-30 - 2006-12-06
        to 2023-02-14 VO_1* 46 50,506 254,044 92,585.84 2013-01-23 2021-01-22 0-1485
        1976-06-22 to 1980-07-30 VO_2* 22 11,312 19,920 12,984.82 2017-02-17 2021-01-22
        0-1483 1977-02-07 to 1980-07-27 MGSC* 588 243,526 748,695 314,741.91 2013-11-05
        2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX* 4,759 145,085 564,192
        16,614,249.40 2023-11-29 2023-11-29 -4242-78961 2005-08-30 to 2023-05-31 ODGC1*
        1 28,918 57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07
        ODGD1* 1 6,620 13,271 6,822.96 2024-01-05 2024-01-05 - 2002-02-19 to 2023-06-30
        ODGE1* 1 50,820 736,852 553,483.19 2024-01-06 2024-01-06 - 2001-04-25 to 2023-06-30
        ODGH1* 1 260 549 69.97 2024-01-25 2024-01-25 - 2002-02-21 to 2023-07-13 ODGM*
        1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03 ODGN1* 2 328
        705 3,404.17 2024-01-05 2024-01-05 - 2002-01-25 to 2023-07-13 ODGR1* 1 7,445
        14,919 3,425.82 2024-01-25 2024-01-25 - 2002-02-18 to 2023-06-30 ODGS1* 1
        2,733 5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH
        2 3,921,637 7,206,271 42,547,315.54 2024-01-04 2024-01-04 816-95199 2002-02-19
        to 2023-05-31 Total 6,673 26,336,440 93,822,773 599,467,176.22 2024-01-25
        2024-01-31 - 1976-06-22 to 2024-01-30 Data Set / Product Type Product Files
        This is a count of the number of files for each product type. NOTE: This is
        largerthan the number of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Data Set / Product Type Product File Sizes This is a sum of the sizes
        for each file for each product type. NOTE: This is largerthan the sum of the
        size of files in a volume since somes files (such as DSMAP.CAT) are included
        in each product even though they are only included once in a volume Last Time
        Product Added This is the last time any product in the given data set and
        product type or in the given volume was added to ODE Last Time Synced This
        is the last the volume or any volume containing the given data set with the
        given product type was synced with ODE. Syncing ensures that the contents
        of ODE matches the volume. This includes adding new products; updating metadata,
        browse, and location information; and removing any products listed in ODE
        that no longer appear in the volume (a rare event). Observation Range The
        observation range is taken from the products Utc Start and Stop time. There
        are a few products that have odd stop times (times later than the current
        date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_2_2_2024.html
    extraction_008:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_4_14_2018_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write a Python script to download data from the Orbital Data Explorer\
        \ (ODE) using STAC terminology, you'll first need to extract relevant metadata\
        \ and attributes from the text provided. Here is a list of important information\
        \ you might consider using in the script:\n\n1. **Mission**: Different missions\
        \ referred to as MEX, MGS, MRO, ODY, VO.\n2. **Instrument**: Instruments associated\
        \ with each mission, e.g., HRSC, MARSIS, OMEGA, TES, CRISM, CTX, HIRISE, MCS,\
        \ RSS, SHARAD, GRS, THEMIS, VISAB.\n3. **Product Type**: Different types of\
        \ products, e.g., DTMRDR, RDRV3, EDR, REFDR3.\n4. **Date Ranges**:\n   - **Last\
        \ Time Product Added**: The date when a product type was last added, which\
        \ helps in determining the latest data available for download.\n   - **Last\
        \ Time Synced**: Date when data was last synced, ensuring that the data on\
        \ ODE matches with the volume.\n   - **Observation Range**: The range of dates\
        \ over which observations were recorded, which can help in filtering data\
        \ for specific time ranges.\n5. **Product Files Information**:\n   - **Number\
        \ of Products**: The total count of products in each category.\n   - **Number\
        \ of Product Files**: The total count of files associated with each product\
        \ type.\n   - **Product File Size (MB)**: The total file size which might\
        \ be useful to manage download sizes.\n\nFor downloading data using STAC (SpatioTemporal\
        \ Asset Catalog), you'll need to structure the script to communicate with\
        \ STAC API endpoints, query for specific metadata attributes (like those above),\
        \ and handle data download.\n\nBelow is a simple Python template to help guide\
        \ the process of writing such a script:\n\n```python\nimport requests\n\n\
        # Define the base URL for the STAC API (this is a placeholder and should be\
        \ replaced with the actual URL)\nstac_api_url = \"https://ode.stac.api/endpoint\"\
        \n\n# Define query parameters based on extracted information\nquery_params\
        \ = {\n    \"collections\": [\"MEX_HRSC\", \"MRO_CRISM\"],  # Example collections\n\
        \    \"datetime\": \"2006-09-27/2017-11-08\",      # Example datetime query\n\
        \    \"limit\": 100,                              # Limit results\n    # You\
        \ can add other relevant query filters as needed\n}\n\ndef download_data():\n\
        \    # Make a request to the STAC API\n    response = requests.get(f\"{stac_api_url}/stac/search\"\
        , params=query_params)\n    response.raise_for_status()\n\n    # Parse the\
        \ response as JSON\n    data = response.json()\n    features = data.get(\"\
        features\", [])\n\n    for feature in features:\n        # Retrieve asset\
        \ information\n        assets = feature.get(\"assets\", {})\n        for asset_key,\
        \ asset in assets.items():\n            download_url = asset.get(\"href\"\
        )\n            print(f\"Downloading: {download_url}\")\n\n            # Download\
        \ the asset\n            asset_response = requests.get(download_url)\n   \
        \         asset_response.raise_for_status()\n\n            # Write the data\
        \ to a file (or handle as needed)\n            with open(f\"{asset_key}.dat\"\
        , 'wb') as f:\n                f.write(asset_response.content)\n\n# Run the\
        \ download function\ndownload_data()\n```\n\nIn the above template, you need\
        \ to:\n- Replace `stac_api_url` with the actual URL of the STAC API you want\
        \ to query.\n- Fill in `query_params` with the appropriate fields and filters\
        \ based on your needs and extracted metadata from the input text.\n- Add any\
        \ additional handling around paginated API responses if you anticipate needing\
        \ more than a few records per query."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2018-04-14T21:06 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range MEX HRSC DTMRDR 9,286 73,532
        616,779.10 2014-06-05 2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEX HRSC
        RDR 42,325 253,950 4,513,168.59 2015-02-21 2015-07-18 10-13323 2004-01-10
        to 2014-06-29 MEX HRSC RDRV3 49,169 295,014 5,123,974.78 2018-03-27 2018-03-27
        10-16200 2004-01-10 to 2016-10-14 MEX HRSC REFDR 34,811 243,677 5,049,869.79
        2015-02-17 2015-08-01 10-13323 2004-01-10 to 2014-06-29 MEX HRSC REFDR3 38,562
        308,496 1,224,447.67 2017-06-19 2017-06-19 10-15836 2004-01-10 to 2016-06-30
        MEX MARSIS EDR 26,781 133,905 106,516.18 2018-04-10 2018-04-10 1-17053 2003-06-16
        to 2017-06-20 MEX MARSIS RDRAIS 9,761 3,120,276 373,209.22 2016-09-14 2016-09-14
        1844-15519 2005-06-22 to 2016-03-30 MEX MARSIS RDRSS 7,865 39,325 212,240.11
        2018-04-10 2018-04-10 1885-17053 2005-07-04 to 2017-06-20 MEX OMEGA DDRGM
        8 46 1,476.99 2015-04-29 2015-04-29 6-8485 2004-01-08 to 2010-08-20 MEX OMEGA
        EDR 26,819 101,148 1,253,361.43 2018-04-10 2018-04-10 -304-16996 2003-02-19
        to 2017-06-03 MEX PFS EDR 93,339 354,451 130,389.13 2017-06-27 2017-06-27
        20-16467 2003-06-23 to 2016-12-31 MGS MOC-NA/WA NADSDP 1,234 3,641 5,062.84
        2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802
        191,485 204,048.94 2009-03-11 2015-08-04 -97-33982 1999-02-28 to 2006-10-15
        MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05 2015-07-16 - 1997-09-15 to
        1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340 60,892.12 2009-03-11 2015-08-04
        -97-33998 1999-02-28 to 2006-10-17 MGS MOLA MEGDR 89 445 12,514.18 2009-03-11
        2017-08-25 3-20333 1997-09-15 to 2001-06-30 MGS MOLA PEDR 771 7,710 23,968.75
        2009-03-11 2015-06-03 1578-20327 1999-02-28 to 2001-06-30 MGS MOLA PRDR 2,546
        7,638 40,139.32 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02 MGS MOLA
        SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15 to 1999-12-31 MGS TES TIMAP
        4 20 162.32 2013-10-28 2018-01-17 - - MGS TES TSDR 326 23,702 198,114.76 2013-10-28
        2015-07-06 - - MRO CRISM ANCILL 5,941 11,882 643.76 2018-02-27 2018-02-27
        - 2006-09-27 to 2017-11-08 MRO CRISM CDR 2,625,543 5,251,086 547,535.12 2018-02-27
        2018-02-27 - 1980-01-01 to 2017-11-09 MRO CRISM DDR 938,776 1,877,552 4,381,871.41
        2018-02-26 2018-02-26 - 2006-09-27 to 2017-11-08 MRO CRISM EDR 2,248,338 13,478,347
        20,262,020.01 2018-02-27 2018-02-27 - 2006-09-27 to 2017-11-08 MRO CRISM LDR
        5,928 11,856 12,307.65 2017-08-28 2017-08-28 - 2009-07-10 to 2017-04-29 MRO
        CRISM MRDR 17,671 49,087 3,751,401.26 2012-02-29 2014-08-22 - - MRO CRISM
        MTRDR 1,953 179,655 2,489,994.26 2018-02-04 2018-02-04 840-27269 2006-09-30
        to 2012-05-21 MRO CRISM TER 1,952 255,700 1,283,116.68 2018-02-05 2018-02-05
        840-27269 2006-09-30 to 2012-05-21 MRO CRISM TRDR 1,709,133 7,188,377 42,885,679.76
        2018-02-26 2018-02-26 - 2006-09-27 to 2017-11-08 MRO CRISM VALREP 338,848
        677,696 9,059.70 2018-02-27 2018-02-27 - 2006-09-27 to 2017-11-08 MRO CTX
        EDR 93,565 271,637 10,114,992.28 2018-03-02 2018-03-02 -4242-52021 2005-08-30
        to 2017-08-31 MRO HIRISE ANAGLY 5,584 16,752 2,212,035.53 2018-04-07 2018-04-07
        - - MRO HIRISE DTM 504 17,830 838,542.28 2018-04-07 2018-04-07 - - MRO HIRISE
        EDR 1,388,161 6,898,380 40,243,710.89 2018-04-07 2018-04-07 1-54399 2006-03-24
        to 2018-03-05 MRO HIRISE RDR 10 199 23,890.50 2012-02-24 2017-10-06 2-7519
        2006-03-25 to 2008-03-04 MRO HIRISE RDRV11 103,814 2,326,796 161,227,342.88
        2018-04-07 2018-04-07 1-54399 2006-03-24 to 2018-03-05 MRO MCS DDR 22,303
        89,212 162,442.46 2018-03-01 2018-03-01 760-52804 2006-09-24 to 2017-10-31
        MRO MCS EDR 22,946 68,838 363,677.33 2018-03-01 2018-03-01 0-52804 2006-09-15
        to 2017-10-31 MRO MCS RDR 22,940 68,820 546,648.27 2018-03-01 2018-03-01 759-52804
        2006-09-24 to 2017-10-31 MRO RSS EDR 18,942 43,421 657,741.03 2017-11-28 2017-11-28
        - 2006-01-01 to 2018-01-25 MRO RSS RSDMAP 30 98 593.09 2016-05-27 2018-02-28
        - 1998-03-27 to 2015-04-30 MRO RSS SHADR 7 14 5.33 2016-05-27 2018-02-28 -
        1998-03-27 to 2015-04-30 MRO RSS SHBDR 4 8 2,285.01 2017-02-27 2018-02-28
        - 1998-03-27 to 2015-04-30 MRO SHARAD EDR 22,335 134,010 5,430,506.48 2018-02-28
        2018-02-28 0-51860 2006-12-06 to 2017-08-19 MRO SHARAD RDR 13,143 65,715 4,669,249.09
        2015-05-29 2017-05-18 1689-27431 2006-12-06 to 2012-06-02 MRO SHARAD USGEOM
        20,304 40,608 6,817.87 2018-02-26 2018-02-26 1689-51797 2006-12-06 to 2017-08-14
        MRO SHARAD USRDR 20,304 81,216 1,203,745.83 2018-02-27 2018-02-27 1689-51797
        2006-12-06 to 2017-08-14 ODY GRS AHD 188 564 48.88 2018-04-13 2018-04-13 -
        2002-02-21 to 2017-10-17 ODY GRS AND 161 483 19.48 2018-04-13 2018-04-13 -
        2002-01-25 to 2017-10-17 ODY GRS CGS 28,918 86,754 675,993.58 2012-03-30 2015-10-13
        - 2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,578 10,734 5,378.63 2018-01-18
        2018-01-18 - 2001-04-25 to 2017-03-09 ODY GRS DHD 5,404 16,212 2,509.60 2018-04-13
        2018-04-13 - 2002-02-18 to 2017-09-30 ODY GRS DND 4,048 12,144 4,165.87 2018-04-13
        2018-04-13 - 2002-02-19 to 2017-09-30 ODY GRS EKERNL 308 1,230 4.96 2018-01-18
        2018-01-18 - 2001-04-25 to 2017-03-09 ODY GRS ELEMTS 24 163 212.34 2012-03-30
        2015-10-13 - 2002-06-04 to 2005-04-03 ODY GRS GAMMAS 2,651 7,953 358,124.54
        2018-01-17 2018-01-17 - 2001-05-02 to 2009-09-30 ODY GRS GRSENG 11,641 518,084
        44,945.43 2018-01-18 2018-01-18 - 2001-04-25 to 2017-06-30 ODY GRS HENDS 5,545
        16,635 19,834.07 2018-01-18 2018-01-18 - 2001-05-02 to 2017-06-30 ODY GRS
        MESSLG 5,775 17,325 17,989.01 2018-01-18 2018-01-18 - 2001-04-25 to 2017-06-30
        ODY GRS NEUTNS 5,514 16,542 46,475.78 2018-01-18 2018-01-18 - 2001-05-02 to
        2017-06-30 ODY GRS PROFIL 2,365 7,095 6,501.12 2018-01-17 2018-01-17 - 2001-06-27
        to 2009-09-07 ODY GRS PULSRS 2,621 7,863 16,866.46 2018-01-18 2018-01-18 -
        2001-05-02 to 2010-07-30 ODY GRS SGS 2,733 8,199 25,478.17 2012-03-30 2015-10-13
        - 2002-06-08 to 2009-05-25 ODY THEMIS IRBTR 223,359 814,806 521,236.28 2018-04-10
        2018-04-10 816-69799 2002-02-19 to 2017-09-08 ODY THEMIS IREDR 673,470 2,206,809
        2,634,508.75 2018-04-10 2018-04-10 816-69799 2002-02-19 to 2017-09-08 ODY
        THEMIS IRGEO1 68,063 461,143 2,217,907.58 2014-10-30 2016-11-04 2400-52299
        2002-06-30 to 2013-09-28 ODY THEMIS IRGEO2 117,553 771,244 5,089,927.77 2018-04-10
        2018-04-10 53085-53085 2013-09-28 to 2017-09-08 ODY THEMIS IRPBT1 67,829 135,658
        300,874.95 2014-11-02 2016-11-05 2400-52299 2002-06-30 to 2013-09-28 ODY THEMIS
        IRPBT2 60,153 180,456 880,973.46 2018-04-10 2018-04-10 52301-69799 2013-09-28
        to 2017-09-08 ODY THEMIS IRRDR 443,331 1,160,931 4,620,944.23 2018-04-10 2018-04-10
        816-69799 2002-02-19 to 2017-09-08 ODY THEMIS VGEO1 187,241 798,478 3,031,198.02
        2016-11-03 2016-11-09 816-52299 2002-02-19 to 2013-09-28 ODY THEMIS VGEO2
        62,922 334,013 1,365,953.48 2018-04-10 2018-04-10 52300-69799 2013-09-28 to
        2017-09-08 ODY THEMIS VISABR 226,312 768,244 1,137,122.62 2018-04-10 2018-04-10
        816-69799 2002-02-19 to 2017-09-08 ODY THEMIS VISALB 23,282 63,119 208,742.75
        2018-04-10 2018-04-10 52300-69796 2013-09-28 to 2017-09-08 ODY THEMIS VISEDR
        226,866 769,983 1,209,534.03 2018-04-10 2018-04-10 816-69799 2002-02-19 to
        2017-09-08 ODY THEMIS VISRDR 225,787 766,454 2,010,880.86 2018-04-10 2018-04-10
        816-69799 2002-02-19 to 2017-09-08 VO VISAB DTM 233 1,165 1,013.77 2012-09-14
        2017-02-28 - - VO VISAB EDR 50,506 353,542 95,216.20 2013-01-23 2014-08-24
        0-1485 1976-06-22 to 1980-07-30 VO VISAB MDIM 5,137 6,125 4,657.36 2017-02-17
        2017-02-28 - - VO VISAB MDIMC 3,826 3,826 3,827.60 2013-11-05 2017-02-28 169-1483
        1977-02-07 to 1980-07-27 VO VISAB MDIMH 2,116 2,116 3,221.25 2012-09-14 2017-02-28
        - - Total 12,984,428 54,883,123 349,041,116.00 2018-04-13 2018-04-13 - 1976-06-22
        to 2018-03-05 Volume Table Volume Group Number Volumes Number Products Number
        Files File Size (MB) Last Time Product Added Last Time Synced Orbit Range
        Observation Range MEXHRS_1* 2 87,731 340,397 11,668,680.80 2018-03-27 2018-03-27
        10-16200 2004-01-10 to 2016-10-14 MEXHRS_2* 1 9,286 29,150 611,336.64 2014-06-05
        2015-07-30 10-6567 2004-01-10 to 2009-02-12 MEXHRS_5* 1 42,325 127,018 4,514,528.95
        2015-02-21 2015-04-30 10-13323 2004-01-10 to 2014-06-29 MEXMDE_1* 1 1,818
        4,132 2,920.77 2015-04-29 2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEXMDI_1*
        6 9,761 3,120,792 374,488.71 2016-09-14 2016-09-14 1844-15519 2005-06-22 to
        2016-03-30 MEXME_1* 7 26,781 80,812 106,618.37 2018-04-10 2018-04-10 1-17053
        2003-06-16 to 2017-06-20 MEXMRS_1* 7 7,865 32,064 213,723.83 2018-04-10 2018-04-10
        1885-17053 2005-07-04 to 2017-06-20 MEXOMG_0* 7 26,819 27,231 1,253,235.28
        2018-04-10 2018-04-10 -304-16996 2003-02-19 to 2017-06-03 MEXOMG_2* 1 8 95
        4,415.38 2015-04-29 2015-04-29 6-8485 2004-01-08 to 2010-08-20 MEXPFS_1* 6
        93,339 187,272 128,832.07 2017-06-27 2017-06-27 20-16467 2003-06-23 to 2016-12-31
        MGSL_2* 2 772 835 23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30
        MGSL_3* 1 89 290 12,497.94 2009-03-11 2017-08-25 3-20333 1997-09-15 to 2001-06-30
        MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02
        MGST_1* 326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31
        162.43 2013-10-28 2018-01-17 - - MROCR_0* 10 5,218,670 17,624,152 20,678,457.05
        2018-02-27 2018-02-27 - 1980-01-01 to 2017-11-09 MROCR_1* 9 938,776 1,879,717
        4,383,165.90 2018-02-26 2018-02-26 - 2006-09-27 to 2017-11-08 MROCR_2* 11
        1,709,125 4,306,376 42,038,905.17 2018-02-26 2018-02-26 - 2006-09-27 to 2017-11-08
        MROCR_3* 4 17,671 36,258 3,751,632.75 2012-02-29 2015-05-31 - - MROCR_4* 1
        1,953 175,677 2,485,243.49 2018-02-04 2018-02-04 840-27269 2006-09-30 to 2012-05-21
        MROCR_5* 8 5,928 13,538 12,774.60 2017-08-28 2017-08-28 - 2009-07-10 to 2017-04-29
        MROCR_6* 1 1,952 253,596 1,280,105.24 2018-02-05 2018-02-05 840-27269 2006-09-30
        to 2012-05-21 MROHR_0* 1 1,498,073 5,764,544 178,927,198.06 2018-04-07 2018-04-07
        1-54399 2006-03-24 to 2018-03-05 MROM_0* 131 22,946 49,429 362,383.29 2018-03-01
        2018-03-01 0-52804 2006-09-15 to 2017-10-31 MROM_1* 130 22,940 52,004 545,297.58
        2018-03-01 2018-03-01 0-52804 2006-09-24 to 2017-10-31 MROM_2* 262 22,303
        49,322 164,030.57 2018-03-01 2018-03-01 0-52804 2006-09-24 to 2017-10-31 MRORS_0*
        1 18,942 38,016 657,458.48 2017-11-28 2017-11-28 - 2006-01-01 to 2018-01-25
        MRORS_1* 1 41 1,119 3,342.86 2017-02-27 2018-02-28 - 1998-03-27 to 2015-04-30
        MROSH_0* 4 22,335 67,849 5,429,087.19 2018-02-28 2018-02-28 0-51860 2006-12-06
        to 2017-08-19 MROSH_1* 3 13,143 53,205 4,668,481.07 2015-05-29 2017-05-18
        1689-27431 2006-12-06 to 2012-06-02 MROSH_2* 1 40,608 162,460 1,265,085.39
        2018-02-27 2018-02-27 1689-51797 2006-12-06 to 2017-08-14 MSL_0* 1 409 9,331
        6,521.54 2012-02-27 2014-08-22 - - VO_1* 46 50,506 254,044 92,585.84 2013-01-23
        2014-08-24 0-1485 1976-06-22 to 1980-07-30 VO_2* 22 11,312 19,920 12,984.82
        2017-02-17 2017-02-28 0-1483 1977-02-07 to 1980-07-27 MGSC* 588 243,526 748,695
        314,741.91 2013-11-05 2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX*
        2,943 93,565 356,985 10,188,105.93 2018-03-02 2018-03-02 -4242-52021 2005-08-30
        to 2017-08-31 ODGC1* 1 28,918 57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19
        to 2009-09-07 ODGD1* 1 4,048 8,127 4,097.82 2018-04-13 2018-04-13 - 2002-02-19
        to 2017-09-30 ODGE1* 1 39,998 563,624 515,844.65 2018-01-18 2018-01-18 - 2001-04-25
        to 2017-06-30 ODGH1* 1 188 405 51.73 2018-04-13 2018-04-13 - 2002-02-21 to
        2017-10-17 ODGM* 1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03
        ODGN1* 1 161 351 22.56 2018-04-13 2018-04-13 - 2002-01-25 to 2017-10-17 ODGR1*
        1 5,404 10,837 2,482.91 2018-04-13 2018-04-13 - 2002-02-18 to 2017-09-30 ODGS1*
        1 2,733 5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH
        2 2,606,168 4,819,611 23,758,097.45 2018-04-10 2018-04-10 816-69799 2002-02-19
        to 2017-09-08 Total 4,558 12,951,836 41,389,889 321,406,692.88 2018-04-13
        2018-04-13 - 1976-06-22 to 2018-03-05 Data Set / Product Type Product Files
        This is a count of the number of files for each product type. NOTE: This is
        largerthan the number of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Data Set / Product Type Product File Sizes This is a sum of the sizes
        for each file for each product type. NOTE: This is largerthan the sum of the
        size of files in a volume since somes files (such as DSMAP.CAT) are included
        in each product even though they are only included once in a volume Last Time
        Product Added This is the last time any product in the given data set and
        product type or in the given volume was added to ODE Last Time Synced This
        is the last the volume or any volume containing the given data set with the
        given product type was synced with ODE. Syncing ensures that the contents
        of ODE matches the volume. This includes adding new products; updating metadata,
        browse, and location information; and removing any products listed in ODE
        that no longer appear in the volume (a rare event). Observation Range The
        observation range is taken from the products Utc Start and Stop time. There
        are a few products that have odd stop times (times later than the current
        date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_14_2018.html
    extraction_009:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_4_2_2013_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of writing Python code to download data from\
        \ the Orbital Data Explorer (ODE) using STAC terminology, you need to extract\
        \ the relevant data structure and information components that fit with the\
        \ STAC model. Here's a breakdown of key pieces of information that can be\
        \ used:\n\n1. **Catalog Information** (Mission, Instrument, and Product Type):\n\
        \   - Mission: E.g., MEX (Mars Express), MRO (Mars Reconnaissance Orbiter),\
        \ ODY (Mars Odyssey), etc.\n   - Instrument: E.g., HRSC, MARSIS, OMEGA, CRISM,\
        \ HIRISE, THEMIS, etc.\n   - Product Type: E.g., RDR, EDR, DTMRDR, REFDR,\
        \ etc.\n\n2. **Item Information**:\n   - Number of Products\n   - Number of\
        \ Product Files\n   - Product File Size (MB)\n   - Last Time Product Added\n\
        \   - Last Time Synced\n   - Orbit Range (if applicable)\n   - Observation\
        \ Range\n\n3. **Collection Information**:\n   - Volume Group\n   - Number\
        \ of Volumes\n   - File Size (MB)\n   - Last Time Product Added\n   - Last\
        \ Time Synced\n   - Observation Range\n\n\n4. **Relevant Dates and Times**:\n\
        \   - Observation Range: Start and end times for the product data, e.g., \"\
        2004-01-10 to 2012-06-30\".\n   - Last Time Product Added: Indicates when\
        \ the last product was added, e.g., \"2012-12-28\".\n   - Last Time Synced:\
        \ Indicates when the dataset was last synchronized, e.g., \"2012-12-28\".\n\
        \n5. **Additional Information**:\n   - Total Number of Products and Product\
        \ Files.\n   - Total Product File Size.\n\nBy organizing the above information\
        \ into the STAC structure, you can create a catalog with collections and items\
        \ that users can interact with when writing Python code to download specific\
        \ data sets. Additionally, you'll need the capability to query this catalog\
        \ based on the properties like observation range, instrument type, or specific\
        \ product types (e.g., EDR, RDR).\n\nThis information can serve as the basis\
        \ for a Python script that constructs requests to access these data sets.\
        \ Using a library like `pystac`, you can convert this information into valid\
        \ STAC Catalogs, Collections, and Items to facilitate querying and downloading\
        \ of the data."
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2013-04-01T07:19 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range MEX HRSC RDR 37,796 226,776
        4,169,308.44 2012-12-28 2012-12-28 10-10821 2004-01-10 to 2012-06-30 MEX HRSC
        DTMRDR 8,530 67,648 571,790.18 2012-08-16 2012-12-28 10-5446 2004-01-10 to
        2008-03-29 MEX HRSC REFDR 32,245 225,715 4,823,068.33 2012-12-29 2012-12-29
        10-10821 2004-01-10 to 2012-06-30 MEX MARSIS EDREx1 3,565 7,130 5,417.90 2012-02-24
        2012-10-19 2419-3068 2005-12-01 to 2006-05-31 MEX MARSIS EDRNom 1,818 3,636
        2,760.18 2012-02-24 2012-10-19 1885-2418 2005-07-04 to 2005-11-30 MEX MARSIS
        RDRAISE1 1,190 273,380 32,540.59 2012-02-23 2012-10-19 2540-4598 2006-01-03
        to 2007-08-03 MEX MARSIS RDRAISE2 2,016 481,952 57,713.86 2012-02-23 2012-10-19
        4800-7669 2007-09-28 to 2009-12-26 MEX MARSIS RDRAISE3 1,683 487,235 58,051.53
        2012-06-19 2012-10-20 7695-9879 2010-01-02 to 2011-09-30 MEX MARSIS RDRAIS
        438 127,160 15,566.81 2012-02-23 2012-10-19 1844-2539 2005-06-22 to 2006-01-03
        MEX MARSIS RDRSS 730 1,460 3,893.17 2012-02-24 2012-10-20 1885-2418 2005-07-04
        to 2005-11-30 MEX OMEGA EDREx1 4,662 16,317 173,450.11 2012-02-23 2012-10-19
        2607-4890 2006-01-22 to 2007-10-23 MEX OMEGA EDREx2 4,770 19,080 167,011.72
        2012-02-23 2012-10-19 4931-7697 2007-11-04 to 2010-01-03 MEX OMEGA EDREx3
        1,462 5,848 67,359.59 2012-09-06 2012-10-19 7701-9182 2010-01-04 to 2011-03-11
        MEX OMEGA EDRNom 7,641 26,767 285,262.21 2012-02-23 2012-10-19 -304-2595 2003-02-19
        to 2006-01-19 MEX PFS EDREx1 11,038 49,056 18,301.31 2012-02-23 2012-10-19
        2530-5135 2003-05-02 to 2007-12-31 MEX PFS EDREx2 13,862 62,340 21,805.39
        2012-02-23 2012-10-19 2604-7689 2007-10-01 to 2009-12-31 MEX PFS EDREx3 5,466
        24,474 8,283.97 2012-02-23 2012-10-19 2604-8944 2010-01-01 to 2010-12-31 MEX
        PFS EDRNom 7,307 32,589 13,682.20 2012-02-23 2012-10-19 10-2593 2003-06-23
        to 2071-01-16 MGS MOC-NA/WA NADSDP 1,234 3,642 3.64 2009-03-11 2012-09-14
        - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WADSDP 814 2,436 2.44 2009-03-11
        2012-09-14 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA NASDP 95,802 191,485 203,860.01
        2009-03-11 2012-12-06 -97-33982 1999-02-28 to 2006-10-15 MGS MOC-NA/WA WASDP
        145,676 291,340 60,639.07 2009-03-11 2012-12-06 -97-33998 1999-02-28 to 2006-10-17
        MGS MOLA PEDR 771 7,710 23,964.51 2009-03-11 2012-10-19 1578-20327 1999-02-28
        to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,137.50 2009-03-11 2012-10-19 -
        1999-02-28 to 2006-11-02 MGS MOLA MEGDR 89 267 12,497.21 2009-03-11 2012-10-19
        3-20333 1997-09-15 to 2001-06-30 MGS MOLA SHADR 1 2 0.52 2009-03-11 2012-10-19
        - 1997-09-15 to 1999-12-31 MRO CRISM EDR 1,623,681 9,737,647 9,988,014.95
        2013-02-25 2013-02-25 - 2006-09-27 to 2012-08-03 MRO CRISM VALREP 205,196
        410,392 5,470.73 2013-02-25 2013-02-25 - 2006-09-27 to 2012-08-03 MRO CRISM
        TRDR 1,488,366 6,310,741 29,069,495.11 2013-02-25 2013-02-25 - 2006-09-27
        to 2012-08-03 MRO CRISM L4TRDR 6 21 1,972.84 2012-03-16 2012-10-18 - 2008-01-09
        to 2011-12-06 MRO CRISM ANCILL 3,233 6,466 546.48 2013-02-25 2013-02-25 -
        2006-09-27 to 2012-08-03 MRO CRISM CDR 2,068,792 4,137,584 355,074.07 2013-02-25
        2013-02-25 - 1980-01-01 to 2014-01-09 MRO CRISM MPDDR 3 9 94.92 2012-03-16
        2012-10-18 - 2008-01-09 to 2011-12-06 MRO CRISM MTRDR 9 57 3,679.71 2012-03-16
        2012-10-18 - 2008-01-09 to 2011-12-06 MRO CRISM MRDR 17,671 49,087 3,751,381.88
        2012-02-29 2012-10-12 - - MRO CRISM DDR 783,105 1,566,210 1,834,492.02 2013-02-25
        2013-02-25 - 2006-09-27 to 2012-08-03 MRO CRISM LDR 2,580 5,160 5,361.50 2013-02-25
        2013-02-25 - 2009-07-10 to 2012-05-24 MRO CTX EDR 48,146 139,032 5,603,660.16
        2013-03-01 2013-03-01 -4242-28587 2005-08-30 to 2012-09-01 MRO HIRISE EDR
        763,995 3,789,450 24,699,532.89 2013-03-04 2013-03-04 1-30609 2006-03-24 to
        2013-02-05 MRO HIRISE RDR 11 88 10,562.70 2012-02-24 2012-10-10 2-7519 2006-03-25
        to 2008-03-04 MRO HIRISE ANAGLY 2,963 8,889 1,334,916.80 2013-03-04 2013-03-04
        - - MRO HIRISE RDRV11 55,853 446,272 41,077,769.71 2013-03-04 2013-03-04 1-30609
        2006-03-24 to 2013-02-05 MRO HIRISE DTM 116 2,975 200,066.82 2013-03-04 2013-03-04
        - - MRO MCS EDR 11,819 35,457 184,318.75 2013-03-01 2013-03-01 0-28189 2006-09-15
        to 2012-07-31 MRO MCS RDR 11,814 35,442 279,504.03 2013-03-01 2013-03-01 759-28189
        2006-09-24 to 2012-07-31 MRO RSS EDR 10,250 23,582 342,861.30 2013-03-01 2013-03-01
        - 2006-01-01 to 2017-01-02 MRO RSS RSDMAP 20 68 19.08 2012-03-01 2012-10-10
        - 1998-03-27 to 2008-10-31 MRO RSS SHADR 5 10 3.49 2012-03-01 2012-10-10 -
        1998-03-27 to 2011-05-05 MRO RSS SHBDR 2 4 946.92 2012-03-01 2012-10-10 -
        2006-08-30 to 2008-10-31 MRO SHARAD EDR 11,809 70,854 2,717,572.64 2012-11-28
        2012-11-29 0-25993 2006-12-06 to 2012-02-11 MRO SHARAD RDR 11,807 59,035 4,170,454.68
        2012-11-28 2012-11-29 1689-25993 2006-12-06 to 2012-02-11 ODY THEMIS (MSL
        Landing Site Selection) Band_D 4 46 179.43 2012-02-27 2012-10-19 - - MGS TES
        (MSL Landing Site Selection) Band_D 4 46 179.43 2012-02-27 2012-10-19 - -
        Multiple Multiple (MSL Landing Site Selection) Cale_D 4 12 32.85 2012-02-27
        2012-10-19 - - MISC SHAPE Cale_D 4 12 32.85 2012-02-27 2012-10-19 - - MEX
        HRSC (MSL Landing Site Selection) Cale_D 4 12 32.85 2012-02-27 2012-10-19
        - - ODY THEMIS (MSL Landing Site Selection) Ferg_D 16 100 1,152.57 2012-02-27
        2012-10-19 - - Multiple Multiple (MSL Landing Site Selection) Golo_D 4 12
        6.09 2012-02-27 2012-10-19 - - MEX HRSC (MSL Landing Site Selection) Gwin_D
        8 24 1,116.54 2012-02-27 2012-10-19 - - MRO HIRISE (MSL Landing Site Selection)
        Mcew_D 107 1,478 199,148.98 2012-02-27 2012-10-19 - - MRO CTX (MSL Landing
        Site Selection) MSSS_D 8 16 292.23 2012-02-27 2012-10-19 - - MRO CRISM (MSL
        Landing Site Selection) Mur_DL 170 4,930 1,195.94 2012-02-27 2012-10-19 -
        - MRO CRISM (MSL Landing Site Selection) Mur_DS 171 3,931 1,436.99 2012-02-27
        2012-10-19 - - Multiple Multiple (MSL Landing Site Selection) MXDMap 4 16
        836.76 2012-02-27 2012-10-19 - - ODY THEMIS (MSL Landing Site Selection) Oste_D
        8 40 222.57 2012-02-27 2012-10-19 - - ODY GRS CMDLST 3,558 10,674 5,369.51
        2012-07-02 2012-12-23 - 2001-04-25 to 2011-10-27 ODY GRS EKERNL 290 1,158
        3.96 2012-07-02 2012-12-23 - 2001-04-25 to 2011-10-27 ODY GRS GAMMAS 2,651
        7,953 358,121.10 2012-03-30 2012-12-23 - 2001-05-02 to 2009-09-30 ODY GRS
        GRSENG 8,057 384,321 35,308.14 2012-12-23 2012-12-23 - 2001-04-25 to 2012-06-30
        ODY GRS HENDS 3,777 11,331 13,374.72 2012-12-23 2012-12-23 - 2001-05-02 to
        2012-06-30 ODY GRS MESSLG 3,984 11,952 17,885.72 2012-12-23 2012-12-23 - 2001-04-25
        to 2012-06-30 ODY GRS NEUTNS 3,747 11,241 31,303.30 2012-12-23 2012-12-23
        - 2001-05-02 to 2012-06-30 ODY GRS PROFIL 2,365 7,095 6,497.58 2012-03-30
        2012-12-23 - 2001-06-27 to 2009-09-07 ODY GRS PULSRS 2,621 7,863 16,862.31
        2012-03-30 2012-12-23 - 2001-05-02 to 2010-07-30 ODY GRS CGS 28,918 86,754
        675,966.32 2012-03-30 2012-12-23 - 2002-02-19 to 2009-09-07 ODY GRS DHD 3,553
        10,659 1,639.06 2012-12-23 2012-12-23 - 2002-02-18 to 2012-06-30 ODY GRS DND
        2,625 7,875 2,686.16 2012-12-23 2012-12-23 - 2002-02-19 to 2012-06-29 ODY
        GRS AHD 125 375 32.38 2012-12-23 2012-12-23 - 2002-02-21 to 2012-06-05 ODY
        GRS AND 109 327 13.08 2012-12-23 2012-12-23 - 2002-01-25 to 2012-06-05 ODY
        GRS ELEMTS 24 163 212.26 2012-03-30 2012-12-23 - 2002-06-04 to 2005-04-03
        ODY GRS SGS 2,733 8,199 25,477.04 2012-03-30 2012-12-24 - 2002-06-08 to 2009-05-25
        ODY THEMIS IREDR 145,344 538,945 1,561,841.82 2013-01-22 2013-01-22 816-46799
        2002-02-19 to 2012-07-02 ODY THEMIS VISEDR 178,071 574,807 964,947.87 2013-01-23
        2013-01-23 816-46799 2002-02-19 to 2012-07-02 ODY THEMIS IRBTR 144,045 477,998
        361,060.33 2013-01-22 2013-01-22 816-46799 2002-02-19 to 2012-07-02 ODY THEMIS
        IRRDR 144,365 474,464 2,970,456.50 2013-01-22 2013-01-22 816-46799 2002-02-19
        to 2012-07-02 ODY THEMIS VISABR 177,574 573,292 933,940.92 2013-01-23 2013-01-23
        816-46799 2002-02-19 to 2012-07-02 ODY THEMIS VISRDR 177,048 571,592 1,591,958.70
        2013-01-23 2013-01-23 816-46799 2002-02-19 to 2012-07-02 VO VISAB EDR 50,506
        353,542 94,885.56 2013-01-23 2013-01-25 0-1485 1976-06-22 to 1980-07-30 VO
        VISAB MDIM 8,548 29,124 19,944.45 2012-09-14 2012-11-02 169-1483 - VO VISAB
        DTM 233 1,165 1,012.69 2012-09-14 2012-10-18 - - Total 8,609,791 33,651,159
        146,370,814.11 2013-03-04 2013-03-04 - 1976-06-22 to 2071-01-16 Volume Table
        Volume Group Number Volumes Number Products Number Files File Size (MB) Last
        Time Product Added Last Time Synced Orbit Range Observation Range MEXHRS_2*
        1 8,530 26,795 566,705.72 2012-08-16 2012-12-28 10-5446 2004-01-10 to 2008-03-29
        MEXHRSC_0* 1 37,796 113,431 4,170,596.15 2012-12-28 2012-12-28 10-10821 2004-01-10
        to 2012-06-30 MEXHRSC_1* 1 32,245 96,772 4,823,521.87 2012-12-29 2012-12-29
        10-10821 2004-01-10 to 2012-06-30 MEXMDE_1* 2 5,383 11,528 8,443.02 2012-02-24
        2012-10-19 1885-3068 2005-07-04 to 2006-05-31 MEXMDI_1* 4 5,327 1,370,624
        165,449.75 2012-06-19 2012-10-20 1844-9879 2005-06-22 to 2011-09-30 MEXMDS_1*
        1 730 1,186 4,134.10 2012-02-24 2012-10-20 1885-2418 2005-07-04 to 2005-11-30
        MEXOMG_0* 4 18,535 18,753 693,004.28 2012-09-06 2012-10-19 -304-9182 2003-02-19
        to 2011-03-11 MEXPFS_1* 4 37,673 94,054 61,015.27 2012-02-23 2012-10-19 10-8944
        2003-05-02 to 2071-01-16 MGSL_2* 2 772 839 23,921.20 2009-03-11 2012-10-19
        0-20327 1997-09-15 to 2001-06-30 MGSL_3* 1 89 197 12,497.56 2009-03-11 2012-10-19
        3-20333 1997-09-15 to 2001-06-30 MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11
        2012-10-19 - 1999-02-28 to 2006-11-02 MROCR_0* 5 3,900,902 12,907,189 10,247,324.71
        2013-02-25 2013-02-25 - 1980-01-01 to 2014-01-09 MROCR_1* 4 783,105 1,567,254
        1,835,656.57 2013-02-25 2013-02-25 - 2006-09-27 to 2012-08-03 MROCR_2* 6 1,488,366
        3,722,465 28,491,359.96 2013-02-25 2013-02-25 - 2006-09-27 to 2012-08-03 MROCR_3*
        4 17,671 36,258 3,751,632.75 2012-02-29 2012-10-12 - - MROCR_5* 3 2,580 5,841
        5,579.02 2013-02-25 2013-02-25 - 2009-07-10 to 2012-05-24 MROCR_6* 1 18 284
        5,812.32 2012-03-16 2012-10-18 - 2008-01-09 to 2011-12-06 MROHR_0* 1 822,848
        3,016,806 101,546,532.41 2013-03-04 2013-03-04 1-30609 2006-03-24 to 2013-02-05
        MROM_0* 68 11,819 25,474 183,625.57 2013-03-01 2013-03-01 0-28189 2006-09-15
        to 2012-07-31 MROM_1* 68 11,814 26,698 278,769.73 2013-03-01 2013-03-01 0-28189
        2006-09-24 to 2012-07-31 MRORS_0* 1 10,250 20,602 342,716.36 2013-03-01 2013-03-01
        - 2006-01-01 to 2017-01-02 MRORS_1* 1 27 90 971.51 2012-03-01 2012-10-10 -
        1998-03-27 to 2011-05-05 MROSH_0* 2 11,809 35,849 2,716,861.79 2012-11-28
        2012-11-29 0-25993 2006-12-06 to 2012-02-11 MROSH_1* 2 11,807 47,650 4,169,773.78
        2012-11-28 2012-11-29 1689-25993 2006-12-06 to 2012-02-11 MSL_0* 1 606 10,922
        210,385.74 2012-02-27 2012-10-19 18056-24300 2010-06-03 to 2011-10-02 VO_1*
        46 50,506 254,044 92,585.84 2013-01-23 2013-01-25 0-1485 1976-06-22 to 1980-07-30
        VO_2* 22 8,781 34,771 20,117.24 2012-09-14 2012-11-02 0-1483 - MGSC* 588 243,526
        748,695 314,741.95 2009-03-11 2012-12-06 -97-33998 1997-09-15 to 2006-10-17
        MROX* 1,612 47,406 184,988 5,544,609.30 2013-03-01 2013-03-01 -4242-27891
        2005-08-30 to 2012-07-08 ODGC1* 1 28,918 57,867 675,600.75 2012-03-30 2012-12-23
        - 2002-02-19 to 2009-09-07 ODGD1* 1 2,625 5,281 2,644.56 2012-12-23 2012-12-23
        - 2002-02-19 to 2012-06-29 ODGE1* 1 31,050 422,699 484,789.02 2012-12-23 2012-12-23
        - 2001-04-25 to 2012-06-30 ODGH1* 1 125 279 35.75 2012-12-23 2012-12-23 -
        2002-02-21 to 2012-06-05 ODGM* 1 24 99 71.59 2012-03-30 2012-12-23 - 2002-06-04
        to 2005-04-03 ODGN1* 1 109 247 16.39 2012-12-23 2012-12-23 - 2002-01-25 to
        2012-06-05 ODGR1* 1 3,553 7,135 1,625.55 2012-12-23 2012-12-23 - 2002-02-18
        to 2012-06-30 ODGS1* 1 2,733 5,496 25,446.75 2012-03-30 2012-12-24 - 2002-06-08
        to 2009-05-25 ODTH 1 966,448 2,347,831 12,369,492.76 2013-01-23 2013-01-23
        816-46799 2002-02-19 to 2012-07-02 Total 2,466 8,609,052 27,232,105 183,888,156.15
        2013-03-04 2013-03-04 - 1976-06-22 to 2071-01-16 Data Set / Product Type Product
        Files This is a count of the number of files for each product type. NOTE:
        This is largerthan the number of files in a volume since somes files (such
        as DSMAP.CAT) are included in each product even though they are only included
        once in a volume Data Set / Product Type Product File Sizes This is a sum
        of the sizes for each file for each product type. NOTE: This is largerthan
        the sum of the size of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Last Time Product Added This is the last time any product in the given
        data set and product type or in the given volume was added to ODE Last Time
        Synced This is the last the volume or any volume containing the given data
        set with the given product type was synced with ODE. Syncing ensures that
        the contents of ODE matches the volume. This includes adding new products;
        updating metadata, browse, and location information; and removing any products
        listed in ODE that no longer appear in the volume (a rare event). Observation
        Range The observation range is taken from the products UTC Start and Stop
        time. There are a few products that have odd stop times (times later than
        the current date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_2_2013.html
    extraction_010:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_odeholdings_Mars_holdings_6_1_2023_html.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code to download data from the Orbital Data Explorer\
        \ (ODE) using STAC (SpatioTemporal Asset Catalog) terminology, you should\
        \ extract the following relevant information from the provided text:\n\n1.\
        \ **Data Identification**:\n   - Each dataset/product type is identified by:\n\
        \     - Mission: For example, \"EM16TGO\", \"MEX\", \"MRO\", \"VO\", etc.\n\
        \     - Instrument: For example, \"ACS\", \"CASSIS\", \"NOMAD\", \"HRSC\"\
        , \"MARSIS\", \"OMEGA\", etc.\n     - Product Type: For example, \"RAWHK\"\
        , \"RAWSC\", \"TCHANC\", \"CALANC\", etc.\n\n2. **Product Statistics**:\n\
        \   - Number of Products: Count of the available items in each product type.\n\
        \   - Number of Product Files: Total files associated with the product type.\n\
        \   - Product File Size (MB): Total file size for the product type.\n\n3.\
        \ **Update Information**:\n   - Last Time Product Added: Date of the last\
        \ item added to this product category.\n   - Last Time Synced: Date of the\
        \ last synchronization with ODE to ensure data consistency.\n\n4. **Observation\
        \ Details**:\n   - Orbit Range: Numerical range of the orbits covered by the\
        \ dataset, if applicable.\n   - Observation Range: Time period during which\
        \ observations were made, using UTC start and stop times.\n\n5. **STAC Integration**:\n\
        \   - STAC terminology requires using \"Items\" for individual observations,\
        \ \"Collections\" for groups of similar data, and \"Assets\" for the data\
        \ files.\n\nUsing this structure, you can proceed with writing Python code\
        \ to interact with the ODE, retrieve relevant datasets, and manage them in\
        \ a STAC-compliant format. If using STAC software libraries, you will format\
        \ each dataset as a \"Collection\" and individual observations as \"Items\"\
        \ with their respective metadata and data files listed as \"Assets\". \n\n\
        Would you like guidance on a specific aspect of the code, such as setting\
        \ up the STAC catalog, downloading data, or handling metadata?"
      prompt: ':::context_prompt :::extraction_prompt Orbital Data Explorer - Mars
        Holdings Orbital Data Explorer - Mars Holdings Updated: 2023-06-01T12:48 All
        Holdings Data Set / Product Type Table Mission Instrument Product Type Number
        Products Number Product Files* Product File Size (MB)* Last Time Product Added
        Last Time Synced Orbit Range Observation Range EM16TGO ACS RAWHK 38,424 76,848
        3,772.28 2023-05-03 2023-05-03 2-22071 2016-03-14 to 2022-11-03 EM16TGO ACS
        RAWSC 265 1,157 43,320.29 2022-04-27 2022-07-23 0-11373 2016-04-05 to 2020-06-11
        EM16TGO ACS TCHANC 1,467 2,934 178.70 2023-05-03 2023-05-03 - 2016-04-05 to
        2023-04-30 EM16TGO CASSIS CALANC 2 4 67.11 2021-03-09 2021-03-09 - - EM16TGO
        CASSIS CALSC 3,418,075 10,270,952 12,529,295.07 2023-05-14 2023-05-14 1742-17558
        2018-04-14 to 2021-10-30 EM16TGO CASSIS PARHK 43,164 86,328 13,565.19 2023-05-01
        2023-05-01 0-22047 2016-03-14 to 2022-11-01 EM16TGO CASSIS RAWHK 74,824 149,648
        15,951.45 2023-05-04 2023-05-04 0-22059 2016-03-14 to 2022-11-02 EM16TGO CASSIS
        RAWSC 3,901,363 19,398,199 4,652,758.92 2023-05-04 2023-05-04 0-22058 2016-04-07
        to 2022-11-02 EM16TGO CASSIS TCHANC 1,424 2,848 471.49 2023-05-01 2023-05-01
        - 2016-04-07 to 2023-04-29 EM16TGO NOMAD CALSC 33,607 132,274 219,217.23 2022-10-31
        2022-10-31 1829-19786 2018-04-21 to 2022-04-30 EM16TGO NOMAD PARHK 13,129
        26,258 15,250.13 2023-05-03 2023-05-03 8-22071 2016-04-04 to 2022-11-03 EM16TGO
        NOMAD PARSC 69,461 138,922 11,392,799.90 2023-05-03 2023-05-03 0-22071 2016-04-04
        to 2022-11-04 EM16TGO NOMAD RAWHK 13,129 26,258 14,021.39 2023-05-03 2023-05-03
        8-22071 2016-04-04 to 2022-11-03 EM16TGO NOMAD RAWSC 112,671 225,342 11,368,797.95
        2023-05-03 2023-05-03 0-22071 2016-04-04 to 2022-11-04 EM16TGO NOMAD TCHANC
        1,486 2,972 96.81 2023-05-03 2023-05-03 - 2016-04-04 to 2023-04-30 MEX HRSC
        DTMRDR 9,286 73,532 616,779.10 2014-06-05 2022-08-19 10-6567 2004-01-10 to
        2009-02-12 MEX HRSC PHOBOS 198 1,386 3,509.76 2016-06-16 2022-08-19 - 2004-08-22
        to 2011-07-03 MEX HRSC RDRV4 65,323 391,938 6,677,694.92 2023-05-01 2023-05-01
        10-23996 2004-01-10 to 2022-12-31 MEX HRSC REFDR3 43,888 394,992 7,295,562.96
        2020-05-18 2023-05-13 10-19592 2004-01-10 to 2019-06-29 MEX HRSC REFDR4 7,127
        64,143 2,039,531.01 2023-05-12 2023-05-12 18976-23498 2019-01-01 to 2022-08-08
        MEX MARSIS EDR 29,139 145,695 116,795.97 2021-01-20 2021-01-20 1-20228 2003-06-16
        to 2019-12-31 MEX MARSIS RDRAIS 11,273 3,846,404 463,738.95 2019-07-31 2023-04-13
        1844-18349 2005-06-22 to 2018-07-02 MEX MARSIS RDRSS 8,459 42,295 224,850.04
        2021-01-21 2022-08-19 1885-20221 2005-07-04 to 2019-12-29 MEX OMEGA DDRGM
        8 46 1,476.99 2015-04-29 2021-01-17 6-8485 2004-01-08 to 2010-08-20 MEX OMEGA
        EDR 32,489 123,828 1,816,052.84 2023-05-02 2023-05-02 -304-23299 2003-02-19
        to 2022-06-11 MEX PFS EDR 110,829 420,837 158,710.27 2023-04-13 2023-04-13
        20-18975 2003-06-23 to 2018-12-31 MEX VMC EDR 70,062 222,140 29,208.45 2022-12-15
        2022-12-15 -1-22741 2003-06-06 to 2021-12-31 MEX VMC RDR 70,062 222,140 288,662.44
        2022-12-15 2022-12-15 -1-22741 2003-06-06 to 2021-12-31 MGS MOC-NA/WA NADSDP
        1,234 3,641 5,062.84 2013-11-05 2015-07-16 - 1997-09-15 to 1998-09-12 MGS
        MOC-NA/WA NASDP 95,802 191,485 204,048.94 2009-03-11 2015-08-04 -97-33982
        1999-02-28 to 2006-10-15 MGS MOC-NA/WA WADSDP 814 2,436 634.66 2013-11-05
        2015-07-16 - 1997-09-15 to 1998-09-12 MGS MOC-NA/WA WASDP 145,676 291,340
        60,892.12 2009-03-11 2015-08-04 -97-33998 1999-02-28 to 2006-10-17 MGS MOLA
        MEGDR 89 445 12,514.18 2009-03-11 2017-08-25 3-20333 1997-09-15 to 2001-06-30
        MGS MOLA PEDR 771 7,710 23,968.75 2009-03-11 2015-06-03 1578-20327 1999-02-28
        to 2001-06-30 MGS MOLA PRDR 2,546 7,638 40,139.32 2009-03-11 2015-06-03 -
        1999-02-28 to 2006-11-02 MGS MOLA SHADR 1 2 0.52 2009-03-11 2015-06-03 - 1997-09-15
        to 1999-12-31 MGS TES TIMAP 4 20 162.32 2013-10-28 2018-01-17 - - MGS TES
        TSDR 326 23,702 198,114.76 2013-10-28 2015-07-06 - - MRO CRISM ANCILL 7,461
        14,922 675.08 2022-08-31 2023-05-30 - 2006-09-27 to 2022-05-07 MRO CRISM CDR
        3,177,157 6,354,314 703,833.47 2023-05-30 2023-05-30 - 1980-01-01 to 2023-02-09
        MRO CRISM DDR 1,025,382 2,050,764 6,733,033.81 2022-05-27 2022-05-27 - 2006-09-27
        to 2022-02-08 MRO CRISM EDR 2,588,671 15,503,825 29,087,771.39 2022-09-01
        2023-05-30 - 2006-09-27 to 2022-05-07 MRO CRISM LDR 5,928 11,856 12,307.65
        2017-08-28 2022-06-05 - 2009-07-10 to 2017-04-29 MRO CRISM MRDR 22,567 169,039
        5,823,545.14 2023-04-18 2023-04-18 - - MRO CRISM MTRDR 10,408 957,515 13,640,386.43
        2022-01-27 2022-06-06 840-27269 2006-09-30 to 2012-05-21 MRO CRISM TER 10,407
        1,363,305 6,716,621.04 2022-01-28 2022-06-07 840-27269 2006-09-30 to 2012-05-21
        MRO CRISM TRDR 1,985,070 8,106,703 98,312,484.04 2023-01-02 2023-01-02 - 2006-09-27
        to 2022-05-07 MRO CRISM VALREP 412,010 824,020 9,575.78 2022-09-01 2023-05-30
        - 2006-09-27 to 2022-05-07 MRO CTX EDR 135,507 397,443 14,978,605.57 2023-02-28
        2023-02-28 -4242-75458 2005-08-30 to 2022-09-01 MRO HIRISE ANAGLY 8,467 25,401
        2,971,488.51 2023-05-04 2023-05-04 - - MRO HIRISE DTM 969 34,918 1,501,358.09
        2023-05-04 2023-05-04 - - MRO HIRISE EDR 2,124,966 10,566,861 57,263,794.17
        2023-05-05 2023-05-05 1-78199 2006-03-24 to 2023-04-02 MRO HIRISE RDR 10 199
        23,890.50 2012-02-24 2021-01-16 2-7519 2006-03-25 to 2008-03-04 MRO HIRISE
        RDRV11 158,315 3,536,589 232,948,521.72 2023-05-04 2023-05-04 1-78199 2006-03-24
        to 2023-04-02 MRO MCS DDR 32,542 130,168 248,555.05 2023-03-01 2023-03-01
        760-76240 2006-09-24 to 2022-10-31 MRO MCS EDR 33,294 99,882 526,114.49 2023-03-01
        2023-03-01 0-76240 2006-09-15 to 2022-10-31 MRO MCS RDR 33,289 99,867 791,421.30
        2023-03-01 2023-03-01 759-76240 2006-09-24 to 2022-10-31 MRO RSS EDR 31,077
        70,654 1,017,045.98 2023-05-30 2023-05-30 - 2006-01-01 to 2023-06-27 MRO RSS
        RSDMAP 30 98 593.09 2016-05-27 2020-10-30 - 1998-03-27 to 2015-04-30 MRO RSS
        SHADR 8 16 6.25 2020-10-30 2020-10-30 - 1998-03-27 to 2019-08-05 MRO RSS SHBDR
        4 8 2,285.01 2017-02-27 2020-10-30 - 1998-03-27 to 2015-04-30 MRO SHARAD EDR
        33,447 200,682 7,950,857.01 2023-03-13 2023-03-13 0-75225 2006-12-06 to 2022-08-13
        MRO SHARAD RDR 33,441 167,205 11,820,902.27 2023-03-14 2023-03-14 1689-75225
        2006-12-06 to 2022-08-13 MRO SHARAD SHARAD3D 2 662 315,906.17 2021-11-03 2021-11-12
        - 2006-12-06 to 2015-09-10 MRO SHARAD SHSIMU 30,728 399,464 5,749,492.97 2023-03-02
        2023-03-02 - 2006-12-06 to 2022-05-25 MRO SHARAD USGEOMV2 31,837 63,674 10,901.35
        2023-05-30 2023-05-30 1689-76399 2006-12-06 to 2022-11-13 MRO SHARAD USRDRV2
        31,837 127,348 1,925,402.02 2023-05-31 2023-05-31 1689-76399 2006-12-06 to
        2022-11-13 ODY GRS AHD 250 750 65.00 2023-03-31 2023-03-31 - 2002-02-21 to
        2022-09-08 ODY GRS AND 439 1,317 53.12 2023-03-31 2023-03-31 - 2002-01-25
        to 2022-10-04 ODY GRS CGS 28,918 86,754 675,993.58 2012-03-30 2015-10-13 -
        2002-02-19 to 2009-09-07 ODY GRS CMDLST 3,585 10,755 5,378.71 2022-09-30 2023-04-01
        - 2001-04-25 to 2022-02-26 ODY GRS DHD 7,172 21,516 3,335.50 2023-03-31 2023-03-31
        - 2002-02-18 to 2022-09-30 ODY GRS DND 11,290 33,870 11,700.79 2023-03-31
        2023-03-31 - 2002-02-19 to 2022-09-30 ODY GRS EKERNL 310 1,238 4.99 2022-01-05
        2023-04-01 - 2001-04-25 to 2021-05-12 ODY GRS ELEMTS 24 163 212.34 2012-03-30
        2015-10-13 - 2002-06-04 to 2005-04-03 ODY GRS GAMMAS 2,651 7,953 358,124.54
        2018-10-03 2023-04-01 - 2001-05-02 to 2009-09-30 ODY GRS GRSENG 15,438 661,945
        54,880.96 2023-04-01 2023-04-01 - 2001-04-25 to 2022-09-30 ODY GRS HENDS 7,425
        22,275 26,671.23 2023-04-01 2023-04-01 - 2001-05-02 to 2022-09-30 ODY GRS
        IDND 75 150 20.40 2022-08-05 2022-08-19 - 2002-02-22 to 2020-12-31 ODY GRS
        MESSLG 7,664 22,992 18,091.14 2023-04-01 2023-04-01 - 2001-04-25 to 2022-09-30
        ODY GRS NEUTNS 7,392 22,176 62,527.70 2023-04-01 2023-04-01 - 2001-05-02 to
        2022-09-30 ODY GRS PROFIL 2,365 7,095 6,501.12 2018-10-03 2023-04-01 - 2001-06-27
        to 2009-09-07 ODY GRS PULSRS 2,621 7,863 16,866.46 2018-10-03 2023-04-01 -
        2001-05-02 to 2010-07-30 ODY GRS SGS 2,733 8,199 25,478.17 2012-03-30 2015-10-13
        - 2002-06-08 to 2009-05-25 ODY THEMIS IRBTR 319,537 1,202,965 703,281.33 2023-04-01
        2023-04-01 816-91899 2002-02-19 to 2022-09-02 ODY THEMIS IREDR 964,727 3,283,901
        3,799,906.33 2023-04-01 2023-04-01 816-91899 2002-02-19 to 2022-09-02 ODY
        THEMIS IRGEO1 63,999 431,314 2,106,417.79 2014-10-30 2021-02-02 2400-50098
        2002-06-30 to 2013-03-31 ODY THEMIS IRGEO2 319,212 2,110,840 12,903,362.74
        2023-04-02 2023-04-02 - 2002-02-19 to 2022-09-02 ODY THEMIS IRPBT1 63,765
        127,530 291,848.96 2014-11-02 2021-02-07 2400-50098 2002-06-30 to 2013-03-31
        ODY THEMIS IRPBT2 163,245 489,733 2,088,668.87 2023-04-02 2023-04-02 816-91899
        2002-02-19 to 2022-09-02 ODY THEMIS IRRDR 635,891 1,745,344 6,686,729.92 2023-04-01
        2023-04-01 816-91899 2002-02-19 to 2022-09-02 ODY THEMIS VGEO1 182,376 775,775
        2,978,463.21 2016-11-03 2021-02-13 2400-50097 2002-06-30 to 2013-03-31 ODY
        THEMIS VGEO2 148,887 792,866 3,410,955.48 2023-04-01 2023-04-01 816-91896
        2002-02-19 to 2022-09-01 ODY THEMIS VISABR 272,700 955,435 1,268,379.38 2023-04-01
        2023-04-01 816-91896 2002-02-19 to 2022-09-01 ODY THEMIS VISALB 66,053 198,158
        766,916.34 2023-04-02 2023-04-02 816-91896 2002-02-19 to 2022-09-01 ODY THEMIS
        VISEDR 273,562 958,412 1,420,858.13 2023-04-01 2023-04-01 816-91899 2002-02-19
        to 2022-09-02 ODY THEMIS VISRDR 272,174 953,736 2,389,037.16 2023-04-01 2023-04-01
        816-91896 2002-02-19 to 2022-09-01 VO VISAB DTM 233 1,165 1,013.77 2012-09-14
        2021-01-22 - - VO VISAB EDR 50,506 353,542 95,216.20 2013-01-23 2021-01-22
        0-1485 1976-06-22 to 1980-07-30 VO VISAB MDIM 5,137 6,125 4,657.36 2017-02-17
        2021-01-22 - - VO VISAB MDIMC 3,826 3,826 3,827.60 2013-11-05 2021-01-22 169-1483
        1977-02-07 to 1980-07-27 VO VISAB MDIMH 2,116 2,116 3,221.25 2012-09-14 2021-01-22
        - - Total 24,301,026 103,605,935 603,823,718.88 2023-05-31 2023-05-31 - 1976-06-22
        to 2023-06-27 Volume Table Volume Group Number Volumes Number Products Number
        Files File Size (MB) Last Time Product Added Last Time Synced Orbit Range
        Observation Range em16_t* 3 7,722,491 28,905,967 38,328,915.00 2023-05-14
        2023-05-14 0-22071 2016-03-14 to 2023-04-30 MEXHRS_1* 1 43,888 219,478 7,296,098.79
        2020-05-18 2023-05-13 10-19592 2004-01-10 to 2019-06-29 MEXHRS_2* 1 9,286
        29,150 611,336.64 2014-06-05 2022-08-19 10-6567 2004-01-10 to 2009-02-12 mexhrs_4*
        9 65,323 196,284 6,679,597.85 2023-05-01 2023-05-01 10-23996 2004-01-10 to
        2022-12-31 MEXHRS_5* 1 198 1,027 3,507.39 2016-06-16 2022-08-19 - 2004-08-22
        to 2011-07-03 mexhrs_6* 2 7,127 36,763 2,071,255.92 2023-05-12 2023-05-12
        18976-23498 2019-01-01 to 2022-08-08 MEXMDE_1* 1 1,818 4,132 2,920.77 2015-04-29
        2015-07-30 1885-2418 2005-07-04 to 2005-11-30 MEXMDI_1* 7 11,273 3,845,848
        465,338.61 2019-07-31 2023-04-13 1844-18349 2005-06-22 to 2018-07-02 MEXME_1*
        8 29,139 87,951 116,948.62 2021-01-20 2021-01-20 1-20228 2003-06-16 to 2019-12-31
        MEXMRS_1* 8 8,459 34,504 226,401.36 2021-01-21 2022-08-19 1885-20221 2005-07-04
        to 2019-12-29 MEXOMG_0* 9 32,489 33,030 1,815,912.76 2023-05-02 2023-05-02
        -304-23299 2003-02-19 to 2022-06-11 MEXOMG_2* 1 8 95 4,415.38 2015-04-29 2021-01-17
        6-8485 2004-01-08 to 2010-08-20 MEXPFS_1* 7 110,829 222,351 156,827.43 2023-04-13
        2023-04-13 20-18975 2003-06-23 to 2018-12-31 MEXVMC_L* 18 140,124 561,126
        327,647.17 2022-12-15 2022-12-15 -1-22741 2003-06-06 to 2021-12-31 MGSL_2*
        2 772 835 23,778.55 2009-03-11 2015-06-03 0-20327 1997-09-15 to 2001-06-30
        MGSL_3* 1 89 290 12,497.94 2009-03-11 2017-08-25 3-20333 1997-09-15 to 2001-06-30
        MGSLR_X* 1 2,546 5,112 40,087.59 2009-03-11 2015-06-03 - 1999-02-28 to 2006-11-02
        MGST_1* 326 326 52,004 202,080.67 2013-10-28 2015-07-06 - - MGST_9* 1 4 31
        162.43 2013-10-28 2018-01-17 - - MROCR_0* 15 6,185,299 20,722,365 29,649,825.22
        2023-05-30 2023-05-30 - 1980-01-01 to 2023-02-09 MROCR_1* 14 1,025,382 2,053,829
        6,734,493.03 2022-05-27 2022-05-27 - 2006-09-27 to 2022-02-08 MROCR_2* 16
        1,985,070 5,132,298 96,784,487.82 2023-01-02 2023-01-02 - 2006-09-27 to 2022-05-07
        MROCR_3* 5 22,567 137,756 5,782,654.79 2023-04-18 2023-04-18 - - MROCR_4*
        1 10,408 936,673 13,571,782.06 2022-01-27 2022-06-06 840-27269 2006-09-30
        to 2012-05-21 MROCR_5* 8 5,928 13,152 12,522.59 2017-08-28 2022-06-05 - 2009-07-10
        to 2017-04-29 MROCR_6* 1 10,407 1,352,792 6,649,923.35 2022-01-28 2022-06-07
        840-27269 2006-09-30 to 2012-05-21 MROHR_0* 1 2,292,727 8,831,325 256,535,544.99
        2023-05-05 2023-05-05 1-78199 2006-03-24 to 2023-04-02 MROM_0* 191 33,294
        71,745 524,414.78 2023-03-01 2023-03-01 0-76240 2006-09-15 to 2022-10-31 MROM_1*
        181 33,289 75,615 789,646.12 2023-03-01 2023-03-01 0-76240 2006-09-24 to 2022-10-31
        MROM_2* 364 32,542 71,996 251,082.51 2023-03-01 2023-03-01 0-76240 2006-09-24
        to 2022-10-31 MRORS_0* 1 31,077 62,310 1,016,611.33 2023-05-30 2023-05-30
        - 2006-01-01 to 2023-06-27 MRORS_1* 1 42 1,121 3,343.77 2020-10-30 2020-10-30
        - 1998-03-27 to 2019-08-05 MROSH_0* 4 33,447 101,185 7,948,714.55 2023-03-13
        2023-03-13 0-75225 2006-12-06 to 2022-08-13 MROSH_1* 4 33,441 134,608 11,818,925.28
        2023-03-14 2023-03-14 1689-75225 2006-12-06 to 2022-08-13 MROSH_2* 1 63,674
        254,724 2,021,594.76 2023-05-31 2023-05-31 1689-76399 2006-12-06 to 2022-11-13
        MROSH_3* 1 2 720 580,261.43 2021-11-03 2021-11-12 - 2006-12-06 to 2015-09-10
        mrosh_s* 1 30,728 399,485 5,749,550.04 2023-03-02 2023-03-02 - 2006-12-06
        to 2022-05-25 VO_1* 46 50,506 254,044 92,585.84 2013-01-23 2021-01-22 0-1485
        1976-06-22 to 1980-07-30 VO_2* 22 11,312 19,920 12,984.82 2017-02-17 2021-01-22
        0-1483 1977-02-07 to 1980-07-27 MGSC* 588 243,526 748,695 314,741.91 2013-11-05
        2015-08-04 -97-33998 1997-09-15 to 2006-10-17 MROX* 4,348 135,507 523,539
        15,139,291.24 2023-02-28 2023-02-28 -4242-75458 2005-08-30 to 2022-09-01 ODGC1*
        1 28,918 57,867 675,600.75 2012-03-30 2015-10-13 - 2002-02-19 to 2009-09-07
        ODGD1* 1 6,358 12,747 6,556.36 2023-03-31 2023-03-31 - 2002-02-19 to 2022-09-30
        ODGE1* 1 49,451 715,002 548,695.34 2023-04-01 2023-04-01 - 2001-04-25 to 2022-09-30
        ODGH1* 1 250 529 67.44 2023-03-31 2023-03-31 - 2002-02-21 to 2022-09-08 ODGM*
        1 24 99 71.59 2012-03-30 2015-10-13 - 2002-06-04 to 2005-04-03 ODGN1* 2 319
        684 3,402.88 2023-03-31 2023-03-31 - 2002-01-25 to 2022-10-04 ODGR1* 1 7,172
        14,373 3,298.74 2023-03-31 2023-03-31 - 2002-02-18 to 2022-09-30 ODGS1* 1
        2,733 5,496 25,446.75 2012-03-30 2015-10-13 - 2002-06-08 to 2009-05-25 ODTH
        2 3,746,128 6,869,763 38,820,032.87 2023-04-02 2023-04-02 816-91899 2002-02-19
        to 2022-09-02 Total 6,232 24,297,717 83,812,435 560,453,885.80 2023-05-31
        2023-05-31 - 1976-06-22 to 2023-06-27 Data Set / Product Type Product Files
        This is a count of the number of files for each product type. NOTE: This is
        largerthan the number of files in a volume since somes files (such as DSMAP.CAT)
        are included in each product even though they are only included once in a
        volume Data Set / Product Type Product File Sizes This is a sum of the sizes
        for each file for each product type. NOTE: This is largerthan the sum of the
        size of files in a volume since somes files (such as DSMAP.CAT) are included
        in each product even though they are only included once in a volume Last Time
        Product Added This is the last time any product in the given data set and
        product type or in the given volume was added to ODE Last Time Synced This
        is the last the volume or any volume containing the given data set with the
        given product type was synced with ODE. Syncing ensures that the contents
        of ODE matches the volume. This includes adding new products; updating metadata,
        browse, and location information; and removing any products listed in ODE
        that no longer appear in the volume (a rare event). Observation Range The
        observation range is taken from the products Utc Start and Stop time. There
        are a few products that have odd stop times (times later than the current
        date).

        '
      url: https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_1_2023.html
    generating_summary:
      action: generate_text
      completed: true
      depends-on: extraction
      prompt: ':::context_prompt :::summarize_prompt

        '
      runnable: false
    web_crawl:
      action: web_crawl
      completed: true
      max_iterations: 100
      runnable: false
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2
    writing_code:
      action: generate_text
      completed: true
      depends-on: generating_summary
      runnable: false
  vars:
    context_prompt: 'We want to write Python code to download data from the Orbital
      Data Explorer, ODE

      for short, using STAC terminology.

      '
    crawl_seeds:
    - https://ode.rsl.wustl.edu/
    - https://oderest.rsl.wustl.edu/
    - https://pds-geosciences.wustl.edu/dataserv/default.htm
    - https://github.com/samiriff/mars-ode-data-access
    extraction_prompt: 'Extract the information relevant to this objective from the
      following text.

      '
    summarize_prompt: 'Summarize the following information in the context of this
      objective.

      '
  versions:
    downloading_a_datacube:
      nodes: {}
      vars:
        context_prompt: 'We want to write Python code to download data from the Orbital
          Data Explorer, ODE

          for short, using STAC terminology.

          '

```

</details>


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-wryjqi/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-wryjqi](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-wryjqi.tar.gz)

🔥

---

- [round 1](./round-1.md)
