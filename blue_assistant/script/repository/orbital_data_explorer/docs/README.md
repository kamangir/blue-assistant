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
      Our objective is to access the Orbital Data Explorer, ODE for short, using STAC 
      terminology. For this purpose, we consider ODE as a catalog and each separate dataset 
      in ODE as a collection that contains items. We call these items objects or datacubes.

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
        max_iterations: 5

    expanding_the_extractions:
      action: expanding_the_extractions
      max_nodes: 100
      test_mode:
        max_nodes: 5
      depends-on: web_crawl

    extraction:
      action: generate_text
      prompt: >
        :::context_prompt
        :::extraction_prompt
        :::page_content
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

```
[metadata.yaml](../metadata.yaml)

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer .

@publish tar .
```



<details>
<summary>metadata</summary>

```yaml
script:
  nodes:
    expanding_the_extractions:
      action: expanding_the_extractions
      completed: true
      depends-on: web_crawl
      max_nodes: 5
      test_mode:
        max_nodes: 5
    extraction_001:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC (SpatioTemporal Asset Catalog) terminology, you need to consider
        the following approach:


        1. **Catalog:** The ODE is considered as a catalog. In STAC, a catalog is
        a container for collections and can provide metadata about the entire dataset.


        2. **Collections:** Each separate dataset within ODE is considered a collection.
        A collection in STAC represents a group of related items (e.g., images, observations)
        that share common metadata.


        3. **Items/Objects/Datacubes:** Within each collection, you have items, which
        you refer to as objects or datacubes. In STAC terminology, items are individual
        pieces of data that contain metadata and references to the actual data files.


        With this structure in mind, your task involves:


        - Identifying the collections within the ODE. Each collection will need its
        own metadata describing the common attributes of the dataset.

        - For each collection, identifying and cataloging the items/objects/datacubes,
        providing the appropriate metadata for each item, including spatial and temporal
        information if applicable.

        - Making sure all metadata and data references are structured according to
        STAC specifications.


        This setup will allow you to access and query the ODE data using the STAC
        framework effectively.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_002:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To meet your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, you''ll need to conceptualize the ODE as a catalog.
        This means that:


        1. **Catalog**: The entire ODE is treated as a catalog, which is the top-level
        STAC object.


        2. **Collections**: Each separate dataset within the ODE acts as a collection.
        In STAC, a collection is a grouping of related items with shared metadata.


        3. **Items**: The individual items within these collections are referred to
        as objects or datacubes. In STAC, an item represents a tangible asset, such
        as a satellite image, with specific metadata.


        By structuring your access to ODE in this manner, you align with STAC''s hierarchical
        organization consisting of catalogs, collections, and items. This alignment
        will facilitate your interaction with the ODE using the STAC API standards.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_003:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve the objective of accessing the Orbital Data Explorer (ODE)
        using SpatioTemporal Asset Catalog (STAC) terminology, the following information
        can be extracted:


        1. **ODE as a Catalog**: ODE serves as the overarching catalog that contains
        various datasets.


        2. **Collections**: Each separate dataset within ODE is treated as a collection.
        In STAC, a collection groups together related items and provides metadata
        at a dataset level.


        3. **Items**: The individual data entities within each collection are referred
        to as items. These items are the fundamental units of data in STAC terminology.


        4. **Objects or Datacubes**: These items are specifically referred to as objects
        or datacubes in the context of ODE. They represent the actual data holdings
        that users will interact with.


        The aim is to map the structure and terminology of ODE into STAC to facilitate
        data discovery and management using a standardized approach.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_004:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, consider the following key points:


        1. **ODE as a Catalog**: Treat the ODE as the main catalog in the STAC framework.
        This means it serves as the entry point for accessing and organizing datasets.


        2. **Datasets as Collections**: Each separate dataset within the ODE is considered
        a collection. In STAC, a collection is a grouping of related items that share
        similar characteristics or metadata.


        3. **Items or Datacubes**: Within each collection, you''ll find items, which
        in the context of ODE are referred to as objects or datacubes. These represent
        the individual data entries or units that are part of the dataset.


        By structuring the ODE in this way, you can effectively utilize STAC to manage
        and access the data, facilitating better organization, search, and discovery
        of datasets and their corresponding data units within ODE.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_005:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, here''s how you can frame the information based on
        your requirements:


        1. **Catalog**: ODE itself is considered a catalog. In the context of STAC,
        a catalog serves as a collection of metadata descriptions that provide access
        to a number of related datasets or collections.


        2. **Collections**: Each dataset within the ODE is regarded as a collection.
        A collection in STAC terms is a group of related items that share a common
        specification and metadata. Each of these datasets will be represented as
        a distinct collection within the ODE catalog.


        3. **Items**: Within each collection, you have items, which in your case are
        referred to as objects or datacubes. In STAC terminology, an item is the fundamental
        unit that contains the actual data or references to the data, along with its
        associated metadata. These items provide detailed information about individual
        data entries or records within a collection.


        By organizing the ODE in this way, you can access and manage the data using
        the structured approach provided by STAC, allowing for standardized metadata
        and easier data interoperability and access.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
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
      max_iterations: 5
      output:
        https://github.com/samiriff/mars-ode-data-access: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/: text/html
        https://ode.rsl.wustl.edu/account/acctCreate.aspx?ReturnUrl=index.aspx: unknown
        https://ode.rsl.wustl.edu/account/login.aspx?ReturnUrl=index.aspx: unknown
        https://ode.rsl.wustl.edu/datasets: unknown
        https://ode.rsl.wustl.edu/download: unknown
        https://ode.rsl.wustl.edu/help: unknown
        https://ode.rsl.wustl.edu/index.aspx: unknown
        https://ode.rsl.wustl.edu/lunar: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mapsearch: unknown
        https://ode.rsl.wustl.edu/mars: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mars/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/mars/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/mars/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/tools?displaypage=footprint: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/tools?displaypage=molapedr: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/mercury/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/Tools_Tab/MRO_Coordinated_Observation_Tool/Intro.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/Creating ODE Bookmarks.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/bookmark_list.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/forgot_password.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/history_list.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/past_ode_cart_orders.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm: text/html
        https://ode.rsl.wustl.edu/mercury/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/tools?displaypage=footprint: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/moon/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/Creating ODE Bookmarks.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/bookmark_list.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/forgot_password.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/past_ode_cart_orders.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm: text/html
        https://ode.rsl.wustl.edu/moon/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/tools?displaypage=footprint: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/tools?displaypage=lolardr: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/tools?displaypage=lrodiviner: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_16_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_19_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_2_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_11_15_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_11_1_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_11_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_12_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_13_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_14_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_14_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_15_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_15_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_31_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_6_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_9_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_19_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_24_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_6_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_6_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_6_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_2_10_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_2_19_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_2_22_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_15_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_16_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_16_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_4_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_7_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_8_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_10_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_16_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_1_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_3_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_4_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_12_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_1_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_1_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_2_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_6_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_6_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_17_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_22_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_23_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_26_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_27_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_2_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_26_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_2_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_30_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_8_18_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_8_19_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_11_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_16_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_26_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_7_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_7_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_11_13_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_17_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_5_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_9_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_12_2025.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_16_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_28_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_30_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_5_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_7_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_9_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_10_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_13_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_16_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_20_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_20_2025.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_22_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_25_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_9_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_11_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_13_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_13_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_18_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_1_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_3_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_4_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_11_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_14_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_3_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_11_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_4_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_14_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_25_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_3_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_5_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_5_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_7_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_7_2_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_7_6_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_13_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_16_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_19_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_1_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_16_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_2_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_4_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_6_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_25_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_28_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_13_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_1_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_22_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_5_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_1_11_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_1_19_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_2_14_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_2_27_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_26_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_31_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_5_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_5_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_7_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_6_19_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_6_2_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_6_2_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_7_26_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_7_3_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_7_8_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_14_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_25_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_9_15_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_12_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_13_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_19_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_26_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_27_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_10_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_13_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_16_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_1_13_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_1_14_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_1_18_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_13_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_18_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_19_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_13_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_17_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_21_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_4_18_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_11_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_22_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_27_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_30_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_31_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_14_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_17_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_19_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_1_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_25_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_28_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_3_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_7_2_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_7_5_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_7_7_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_8_16_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_14_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_15_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_17_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/index.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/oldholding.html: text/html
        https://ode.rsl.wustl.edu/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: unknown
        https://ode.rsl.wustl.edu/productsearch: unknown
        https://ode.rsl.wustl.edu/tools: unknown
        https://ode.rsl.wustl.edu/tools?displaypage=coordinatedobs: unknown
        https://ode.rsl.wustl.edu/tools?displaypage=footprint: unknown
        https://ode.rsl.wustl.edu/tools?displaypage=lolardr: unknown
        https://ode.rsl.wustl.edu/tools?displaypage=lrodiviner: unknown
        https://ode.rsl.wustl.edu/venus: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/index.aspx: text/html
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=datasetexplorer: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=download: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=help: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=index.aspx: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=mapsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=productsearch: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/login.aspx?ReturnUrl=tools: text/html;
          charset=utf-8
        https://ode.rsl.wustl.edu/venus/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/Tools_Tab/MRO_Coordinated_Observation_Tool/Intro.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/Creating ODE Bookmarks.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/bookmark_list.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/forgot_password.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/history_list.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/past_ode_cart_orders.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/venus/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm: text/html
        https://ode.rsl.wustl.edu/venus/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/tools?displaypage=footprint: text/html; charset=utf-8
        https://oderest.rsl.wustl.edu/: text/html
        https://pds-geosciences.wustl.edu/dataserv/default.htm: text/html
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 5
    writing_code:
      action: generate_text
      completed: true
      depends-on: generating_summary
      runnable: false
  vars:
    context_prompt: "Our objective is to access the Orbital Data Explorer, ODE for\
      \ short, using STAC \nterminology. For this purpose, we consider ODE as a catalog\
      \ and each separate dataset \nin ODE as a collection that contains items. We\
      \ call these items objects or datacubes.\n"
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

```

</details>


[orbital-data-explorer-2025-03-16-bj8ghf](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-bj8ghf.tar.gz)

🔥

---

- [round 1](./round-1.md)
