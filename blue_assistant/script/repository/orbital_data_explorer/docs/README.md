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
      output: "The relevant information for writing Python code to access the Orbital\
        \ Data Explorer (ODE) using STAC terminology is derived from the repository\
        \ mentioned: `samiriff/mars-ode-data-access`. This repository serves as a\
        \ Python package that facilitates interaction with data from the Mars Orbital\
        \ Data Explorer via a REST service. Here's the key information extracted from\
        \ your text:\n\n1. **ODE as a Catalog**: The Orbital Data Explorer is treated\
        \ as a catalog in this context.\n\n2. **Dataset as Collections**: Each dataset\
        \ within the ODE is considered a separate collection.\n\n3. **Items**: Within\
        \ these collections, individual data items, such as high-resolution map-projected\
        \ JP2 images, can be accessed and processed.\n\n4. **Python Package**: \n\
        \   - The package is named `mars-ode-data-access` and is hosted on GitHub\
        \ under the repository `samiriff/mars-ode-data-access`.\n   - It aims to provide\
        \ an easy-to-use interface for accessing data from the ODE.\n\n5. **REST API\
        \ Interaction**: \n   - The interaction with ODE data is performed using the\
        \ ODE REST Service, where users can define queries to access specific datasets.\n\
        \n6. **Query Processing**:\n   - The `QueryProcessor` class is used to construct\
        \ and process user-defined queries for accessing ODE data.\n   - Supported\
        \ query parameters include target planetary body, mission, instrument, product\
        \ type, geographic coordinates, observation time, and more.\n\n7. **Result\
        \ Processing**:\n   - The `QueryResultProcessor` class processes results returned\
        \ by queries.\n   - It supports downloading data, chunking large images, and\
        \ handling image binning.\n\n8. **Image Processing Utilities**:\n   - Includes\
        \ utility methods for processing images, such as cropping black margins, slicing\
        \ images into chunks, and aligning/rotating images.\n\n9. **Sample Code Usage**:\n\
        \   - The main script `main.py` demonstrates how to use the package to formulate\
        \ a query and retrieve sample data from ODE.\n\n10. **Acknowledgements**:\
        \ Dependencies and acknowledgements include packages like scikit-image.\n\n\
        These points should provide a foundation for developing Python code that accesses\
        \ and manipulates ODE data using the STAC framework. Further exploration of\
        \ the `mars-ode-data-access` package and its functionalities is required to\
        \ fully implement your objective."
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
      output: "To write Python code that accesses the Orbital Data Explorer (ODE)\
        \ using SpatioTemporal Asset Catalog (STAC) terminology, let's extract the\
        \ relevant information from the provided text:\n\n### Overview\n- **Catalog**:\
        \ Consider the entire ODE as a catalog.\n- **Collections**: \n  - Each dataset\
        \ within the ODE is a collection.\n  - Collections exist for different celestial\
        \ bodies: Mars, Moon (Lunar), Mercury, and Venus.\n  \n### Collections and\
        \ Items\n- **Mars ODE Collection**: Includes items from missions such as Mars\
        \ Reconnaissance Orbiter (MRO), Mars Express, ExoMars Trace Gas Orbiter, etc.\
        \ Instruments include CRISM, CTX, HiRISE, etc.\n- **Lunar ODE Collection**:\
        \ Includes items from missions like Lunar Reconnaissance Orbiter (LRO), GRAIL,\
        \ Chandrayaan-1, etc. Instruments include DLRE, LROC, LAMP, etc.\n- **Mercury\
        \ ODE Collection**: Contains items from the MESSENGER mission with instruments\
        \ like GRS, MASCS, MDIS-NAC, etc.\n- **Venus ODE Collection**: Includes data\
        \ from Magellan, MESSENGER (Venus data), and Venus Express missions. Instruments\
        \ include RDRS, VIRTIS, RSS, etc.\n\n### Access and Features\n- **Search and\
        \ Retrieval**: The ODE provides search, display, and download tools for accessing\
        \ PDS science data. \n- **User Features**: \n  - Faceted product search\n\
        \  - Interactive map-based search interface\n  - User cart for downloading\
        \ multiple products at once\n- **Access**: All data products are freely available\
        \ and can also be downloaded directly from observation detail pages.\n\n###\
        \ Contact Information\n- For questions related to ODE, users can contact the\
        \ provided email: ode@wunder.wustl.edu.\n\nUsing the described information,\
        \ you can design Python code to interact with this data structure, treating\
        \ ODE as a STAC catalog with collections (planetary datasets) and items (missions\
        \ and instruments data)."
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
      cache: extraction_cache/ode_rsl_wustl_edu_lunar.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To access the Orbital Data Explorer (ODE) using STAC (SpatioTemporal\
        \ Asset Catalog) terminology, we can think of the ODE as a catalog. Each specific\
        \ dataset within the ODE can be considered a collection, and the individual\
        \ items within these collections would correspond to the specific data products.\n\
        \nHere's a simplified breakdown of the relevant information that can be extracted\
        \ from the provided text:\n\n1. **Catalog**: \n   - ODE serves as a catalog\
        \ for lunar, and potentially other planetary, orbital data.\n\n2. **Collections**:\n\
        \   - Each dataset from different lunar missions, such as the Lunar Reconnaissance\
        \ Orbiter (LRO), the Gravity Recovery and Interior Laboratory (GRAIL), Clementine,\
        \ the Lunar Prospector, the Lunar Orbiter, and the Chandrayaan-1, can be considered\
        \ as a separate collection within the ODE catalog.\n\n3. **Items**:\n   -\
        \ Within each mission dataset (collection), there are data products which\
        \ can be considered as items. These items can be searched according to missions,\
        \ instruments, and data sets via parameters like time, location, and product\
        \ IDs.\n\n4. **Data Access and Tools**:\n   - Users can search, display, and\
        \ download the available data using the ODE website tools such as \"Data Product\
        \ Search\" and \"Data Set Browser.\"\n   - The ODE platform also provides\
        \ additional tools like LOLA RDR Query and DIVINER RDR Query for specific\
        \ data interrogation.\n\n5. **Download Mechanisms**:\n   - Users can add desired\
        \ products to a cart and download them collectively, facilitating batch data\
        \ retrieval.\n\n6. **Technical Requirements**:\n   - JavaScript and browser\
        \ frames need to be enabled to use the ODE website effectively.\n\n7. **Additional\
        \ Features**:\n   - There are additional resources and help documentation\
        \ available for users to assist with utilizing the ODE platform.\n\nUnderstanding\
        \ these aspects will help in crafting Python code that can interface with\
        \ the ODE platform using STAC terminology to access and utilize lunar orbital\
        \ datasets programmatically."
      prompt: ':::context_prompt :::extraction_prompt Lunar Orbital Data Explorer
        - Home Page You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources Welcome
        to The Lunar Orbital Data Explorer The PDS Geosciences Node Lunar Orbital
        Data Explorer (ODE) provides search, display, and download tools for the PDS
        science data archives of the Lunar Reconnaissance Orbiter (LRO), the Gravity
        Recovery and Interior Laboratory (GRAIL), the Clementine, the Lunar Prospector,
        the Lunar Orbiter, and the Indian Space Research Organisation''s Chandrayaan-1
        missions to Earth''s moon. Choose one of the above tabs to start using ODE.
        JavaScript must be enabled for the ODE website to function properly Browser
        Frames must be enabled for the ODE website to function properly Important
        Note: ODE has detected that JavaScript is not currently enabled in your browser.
        Please enable JavaScript to allow the website to function properly. Data Product
        Search Search for orbital science products across missions, instruments, and
        data sets via time, location, and product ids. What''s New See what''s new
        with ODE Additional Tools LOLA RDR Query DIVINER RDR Query Product Type Coverage
        Help & Resources Access the ODE help, find additional resources, and see what''s
        coming Data Set Browser Browse through the orbital data set files stored in
        the PDS archives Available Data Sets A full list of mission, instrument, and
        product types available in Lunar ODE Download Cart Download products added
        to the cart from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE
        The Lunar Orbital Data Explorer is produced by the PDS Geosciences Node at
        Washington University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/lunar
    extraction_004:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_account_acctCreate_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code accessing the Orbital Data Explorer (ODE) using\
        \ STAC terminology, we need to structure our approach as follows:\n\n1. **Define\
        \ ODE as a Catalog:**\n   - In STAC terminology, a \"Catalog\" is a container\
        \ for one or more \"Collections.\" The ODE is treated as this main Catalog.\n\
        \n2. **Identify Datasets as Collections:**\n   - Each separate dataset within\
        \ ODE serves as a \"Collection.\" A Collection in STAC is a group of related\
        \ \"Items.\"\n\n3. **Dataset Items:**\n   - In each dataset/Collection, there\
        \ are individual data entries or assets, which are referred to as \"Items.\"\
        \n\n4. **Access and Features:**\n   - Users can track search history, bookmark\
        \ searches, and individual observations, which means interaction can consider\
        \ search/filter capabilities.\n   - Observations available include products\
        \ from PDS, ESA, and JAXA.\n   \n5. **Account and Authentication:**\n   -\
        \ While access is free, creating an account offers added benefits like tracking\
        \ and bookmarking, which may require authentication.\n   - Account creation\
        \ checks for valid emails and passwords (8-32 characters with specific allowed\
        \ symbols).\n\nIn summary, to access ODE as a catalog using STAC, each dataset\
        \ is a collection, and individual data entries are items. Python code will\
        \ involve forming requests to browse/search collections and items, potentially\
        \ using account features if advanced interaction is required."
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
      cache: extraction_cache/ode_rsl_wustl_edu_mars_help.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To write Python code to access the Orbital Data Explorer (ODE) using
        STAC terminology, you should understand the following key points from the
        text:


        1. **ODE as a Catalog**: Consider ODE as a catalog that organizes different
        datasets. In STAC terms, a catalog is a container or index of collections.


        2. **Collections**: Each dataset within ODE should be viewed as a collection.
        A collection in STAC is a group of related items, typically containing similar
        types of data.


        3. **Items**: Within each collection, there are items. In STAC, an item is
        an individual data entity or asset with metadata, such as a single image or
        data file.


        4. **Account System**: The text mentions creating an account and signing in.
        This could imply that to access data programmatically, you may potentially
        need authentication. Consider looking into API keys or login credentials if
        necessary.


        5. **Data Access**: The text talks about "Data Product Search," "Map Search,"
        and "Data Set Browser," indicating that ODE supports searching and browsing
        functionalities. These features might be accessible through an API, which
        you''ll need to explore for programmatic access.


        To proceed, you should investigate whether ODE provides a REST API or another
        interface conforming to the STAC (SpatioTemporal Asset Catalog) specification.
        This could involve reviewing ODE''s official documentation or contacting their
        support for further guidance on programmatic data access methods.


        Additionally, familiarize yourself with the basic structure and concepts of
        STAC such as catalogs, collections, items, and how they are accessed via APIs.
        Libraries such as `pystac` might be useful for handling STAC data in Python.'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Help and Resources You are an anonymous user. Sign in Create a free account
        Read account help Your cart contents Your cart is empty. Show cart Home Data
        Product Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/help
    extraction_006:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_index_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "The text provides an overview of the Mars Orbital Data Explorer (ODE)\
        \ and outlines the functionality available on its website. To achieve the\
        \ objective of accessing ODE using STAC terminology, key elements to consider\
        \ include:\n\n1. **Catalog**: The Mars Orbital Data Explorer itself can be\
        \ considered a catalog, which serves as the entry point to all the data collections.\n\
        \n2. **Collections**: Each separate dataset in ODE can be seen as a collection.\
        \ These collections are grouped by missions (e.g., Mars Reconnaissance Orbiter,\
        \ 2001 Mars Odyssey, Mars Global Surveyor), instruments, and data sets.\n\n\
        3. **Items**: An Item in STAC terms would correspond to individual data products\
        \ or files within these collections. These can be searched based on parameters\
        \ like time, location, and product IDs.\n\n4. **Functionality for ODE Access**:\n\
        \   - Use the **Data Product Search** to find and filter items across different\
        \ collections using criteria such as time, location, and product IDs.\n  \
        \ - Use the **Data Set Browser** to navigate through available collections\
        \ and their respective items stored in the PDS archives.\n\n5. **Additional\
        \ Features**:\n   - **Download Cart**: Users can add items to a download cart\
        \ for batch downloading.\n   - **Help & Resources**: Provides access to additional\
        \ information and resources, which can be valuable for understanding the datasets\
        \ and how to work with the data.\n\nBy representing ODE with these STAC concepts,\
        \ you can create a hierarchical structure where the catalog contains multiple\
        \ collections, each of which contains items of data, allowing for structured\
        \ and efficient access to the data available in ODE."
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
    extraction_007:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_indexProductSearch_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of accessing the Orbital Data Explorer (ODE)\
        \ using STAC (SpatioTemporal Asset Catalog) terminology, you can extract the\
        \ following relevant information from the provided text:\n\n1. **Catalog**:\
        \ The ODE is considered the main catalog. In STAC, a catalog is the central\
        \ place that maintains a structure to access collections and items.\n\n2.\
        \ **Collections**: In the context of ODE, each separate dataset available\
        \ is treated as a collection. A collection in STAC represents a grouping of\
        \ related items.\n\n3. **Items**: Within each collection (dataset), there\
        \ are items. Items in STAC are the core entity and contain metadata about\
        \ a unique spatiotemporal asset or dataset granule.\n\n4. **Access Points**:\
        \ \n   - The text mentions \"Data Product Search\" and \"Map Search\", which\
        \ suggests there are tools available to find and access data products within\
        \ ODE. These can be considered functionalities for accessing collections or\
        \ items within the catalog.\n   - There are also references to tools like\
        \ \"Data Set Browser\" and \"Download\", which might be used to interact with\
        \ or retrieve specific items or collections from the ODE.\n\nFor a Python\
        \ implementation, you would likely need to interact with ODE's API (if available)\
        \ or web interface to navigate the catalog, query collections, and access\
        \ the items using the searches and tools mentioned."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Product Search You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx
    extraction_008:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_pagehelp_Content_Web_Interface_User_Account_creating_account_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To access the Orbital Data Explorer (ODE) using STAC terminology, you\
        \ would structure your approach as follows:\n\n1. **Catalog**: The ODE itself\
        \ serves as the catalog.\n\n2. **Collections**: Each dataset within ODE corresponds\
        \ to a collection.\n\n3. **Items**: Within each collection, there are items\
        \ that represent individual entries or data points.\n\nIn terms of implementing\
        \ this in Python:\n\n- You would need to interact with the ODE platform to\
        \ retrieve information about the collections and their items.\n- Using an\
        \ API, if available, would likely be the most direct method. If not, web scraping\
        \ techniques may be required.\n- To interact programmatically, it might be\
        \ necessary to create an account on ODE for access to additional features,\
        \ like bookmarking or personalizing searches.\n\nHere is a general outline\
        \ of steps you might follow in the code:\n\n```python\nimport requests\n\n\
        # Base URL for ODE api\nbase_url = \"https://ode.api.url\"  # Hypothetical\
        \ URL\n\ndef list_collections():\n    # Function to list all collections in\
        \ ODE\n    response = requests.get(f\"{base_url}/collections\")\n    collections\
        \ = response.json()\n    return collections\n\ndef get_items(collection_id):\n\
        \    # Function to get items in a specific collection\n    response = requests.get(f\"\
        {base_url}/collections/{collection_id}/items\")\n    items = response.json()\n\
        \    return items\n\n# Example Usage:\ncollections = list_collections()\n\
        for collection in collections:\n    print(f\"Collection: {collection['id']}\"\
        )\n    items = get_items(collection['id'])\n    for item in items:\n     \
        \   print(f\"- Item ID: {item['id']}\")\n```\n\nNote:\n- Replace `https://ode.api.url`\
        \ with the actual API endpoint for the Orbital Data Explorer.\n- Consider\
        \ handling authentication or session management if required by the ODE for\
        \ accessing data. Creating an account may provide necessary credentials or\
        \ tokens for authenticating API requests."
      prompt: ':::context_prompt :::extraction_prompt Creating An Account Skip To
        Main Content Account Settings Logout placeholder Account Settings Logout Filter:
        All Files Submit Search Creating An Account Creating an account is quick and
        simple! At the top of the ODE banner, an icon exists that shows that the user
        is not logged in. Clicking on that icon will confirm you are an anonymous
        user and provide options for sign in, creating an account or this help. Here
        is the menu displayed to anonymous users: Click on the "Create an account"
        link, which directs the browser to a page for creating the account. Enter
        your preferred email address, password, and the displayed "CAPTCHA" text.
        If it is not legible, click the refresh button to the right of the captcha.
        Sometimes the "CAPTCHA" text can be difficult to read. After populating these
        fields, click the "Create account" button. Upon successful creation of the
        account, a confirmation message will be displayed and a corresponding email
        will be sent. That''s it! Now upon navigating to other pages of the website,
        you will see the logged in menu is populated. In addition, the option to bookmark
        product detail pages and search result lists will be provided.

        '
      url: https://ode.rsl.wustl.edu/mars/pagehelp/Content/Web_Interface/User_Account/creating_account.htm
    extraction_009:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_productsearch.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code to access the Orbital Data Explorer (ODE) using\
        \ the SpatioTemporal Asset Catalog (STAC) terminology, you need to understand\
        \ the structure ODE uses and how it maps to STAC concepts. Here's how you\
        \ can extract the relevant information based on the description provided:\n\
        \n1. **ODE as a Catalog**:\n   - Catalog: In STAC, a catalog is a container\
        \ for collections and items. In this scenario, the entire ODE acts as the\
        \ catalog, which you will be interacting with in your Python code.\n\n2. **Datasets\
        \ as Collections**:\n   - Collection: Each dataset within ODE functions as\
        \ a separate STAC collection. Collections contain metadata common to all the\
        \ items in the dataset, such as the dataset's name, description, and spatial\
        \ and temporal extent.\n\n3. **Data Products as Items**:\n   - Item: In STAC,\
        \ an item represents an individual, identifiable asset. In the context of\
        \ ODE, these would correspond to individual data products within a dataset.\
        \ Each item will have specific metadata attributes like acquisition time,\
        \ location, product ID, etc.\n\n4. **Elements to Access**:\n   - Data Product\
        \ Search: This feature is likely used to navigate or query items within a\
        \ collection (dataset).\n   - Data Set Browser: This may allow browsing through\
        \ available collections (datasets).\n\n5. **Implementation Steps**:\n   -\
        \ Authenticate: Consider whether authentication is required; if so, implement\
        \ a mechanism to manage user authentication.\n   - Query: Use a STAC Client\
        \ library or HTTP methods to interact with the ODE system and query the required\
        \ collections or items.\n   - Parse Results: Parse the returned datasets and\
        \ items according to STAC JSON structure.\n   - Download: Use the \"Download\"\
        \ functionality mentioned to retrieve specific data items.\n\n6. **Additional\
        \ Resources**:\n   - Utilize available \"Help & Resources\" to understand\
        \ ODE's API endpoints or data retrieval methods better.\n   - Consider using\
        \ the \"Tools\" or \"Map Search\" for enhanced data interaction if applicable.\n\
        \nBy structuring your Python code around these STAC elements, you'll be able\
        \ to effectively access and retrieve data from ODE, treating it as a catalog\
        \ of collections and items."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Product Search You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/productsearch
    extraction_010:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_moon_account_login_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "Based on the provided text, here is the information relevant to accessing\
        \ the Orbital Data Explorer (ODE) using STAC (SpatioTemporal Asset Catalog)\
        \ terminology:\n\n1. **Catalog**:\n   - ODE serves as the Catalog. It is the\
        \ overarching system that contains various datasets related to orbital data.\n\
        \n2. **Collections**:\n   - Each separate dataset within the ODE is considered\
        \ a Collection. These collections would include various datasets from PDS\
        \ (Planetary Data System), ESA (European Space Agency), and JAXA (Japan Aerospace\
        \ Exploration Agency).\n\n3. **Items**:\n   - Each Collection contains Items.\
        \ These items represent individual observations or data entries within a dataset\
        \ and can be bookmarked or added to a user's cart.\n\nThe Python code to interact\
        \ with ODE, in terms of STAC, would first focus on accessing the Catalog,\
        \ identifying and retrieving the Collections, and then managing the individual\
        \ Items within those Collections."
      prompt: ':::context_prompt :::extraction_prompt Lunar Orbital Data Explorer
        - Home Page {1} ##LOC[OK]## {1} ##LOC[OK]## ##LOC[Cancel]## {1} ##LOC[OK]##
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
      url: https://ode.rsl.wustl.edu/moon/account/login.aspx
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
        https://ode.rsl.wustl.edu/account/acctCreate.aspx: unknown
        https://ode.rsl.wustl.edu/datasets: unknown
        https://ode.rsl.wustl.edu/download: unknown
        https://ode.rsl.wustl.edu/help: unknown
        https://ode.rsl.wustl.edu/lunar: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mars/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/mars/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/account/login.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Introduction/Introduction.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/bookmark_list.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/forgot_password.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/history_list.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/past_ode_cart_orders.htm: text/html
        https://ode.rsl.wustl.edu/moon/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm: text/html
        https://ode.rsl.wustl.edu/moon/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_15_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_18_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_2_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_5_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_15_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_22_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_14_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_3_8_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_10_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_13_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_30_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_5_7_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_18_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_8_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_13_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_13_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_3_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_10_12_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_10_4_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_11_29_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_11_6_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_10_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_6_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_3_11_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_15_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_18_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_11_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_16_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_22_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_19_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_24_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_8_14_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_9_5_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_20_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_1_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_21_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_24_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_3_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_2_19_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_1_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_22_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_22_2021.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_11_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_6_18_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_5_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_9_1_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_12_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_17_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_10_4_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_22_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_30_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_1_2_2025.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_3_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_7_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_4_14_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_4_5_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_29_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_4_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_3_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_7_13_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_8_22_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/index.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/oldholding.html: text/html
        https://ode.rsl.wustl.edu/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: unknown
        https://ode.rsl.wustl.edu/productsearch: unknown
        https://ode.rsl.wustl.edu/tools: unknown
        https://ode.rsl.wustl.edu/venus/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/productsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/tools: text/html; charset=utf-8
        https://oderest.rsl.wustl.edu/: text/html
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2
    writing_code:
      action: generate_text
      completed: true
      depends-on: generating_summary
      runnable: false
  vars:
    context_prompt: "Our objective is to write Python code to access the Orbital Data\
      \ Explorer, ODE for short, \nusing STAC terminology. For this purpose, we consider\
      \ ODE as a catalog and each separate \ndataset in ODE as a collection that contains\
      \ items.\n"
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


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-4p0amd/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-4p0amd](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-4p0amd.tar.gz)

🔥

---

- [round 1](./round-1.md)
