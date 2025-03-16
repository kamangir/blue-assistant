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
        max_iterations: 2

    expanding_the_extractions:
      action: expanding_the_extractions
      max_nodes: 10
      test_mode:
        max_nodes: 5
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

```
[metadata.yaml](../metadata.yaml)

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer .

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
        max_nodes: 5
    extraction_001:
      action: generate_text
      cache: extraction_cache/github_com_samiriff_mars-ode-data-access.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "From the provided text, the relevant information related to accessing\
        \ the Orbital Data Explorer (ODE) using STAC terminology can be extracted\
        \ as follows:\n\n### Overview\n- **Objective**: Access data from the Mars\
        \ Orbital Data Explorer (ODE) using STAC terminology.\n- **Catalog**: ODE\
        \ is treated as a catalog.\n- **Collections**: Each dataset in ODE is considered\
        \ as a collection.\n- **Items**: The items within these collections are referred\
        \ to as objects or datacubes.\n\n### Access Method\n- This is facilitated\
        \ through a Python package available on GitHub, specifically the `samiriff/mars-ode-data-access`\
        \ repository.\n- The package provides an easy-to-use interface to access data\
        \ from ODE.\n\n### Features of the Python Package\n- Utilizes the ODE REST\
        \ Service.\n- Provides utility methods for processing high-resolution map-projected\
        \ JP2 images:\n  - Slicing images into equal-sized chunks and removing black\
        \ margins for machine learning processing.\n- Functionality includes constructing\
        \ HTTP requests to ODE with user-defined query parameters and processing the\
        \ results.\n\n### Query Parameters\n- Users can define queries using various\
        \ parameters such as:\n  - `target`: The planetary body (e.g., Mars, Mercury).\n\
        \  - `mission`: The mission name (e.g., MGS, MRO).\n  - `instrument`: Instrument\
        \ names (e.g., HIRISE, CRISM).\n  - `product_type`: Type of product (e.g.,\
        \ DTM).\n  - Geographical constraints: `western_lon`, `eastern_lon`, `min_lat`,\
        \ `max_lat`.\n  - Temporal constraints: `min_ob_time`, `max_ob_time`.\n\n\
        ### Processing Results\n- After querying, results can be processed with additional\
        \ parameters such as:\n  - `bin_type`: Type of binning used in images.\n \
        \ - `product_types`: Types of products to filter.\n\n### Miscellaneous\n-\
        \ Additional processing options include handling image chunks, alignment,\
        \ cropping, and dealing with black margins.\n\nThis information offers an\
        \ interface and parameters necessary for accessing and manipulating data from\
        \ the Mars Orbital Data Explorer in a manner aligned with STAC concepts."
      prompt: ':::context_prompt :::extraction_prompt GitHub - samiriff/mars-ode-data-access:
        Python package that provides an easy-to-use interface to access data from
        the Mars Orbital Data Explorer Skip to content Navigation Menu Toggle navigation
        Sign in Product GitHub Copilot Write better code with AI Security Find and
        fix vulnerabilities Actions Automate any workflow Codespaces Instant dev environments
        Issues Plan and track work Code Review Manage code changes Discussions Collaborate
        outside of code Code Search Find more, search less Explore All features Documentation
        GitHub Skills Blog Solutions By company size Enterprises Small and medium
        teams Startups Nonprofits By use case DevSecOps DevOps CI/CD View all use
        cases By industry Healthcare Financial services Manufacturing Government View
        all industries View all solutions Resources Topics AI DevOps Security Software
        Development View all Explore Learning Pathways Events & Webinars Ebooks &
        Whitepapers Customer Stories Partners Executive Insights Open Source GitHub
        Sponsors Fund open source developers The ReadME Project GitHub community articles
        Repositories Topics Trending Collections Enterprise Enterprise platform AI-powered
        developer platform Available add-ons Advanced Security Enterprise-grade security
        features Copilot for business Enterprise-grade AI features Premium Support
        Enterprise-grade 24/7 support Pricing Search or jump to... Search code, repositories,
        users, issues, pull requests... Search Clear Search syntax tips Provide feedback
        We read every piece of feedback, and take your input very seriously. Include
        my email address so I can be contacted Cancel Submit feedback Saved searches
        Use saved searches to filter your results more quickly Name Query To see all
        available qualifiers, see our documentation . Cancel Create saved search Sign
        in Sign up Reseting focus You signed in with another tab or window. Reload
        to refresh your session. You signed out in another tab or window. Reload to
        refresh your session. You switched accounts on another tab or window. Reload
        to refresh your session. Dismiss alert samiriff / mars-ode-data-access Public
        Notifications You must be signed in to change notification settings Fork 3
        Star 9 Python package that provides an easy-to-use interface to access data
        from the Mars Orbital Data Explorer License MIT license 9 stars 3 forks Branches
        Tags Activity Star Notifications You must be signed in to change notification
        settings Code Issues 0 Pull requests 0 Actions Projects 0 Security Insights
        Additional navigation options Code Issues Pull requests Actions Projects Security
        Insights samiriff/mars-ode-data-access master Branches Tags Go to file Code
        Folders and files Name Name Last commit message Last commit date Latest commit
        History 21 Commits ode_data_access ode_data_access .gitignore .gitignore LICENSE
        LICENSE README.md README.md VERSION VERSION main.py main.py setup.cfg setup.cfg
        setup.py setup.py View all files Repository files navigation README MIT license
        Mars Orbital Data Explorer Access This project aims to provide an easy-to-use
        interface to access data from the Mars Orbital Data Explorer (ODE) , maintained
        by the Geosciences Node of NASA''s Planetary Data System (PDS), via the ODE
        REST Service Since the data return by the ODE usually consists of high-resolution
        map-projected JP2 images, utility methods have also been provided to slice
        each image into equal-size chunks with all black-margins cropped out so that
        they can be processed by appropriate machine learning models. _____ ________
        ________ ___________ ________ __ _____ / \ _____ _______ ______ \_____ \ \______
        \ \_ _____/ \______ \ _____ _/ |______ / _ \ ____ ____ ____ ______ ______
        / \ / \\__ \\_ __ \/ ___/ ______ / | \ | | \ | __)_ ______ | | \\__ \\ __\__
        \ ______ / /_\ \_/ ___\/ ___\/ __ \ / ___// ___// Y \/ __ \| | \/\___ \ /_____/
        / | \| ` \| \ /_____/ | ` \/ __ \| | / __ \_ /_____/ / | \ \__\ \__\ ___/
        \___ \ \___ \ \____|__ (____ /__| /____ > \_______ /_______ /_______ / /_______
        (____ /__| (____ / \____|__ /\___ >___ >___ >____ >____ > \/ \/ \/ \/ \/ \/
        \/ \/ \/ \/ \/ \/ \/ \/ \/ Project Structure root/ ode_data_access/ autocropper.py
        Aligns, rotates and crops images to remove black margins chunk_processor.py
        Slices a high-resolution (m x n) image into (m / p x n / p) chunks, where
        each chunk is of size (p x p) image_utils.py Utility methods to process images
        lblreader.py Reads an LBL file and converts it into a map of key-value pairs
        query_processor.py Constructs a HTTP Request to be sent to the Orbital Data
        Explorer, using user-defined query parameters query_result_processor.py Processes
        the results sent by the Orbital Data Explorer in response to a user-defined
        query LICENSE main.py Provides Sample Usage of package README.md setup.cfg
        setup.py VERSION Basic Usage Run main.py to generate a sample query and fetch
        sample results: python main.py The entire process consists of 3 steps: 1.
        Initialize Query Processor Initialize an instance of the QueryProcessor class
        to process user-defined query parameters, details of which are given in the
        upcoming sections: query_processor = QueryProcessor()query_results = query_processor.query_files_urls(target,
        mission, instrument, product_type, western_lon, eastern_lon, min_lat, max_lat,
        min_ob_time, max_ob_time, product_id, file_name, number_product_limit, result_offset_number)
        Supported Query Parameters The list of supported query parameters is as shown
        below: Parameter Description target Aimed planetary body, i.e., Mars, Mercury,
        Moon, Phobos, or Venus mission Aimed mission, e.g., MGS or MRO instrument
        Aimed instrument from the mission, e.g., HIRISE or CRISM product_type Type
        of product to look for, e.g., DTM or RDRV11 western_lon Western longitude
        to look for the data, from 0 to 360 eastern_lon Eastern longitude to look
        for the data, from 0 to 360 min_lat Minimal latitude to look for the data,
        from -90 to 90 max_lat Maximal latitude to look for the data, from -90 to
        90 product_id PDS Product Id to look for, with wildcards (*) allowed min_ob_time
        Minimal observation time in (even partial) UTC format, e.g., ''2017-03-01''
        max_ob_time Maximal observation time in (even partial) UTC format, e.g., ''2017-03-01''
        file_name File name to look for, with wildcards (*) allowed number_product_limit
        Maximal number of products to return (100 at most) result_offset_number Offset
        the return products, to go beyond the limit of 100 returned products remove_ndv
        Replace the no-data value as mentionned in the label by np.nan 2. Initialize
        Query Result Processor Initialize an instance of the QueryResultProcessor
        class to process the results returned by your QueryProcessor instance. In
        this step, you will have to specify user-defined parameters for the chunks
        and bin type (if applicable): query_result_processor = QueryResultProcessor()should_continue
        = query_result_processor.download(query_results, bin_type, product_types)##
        Add the following lines only if you wish to chunkify all downloaded imagesif
        should_continue: query_result_processor.process(SAVE_DIR_PREFIX, CHUNK_SIZE,
        SKIP_BLACK_IMAGES, ALIGN_AND_CROP_THRESHOLDS, None) Supported Query Result
        Parameters The list of supported query result parameters is as shown below:
        Parameter Description bin_type Type of binning used in image - Bin1 = 0.35
        cm/pixel, Bin2 = 2xBin1, Bin4 = 2xBin2 product_types Set of product types
        to which any downloaded product should belong. Eg., PRODUCT DATA FILE, BROWSE,
        GREYSCALE THUMBNAIL Chunk Parameters The following parameters can be used
        to control how chunks are processed: Parameter Description save_dir_prefix
        Prefix to be used in the name of the directory where the chunks of an image
        will be saved. For eg., chunks of an image "ESP_123_456.JP2" will be saved
        in a directory named "save_dir_prefix_ESP_123_456" chunk_size Size of each
        chunk that will be sliced from a high-resolution image. Eg., 1024 vectorized_chunks
        List in which all chunks of all JP2 images will be aggregated. If not required,
        just assign None skip_black_images Flag to indicate that all images containing
        black pixels near the center should be skipped Chunk Alignment and Cropping
        Thresholds The following parameters can be used to control how a chunk containing
        black margins, is aligned, cropped and/or rotated: Parameter Description max_border_size
        Border to be checked around the image while aligning and cropping black margins
        safety_margin Removes extra pixels from the sides to make sure no black remains
        while aligning and cropping black margins tolerance A gray value is more likely
        to be considered black when you increase the tolerance 3. Vectorized Chunks
        (Optional) If you wish to accumulate all chunks of all images into a python
        list, then initialize an empty list before step 1, and each time you call
        the QueryResultProcessor for multiple queries, pass this list as the vectorized_chunks
        parameter: query_result_processor.process(SAVE_DIR_PREFIX, CHUNK_SIZE, SKIP_BLACK_IMAGES,
        ALIGN_AND_CROP_THRESHOLDS, vectorized_chunks) Acknowledgements scikit-dataaccess
        Autocroppy scikit-image About Python package that provides an easy-to-use
        interface to access data from the Mars Orbital Data Explorer Topics nasa rest-api
        crop ode mars preprocessing jp2 pds chunks Resources Readme License MIT license
        Activity Stars 9 stars Watchers 0 watching Forks 3 forks Report repository
        Releases No releases published Packages 0 No packages published Languages
        Python 100.0% Footer 2025 GitHub,Inc. Footer navigation Terms Privacy Security
        Status Docs Contact Manage cookies Do not share my personal information You
        cant perform that action at this time.

        '
      url: https://github.com/samiriff/mars-ode-data-access
    extraction_002:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To access the Orbital Data Explorer (ODE) using STAC terminology, you\
        \ can consider the following information extracted from the text:\n\n1. **ODE\
        \ as a Catalog**:\n   - The Orbital Data Explorer is viewed as a catalog that\
        \ contains various datasets related to the planetary science data archives.\n\
        \n2. **Collections within ODE**:\n   - Each dataset in the ODE represents\
        \ a collection. These are organized based on planetary targets and missions.\
        \ The main collections are based on celestial bodies and their respective\
        \ missions:\n     - ***Mars***: Collections include data from missions like\
        \ Mars Reconnaissance Orbiter (MRO), 2001 Mars Odyssey, Mars Global Surveyor\
        \ (MGS), Viking Orbiter 1 and 2, ESA's Mars Express, and ExoMars Trace Gas\
        \ Orbiter.\n     - ***Moon*** (Lunar ODE): Collections include data from missions\
        \ like Lunar Reconnaissance Orbiter (LRO), Gravity Recovery and Interior Laboratory\
        \ (GRAIL), Clementine, Lunar Prospector, Lunar Orbiter, JAXA's SELENE, and\
        \ ISRO's Chandrayaan-1.\n     - ***Mercury***: Collection consists of data\
        \ from the MESSENGER mission.\n     - ***Venus***: Collections include data\
        \ from NASA's Magellan mission, MESSENGER mission's Venus data, and ESA's\
        \ Venus Express mission.\n\n3. **Items or Datacubes in Collections**:\n  \
        \ - Each collection contains items, referred to as objects or datacubes. These\
        \ items are specific observations or data products available within each mission's\
        \ dataset.\n   - Users can perform searches to locate these items using ODE's\
        \ faceted product search and interactive map-based search interface.\n\n4.\
        \ **Access and Download**:\n   - All data products within the collections\
        \ are freely available for download. Users can download individual data files\
        \ directly from observation detail pages or use a convenient user cart feature\
        \ to download multiple data products at one time.\n\n5. **Contact for Queries**:\n\
        \   - For questions related to ODE, users can reach out via the email address:\
        \ ode@wunder.wustl.edu. \n\nBy using this structure, you can effectively categorize\
        \ and access the data within ODE as a STAC catalog, where each mission or\
        \ planetary body represents a collection and each data product is an item\
        \ within those collections."
      prompt: ':::context_prompt :::extraction_prompt PDS Geosciences Node Orbital
        Data Explorer (ODE) + NASA Homepage + NASA en Espaol + Contact NASA HOME DATA
        AND SERVICES TOOLS ABOUT US CONTACT US SITE MAP Welcome to the Orbital Data
        Explorer The PDS Geosciences Node Orbital Data Explorer (ODE) website is a
        cross-mission and instrument query, search, display, and download tool for
        locating and retrieving PDS orbital science data archives of Mars , Mercury
        , Venus , and the Moon . ODE provides a faceted product search and an interactive
        map-based search interface for finding desired orbital observations. A convenient
        user cart feature allows multiple PDS data products to be downloaded at one
        time. Individual data files may be downloaded directly from observation detail
        pages, as well. All data products are freely available. Questions can be directed
        to ode@wunder.wustl.edu . Orbital Data Explorer Targets: Mars Orbital Data
        Explorer The Mars Orbital Data Explorer (ODE) provides search, display, and
        download tools for selected PDS science data archives of the Mars Reconnaissance
        Orbiter (MRO), the 2001 Mars Odyssey, the Mars Global Surveyor (MGS), the
        Viking Orbiter 1 and 2, and the European Space Agency''s Mars Express and
        ExoMars Trace Gas Orbiter missions. Supported Missions and Instruments: Mars
        Reconnaissance Orbiter (MRO): CRISM, CTX, Gravity/Radio Science, HiRISE, MCS,
        SHARAD ESA''s ExoMars Trace Gas Orbiter: ACS, CASSIS, NOMAD ESA''s Mars Express:
        HRSC, MARSIS, OMEGA, PFS, VMC 2001 Mars Odyssey: GRS, THEMIS Mars Global Surveyor:
        MOC, MOLA, TES Viking Orbiter 1 and 2: VISAB Lunar Orbital Data Explorer The
        Lunar Orbital Data Explorer (ODE) provides search, display, and download tools
        for the PDS science data archives of the Lunar Reconnaissance Orbiter (LRO),
        the Gravity Recovery and Interior Laboratory:(GRAIL), the Clementine, the
        Lunar Prospector, the Lunar Orbiter, the Japan Aerospace Exploration Agency''s
        SELENE mission, and the Indian Space Research Organisation''s Chandrayaan-1
        missions. Supported Missions and Instruments: Lunar Reconnaissance Orbiter
        (LRO): DLRE, LAMP, LEND, LOLA, LROC, MRFLRO ISRO''s Chandrayaan-1: M3, Mini-RF
        JAXA''s SELENE: ARD, GRS, HDTV, LALT, LMAG, LRS, MI, PACE, RSAT/VRAD, TC,
        UPI Gravity Recovery and Interior Laboratory (GRAIL): LGRS Clementine: HIRES,
        LIDAR, LWIR, NIR, RSS, UVVIS Lunar Prospector: ER, GRS, MAG, NS, RSS Lunar
        Orbiter: 24 Inch Focal Length Camera, 80mm Focal Length Camera Mercury Orbital
        Data Explorer The Mercury Orbital Data Explorer (ODE) provides search, display,
        and download tools for the PDS science data archives of the MESSENGER (Mercury
        Surface, Space Environment, Geochemistry, and Ranging) mission. Supported
        Missions and Instruments: MESSENGER: GRS, MASCS, MDIS-NAC, MDIS-WAC, MLA,
        NS, RSS, and XRS Venus Orbital Data Explorer The Venus Orbital Data Explorer
        (ODE) provides search, display, and download tools for the PDS science data
        archives of the Magellan mission, the MESSENGER mission''s Venus data, and
        ESA''s Venus Express mission. Supported Missions and Instruments: Magellan:
        RDRS, RSS MESSENGER (Venus Data): GRS, MASCS, MDIS-NAC, MDIS-WAC, MLA, NS,
        RSS, and XRS ESA''s Venus Express: MAG, VIRTIS + Freedom of Information Act
        + NASA Privacy Statement, Disclaimer, and Accessibility Certification + Copyright/Image
        Use Policy Curator: Jennifer Ward NASA Official: Paul Byrne Last Updated:
        + Comments and Questions 1

        '
      url: https://ode.rsl.wustl.edu/
    extraction_003:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To access the Orbital Data Explorer (ODE) using STAC terminology, consider
        the following relevant information extracted from the provided text:


        1. **Catalog**: The entire Mars Orbital Data Explorer (ODE) can be viewed
        as a catalog containing various datasets related to Mars missions.


        2. **Collections**: Each separate dataset within ODE acts as a collection.
        These datasets are associated with missions and instruments, such as the Mars
        Reconnaissance Orbiter (MRO), the 2001 Mars Odyssey, the Mars Global Surveyor,
        the Viking Orbiter 1 and 2, and the European Space Agency''s Mars Express
        and ExoMars Trace Gas Orbiter missions.


        3. **Items (Objects/Datacubes)**: The items within each collection can be
        thought of as objects or datacubes. These items are the individual orbital
        science products that can be searched for and accessed based on parameters
        like time, location, and product IDs.


        4. **Access Tools**: The ODE provides search, display, and download tools
        for these data archives. Searching can be conducted across missions, instruments,
        and datasets.


        5. **Additional Resources**: Users may access help resources or additional
        tools provided by ODE, such as the Data Product Search, Data Set Browser,
        and Download Cart for managing and obtaining desired datasets.


        This structure aligns with the STAC (SpatioTemporal Asset Catalog) model,
        where hierarchies are typically catalog, collections, and items.'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Home Page You are an anonymous user. Sign in Create a free account Read account
        help Your cart contents Your cart is empty. Show cart Home Data Product Search
        Map Search Tools Data Set Browser Download Help & Resources Welcome to The
        Mars Orbital Data Explorer The PDS Geosciences Node Mars Orbital Data Explorer
        (ODE) provides search, display, and download tools for the PDS science data
        archives and other data sets from the Mars Reconnaissance Orbiter (MRO), the
        2001 Mars Odyssey, the Mars Global Surveyor, the Viking Orbiter 1 and 2, and
        the European Space Agency''s Mars Express and ExoMars Trace Gas Orbiter missions.
        Choose one of the above tabs to start using ODE. JavaScript must be enabled
        for the ODE website to function properly Browser Frames must be enabled for
        the ODE website to function properly Important Note: ODE has detected that
        JavaScript is not currently enabled in your browser. Please enable JavaScript
        to allow the website to function properly. Data Product Search Search for
        orbital science products across missions, instruments, and data sets via time,
        location, and product ids. What''s New See what''s new with ODE Additional
        Tools MRO Coordinated Observations MOLA PEDR Query Product Type Coverage Help
        & Resources Access the ODE help, find additional resources, and see what''s
        coming Data Set Browser Browse through the orbital data set files stored in
        the PDS archives Available Data Sets A full list of mission, instrument, and
        product types available in Mars ODE Download Cart Download products added
        to the cart from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE
        The Mars Orbital Data Explorer is produced by the PDS Geosciences Node at
        Washington University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mars/
    extraction_004:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_account_acctCreate_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'The text provides the following information relevant to the objective
        of accessing the Orbital Data Explorer (ODE) using STAC terminology:


        1. **Catalog**: The Orbital Data Explorer (ODE) is considered the catalog.


        2. **Collections**: In the context of ODE, each separate dataset is regarded
        as a collection.


        3. **Items**: Within these collections, the items are referred to as objects
        or datacubes.


        4. **Access**: Access to the data is available at no charge, and a user may
        create an account for additional features like tracking search history, bookmarking
        searches and individual observations, and reviewing cart history.


        5. **User Interaction**: Users can optionally login, which enhances the ability
        to manage personal data interactions with the ODE.


        6. **Support**: For any problems or assistance, users can contact support
        at the provided email (ode@wunder.wustl.edu).


        7. **Account Creation Requirements**: To create an account, users must provide
        a valid email address and create a password (8 to 32 characters long, using
        specific allowed characters).


        This framework sets the groundwork for interacting with the ODE as a STAC-compliant
        resource library.'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Home Page {1} ##LOC[OK]## {1} ##LOC[OK]## ##LOC[Cancel]## {1} ##LOC[OK]##
        ##LOC[Cancel]## You are an anonymous user. Sign in Create an account Read
        account help Your cart contents Your cart is empty. Show cart Welcome to the
        Orbital Data Explorer. All data are available at no charge. We offer a new
        optional login, which allows users to track search history, bookmark searches
        and individual observations (PDS, ESA, and JAXA products), and review cart
        history. More information can be found in the ODE help. To report problems
        or request assistance, contact us at ode@wunder.wustl.edu Create Account Email
        address* Enter valid email address first. Password* Password must be 8 to
        32 characters long. You can use letters, numbers, and these symbols: ! @ #
        $ % ^ & * ? _ ~ - ( ) [ ] { } + = | ; : < > . / Remember my email address
        in this browser BotDetect CAPTCHA ASP.NET Form Validation Create account Important
        Note: ODE has detected that JavaScript is not currently enabled in your browser.
        Please enable JavaScript to allow the website to function properly.

        '
      url: https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx
    extraction_005:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_account_login_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "The relevant information for accessing the Orbital Data Explorer (ODE)\
        \ using STAC terminology is as follows:\n\n1. **Catalog Identification**:\
        \ ODE is considered a catalog within the STAC framework.\n\n2. **Collection\
        \ Definition**: Each separate dataset within ODE is regarded as a collection.\
        \ These collections contain items.\n\n3. **Item Description**: The items within\
        \ a collection are referred to as objects or datacubes.\n\nAdditional details\
        \ about accessing and using the ODE include:\n\n- **Access Requirements**:\
        \ All data in ODE are available without charge.\n  \n- **Account Benefits**:\
        \ Creating an account provides additional features such as tracking search\
        \ history, bookmarking searches and individual observations, and reviewing\
        \ cart history. This can be useful for managing interactions with the dataset\
        \ collections and items.\n\n- **Technical Requirement**: JavaScript must be\
        \ enabled in your browser for the ODE website to function correctly.\n\n-\
        \ **Contact Information**: For assistance, you can contact the support team\
        \ at ode@wunder.wustl.edu. \n\nThese elements are crucial for understanding\
        \ how to navigate and utilize the ODE as a STAC-based catalog."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Home Page {1} ##LOC[OK]## {1} ##LOC[OK]## ##LOC[Cancel]## {1} ##LOC[OK]##
        ##LOC[Cancel]## You are an anonymous user. Sign in Create an account Read
        account help Your cart contents Your cart is empty. Show cart Welcome to the
        Orbital Data Explorer. All data are available at no charge. We offer a new
        optional login, which allows users to track search history, bookmark searches
        and individual observations (PDS, ESA, and JAXA products), and review cart
        history. More information can be found in the ODE help. To report problems
        or request assistance, contact us at ode@wunder.wustl.edu Log In Email Need
        an account? Sign up Enter valid email address first. Password Remember my
        email address in this browser Sign in Forgot password Important Note: ODE
        has detected that JavaScript is not currently enabled in your browser. Please
        enable JavaScript to allow the website to function properly.

        '
      url: https://ode.rsl.wustl.edu/mars/account/login.aspx
    extraction_006:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_download.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of accessing the Orbital Data Explorer (ODE)\
        \ using STAC terminology, consider the following key points extracted from\
        \ the text:\n\n1. **Catalog**: The ODE itself is viewed as a catalog in STAC\
        \ terminology.\n\n2. **Collections**: Each separate dataset within the ODE\
        \ is considered a collection. \n\n3. **Items**: The items within each collection\
        \ are referred to as objects or datacubes.\n\n4. **Identification**: You are\
        \ accessing the ODE as an anonymous user, although there is an option to sign\
        \ in or create a free account for more functionalities.\n\n5. **Access Methods**:\
        \ The ODE provides several ways to search and interact with the data:\n  \
        \ - **Data Product Search**: Presumably allows searching through the collections\
        \ and items.\n   - **Map Search**: Likely provides a geographical interface\
        \ for exploring collections and items.\n   - **Data Set Browser**: Potentially\
        \ offers a way to browse through available datasets systematically.\n\n6.\
        \ **Tools & Resources**: Additional tools and resources are presumably available\
        \ to assist in accessing and managing data from the ODE.\n\nFor fully utilizing\
        \ the ODE in line with STAC terminology, one would typically need to:\n- Determine\
        \ the specific collections of interest within the ODE catalog.\n- Identify\
        \ and access the items/datacubes within those collections using the provided\
        \ search and access tools.\n- Optionally create an account for enhanced access\
        \ and features."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Download You are an anonymous user. Sign in Create a free account Read account
        help Your cart contents Your cart is empty. Show cart Home Data Product Search
        Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/download
    extraction_007:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_index_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To access the Mars Orbital Data Explorer (ODE) using SpatioTemporal\
        \ Asset Catalog (STAC) terminology, consider the following relevant information\
        \ extracted from the text:\n\n1. **ODE as a Catalog**: The Mars Orbital Data\
        \ Explorer is treated as a catalog in STAC terminology.\n\n2. **Collections\
        \ in ODE**: Each separate dataset in ODE is considered a collection. These\
        \ datasets are derived from various Mars missions and instruments, specifically:\n\
        \   - Mars Reconnaissance Orbiter (MRO)\n   - 2001 Mars Odyssey\n   - Mars\
        \ Global Surveyor\n   - Viking Orbiter 1 and 2\n   - European Space Agency's\
        \ Mars Express\n   - ExoMars Trace Gas Orbiter missions\n\n3. **Items or Objects\
        \ (Datacubes)**: Within each collection, the individual items are referred\
        \ to as objects or datacubes. These items can be searched and accessed via:\n\
        \   - Time\n   - Location\n   - Product IDs\n   \n4. **Accessing ODE**: To\
        \ begin using ODE, you can perform actions such as:\n   - Data Product Search:\
        \ Search for orbital science products using various filters like mission,\
        \ instrument, and data set.\n   - Data Set Browser: Browse through the available\
        \ orbital data set files stored in the PDS archives.\n   - Download Cart:\
        \ Download products that have been added to the cart from the product search.\n\
        \n5. **Additional Resources and Tools**: \n   - MRO Coordinated Observations\n\
        \   - MOLA PEDR Query\n   - Product Type Coverage\n\n6. **Help and Support**:\
        \ The ODE provides access to help resources and additional support via email\
        \ (ode@wunder.wustl.edu) for comments and questions.\n\nBy aligning your objective\
        \ with these extracted details, you can utilize the ODE effectively within\
        \ the STAC framework."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Home Page You are an anonymous user. Sign in Create a free account Read account
        help Your cart contents Your cart is empty. Show cart Home Data Product Search
        Map Search Tools Data Set Browser Download Help & Resources Welcome to The
        Mars Orbital Data Explorer The PDS Geosciences Node Mars Orbital Data Explorer
        (ODE) provides search, display, and download tools for the PDS science data
        archives and other data sets from the Mars Reconnaissance Orbiter (MRO), the
        2001 Mars Odyssey, the Mars Global Surveyor, the Viking Orbiter 1 and 2, and
        the European Space Agency''s Mars Express and ExoMars Trace Gas Orbiter missions.
        Choose one of the above tabs to start using ODE. JavaScript must be enabled
        for the ODE website to function properly Browser Frames must be enabled for
        the ODE website to function properly Important Note: ODE has detected that
        JavaScript is not currently enabled in your browser. Please enable JavaScript
        to allow the website to function properly. Data Product Search Search for
        orbital science products across missions, instruments, and data sets via time,
        location, and product ids. What''s New See what''s new with ODE Additional
        Tools MRO Coordinated Observations MOLA PEDR Query Product Type Coverage Help
        & Resources Access the ODE help, find additional resources, and see what''s
        coming Data Set Browser Browse through the orbital data set files stored in
        the PDS archives Available Data Sets A full list of mission, instrument, and
        product types available in Mars ODE Download Cart Download products added
        to the cart from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE
        The Mars Orbital Data Explorer is produced by the PDS Geosciences Node at
        Washington University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mars/index.aspx
    extraction_008:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_indexProductSearch_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To access the Orbital Data Explorer (ODE) using STAC terminology, consider
        the following structure:


        1. **Catalog**: The Orbital Data Explorer (ODE) serves as the catalog.


        2. **Collections**: Each separate dataset within the ODE is considered a collection.
        These collections contain various scientific data relevant to Mars exploration.


        3. **Items (Objects or Datacubes)**: Within each collection, the specific
        data products or datasets are treated as items. These items can be thought
        of as objects or datacubes that users can query, analyze, and download.


        This structure allows users to navigate the ODE similar to a STAC-based system,
        facilitating easier access and management of spatial and temporal data products
        related to Mars orbital missions.'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Product Search You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx
    extraction_009:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_mapsearch.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, you should treat the ODE as a catalog. Each dataset
        within ODE should be considered as a collection, and the individual items
        within these datasets are referred to as objects or datacubes.


        Here''s the relevant information extracted from the provided text:


        1. ODE is accessed as a catalog.

        2. Each dataset within ODE is a collection.

        3. Items within these datasets are called objects or datacubes.


        This setup allows you to navigate and retrieve data from ODE using the STAC
        framework, facilitating search and access to Mars data.'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Map Search You are an anonymous user. Sign in Create a free account Read account
        help Your cart contents Your cart is empty. Show cart Home Data Product Search
        Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/mapsearch
    extraction_010:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_pagehelp_Content_Introduction_Introduction_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of accessing the Orbital Data Explorer (ODE)\
        \ using STAC terminology, the following information is relevant:\n\n1. **Catalog**:\
        \ ODE is considered as the catalog in the STAC framework.\n\n2. **Collections**:\
        \ Each separate dataset within ODE represents a collection. Examples of these\
        \ datasets include:\n   - Mars ODE (containing data from missions like Mars\
        \ Reconnaissance Orbiter, Mars Express, Mars Odyssey, Mars Global Surveyor,\
        \ and Viking Orbiter)\n   - Mercury ODE (containing data from the MESSENGER\
        \ spacecraft)\n   - Lunar ODE (containing data from Clementine, Lunar Prospector,\
        \ Lunar Reconnaissance Orbiter, Chandrayaan-1, and Lunar Orbiter)\n   - Venus\
        \ ODE (containing data from the Magellan and MESSENGER spacecraft)\n\n3. **Items\
        \ (Objects or Datacubes)**: Within each collection, the items are referred\
        \ to as objects or datacubes. These items are the specific products that users\
        \ can find, review, and download.\n\n4. **Functionality**: ODE provides tools\
        \ for advanced search, retrieval, and ordering of PDS (Planetary Data System)-compliant\
        \ archives. It includes integrated analysis and visualization tools, allowing\
        \ easy access to specific products.\n\n5. **Data Handling**: ODE uses a central\
        \ database to store metadata, not the actual content, loaded from local and\
        \ remote nodes. The data process involves searching and selecting desired\
        \ products for downloading without altering the PDS archives."
      prompt: ':::context_prompt :::extraction_prompt ODE Introduction Skip To Main
        Content Account Settings Logout placeholder Account Settings Logout Filter:
        All Files Submit Search Introduction NASAs Planetary Data System (PDS) Geosciences
        Node s Orbital Data Explorer (ODE) provides map and forms-based search, retrieve,
        and order function for PDS-compliant archives from a variety of spacecraft
        instrument observations. Mars ODE includes observations from Mars Reconnaissance
        Orbiter (MRO), the European Space Agencys Mars Express (MEX), Mars Odyssey,
        the Mars Global Surveyor (MGS), and the Viking Orbiter (VO) spacecraft. The
        MRO mission is characterized by very high data volumes and complex observation
        plans relative to previous planetary missions. Mercury ODE includes observations
        from the MESSENGER (Mercury Surface, Space Environment, Geochemistry and Ranging)
        spacecraft. Lunar ODE includes observations from the Clementine, Lunar Prospector,
        the Lunar Reconnaissance Orbiter (LRO), and ISRO''s Chandrayaan-1, and Lunar
        Orbiter (LO) spacecraft . Venus ODE includes data from the Magellan and MESSENGER
        spacecraft. ODE is designed to augment the existing PDS search and retrieval
        interface by providing advanced search, retrieve, and order tools, integrated
        analysis tools, and visualization tools. ODE provides a way to store, query,
        retrieve, and order PDS archive data at the product level. In general, ODE
        has a back-end process that loads PDS archive data from local and remote nodes
        into a central database. This database is then used to allow the user to find,
        review, and download specific products. ODE does not change PDS archives nor,
        in most cases, stores the actual product contents. Rather it is a tool for
        finding, exploring, selecting, and downloading these products.

        '
      url: https://ode.rsl.wustl.edu/mars/pagehelp/Content/Introduction/Introduction.htm
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
      output:
        https://github.com/samiriff/mars-ode-data-access: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/: text/html
        https://ode.rsl.wustl.edu/mars/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/login.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/mars/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/mars/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/index.aspx: text/html
        https://ode.rsl.wustl.edu/mercury/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/mercury/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/forgot_password.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/moon/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_14_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_25_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_11_28_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_31_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_6_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_15_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_9_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_6_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_15_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_1_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_10_19_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_10_19_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_10_5_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_11_16_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_11_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_20_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_10_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_16_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_2_2_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_17_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_26_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_10_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_23_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_7_21_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_8_19_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_10_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_14_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_15_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_19_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_14_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_15_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_20_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_1_25_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_4_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_1_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_22_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_5_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_5_4_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_5_5_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_6_3_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_7_25_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_10_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_9_7_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_26_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_4_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_5_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_4_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_11_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_19_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_13_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_17_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_7_2_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_8_29_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_24_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_26_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/index.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/oldholding.html: text/html
        https://ode.rsl.wustl.edu/venus/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/index.aspx: text/html
        https://ode.rsl.wustl.edu/venus/account/login.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/download: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/tools: text/html; charset=utf-8
        https://oderest.rsl.wustl.edu/: text/html
        https://pds-geosciences.wustl.edu/dataserv/default.htm: text/html
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2
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


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-cajjx2/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-cajjx2](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-cajjx2.tar.gz)

🔥

---

- [round 1](./round-1.md)
