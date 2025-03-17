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
      cache: extraction_cache/github_com_samiriff_mars-ode-data-access.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology\
        \ and the provided Python package, you can extract useful information from\
        \ the text as follows:\n\n### Key Steps and Components:\n\n1. **Initialize\
        \ Query Processor:**\n   - Use the `QueryProcessor` class to set up and execute\
        \ queries with various parameters like target, mission, instrument, etc.\n\
        \   - Example Code:\n     ```python\n     from ode_data_access.query_processor\
        \ import QueryProcessor\n\n     query_processor = QueryProcessor()\n     query_results\
        \ = query_processor.query_files_urls(\n         target='Mars', \n        \
        \ mission='MRO', \n         instrument='HIRISE', \n         product_type='DTM',\
        \ \n         western_lon=0, \n         eastern_lon=360, \n         min_lat=-90,\
        \ \n         max_lat=90, \n         min_ob_time='2017-03-01', \n         max_ob_time='2017-04-01',\
        \ \n         product_id='*', \n         file_name='*', \n         number_product_limit=100,\
        \ \n         result_offset_number=0\n     )\n     ```\n\n2. **Initialize Query\
        \ Result Processor:**\n   - Use `QueryResultProcessor` to handle the processing\
        \ and downloading of query results.\n   - Example Code:\n     ```python\n\
        \     from ode_data_access.query_result_processor import QueryResultProcessor\n\
        \n     query_result_processor = QueryResultProcessor()\n     should_continue\
        \ = query_result_processor.download(query_results, bin_type='Bin1', product_types={'PRODUCT\
        \ DATA FILE', 'BROWSE'})\n     if should_continue:\n         query_result_processor.process(\n\
        \             SAVE_DIR_PREFIX='output',\n             CHUNK_SIZE=1024,\n \
        \            SKIP_BLACK_IMAGES=True,\n             ALIGN_AND_CROP_THRESHOLDS={'max_border_size':\
        \ 10, 'safety_margin': 5, 'tolerance': 15},\n             vectorized_chunks=None\n\
        \         )\n     ```\n\n### Supported Query Parameters:\n- **target:** Planetary\
        \ body (e.g., Mars, Mercury)\n- **mission:** Space mission (e.g., MGS, MRO)\n\
        - **instrument:** Instrument used in the mission (e.g., HIRISE)\n- **product_type:**\
        \ Type of data product (e.g., DTM)\n- **western_lon/eastern_lon:** Longitude\
        \ range (0 to 360)\n- **min_lat/max_lat:** Latitude range (-90 to 90)\n- **min_ob_time/max_ob_time:**\
        \ Time range for observation (UTC format)\n- **product_id:** Product ID with\
        \ wildcard support\n- **file_name:** Filename with wildcard support\n- **number_product_limit:**\
        \ Limit on the number of returned products\n- **result_offset_number:** Offset\
        \ for products beyond the limit\n\n### Supported Query Result Parameters:\n\
        - **bin_type:** Binning type (e.g., Bin1, Bin2)\n- **product_types:** Set\
        \ of desired product types\n\n### Chunk Parameters:\n- **save_dir_prefix:**\
        \ Prefix for directories where image chunks will be saved\n- **chunk_size:**\
        \ Size of each chunk\n- **skip_black_images:** Flag to skip images with black\
        \ pixels at the center\n- **ALIGN_AND_CROP_THRESHOLDS:** Parameters for dealing\
        \ with black margins\n\nBy following these steps and using the necessary parameters,\
        \ you can effectively download and process data from the Mars ODE using the\
        \ `mars-ode-data-access` package in Python."
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
      output: "To download data from the Orbital Data Explorer (ODE) using STAC (SpatioTemporal\
        \ Asset Catalog) terminology, you can extract the following relevant information\
        \ from the provided text:\n\n1. **Target Planets and Missions**:\n   - Mars:\
        \ Mars Reconnaissance Orbiter (MRO), 2001 Mars Odyssey, Mars Global Surveyor\
        \ (MGS), Viking Orbiter 1 and 2, ESA's Mars Express, ExoMars Trace Gas Orbiter.\n\
        \   - Moon: Lunar Reconnaissance Orbiter (LRO), Gravity Recovery and Interior\
        \ Laboratory (GRAIL), Clementine, Lunar Prospector, Lunar Orbiter, JAXA's\
        \ SELENE, ISRO's Chandrayaan-1.\n   - Mercury: MESSENGER.\n   - Venus: Magellan,\
        \ MESSENGER (Venus data), ESA's Venus Express.\n\n2. **Available Instruments**:\n\
        \   - For each mission, specific instruments are listed such as CRISM, HiRISE,\
        \ SHARAD for Mars Reconnaissance Orbiter (MRO), or GRS, MASCS for MESSENGER.\n\
        \n3. **Functionalities of ODE**:\n   - Search, display, and download tools\
        \ are available for locating and retrieving data archives.\n   - Faceted product\
        \ search and interactive map-based search interface.\n   - User cart feature\
        \ for downloading multiple PDS data products at once or downloading individual\
        \ files from observation detail pages.\n\n4. **Access and Contact**:\n   -\
        \ All data products are freely available.\n   - For questions or support,\
        \ users can contact ode@wunder.wustl.edu.\n\n5. **STAC Integration**:\n  \
        \ - While the text doesn't mention STAC explicitly, the use of a \"faceted\
        \ product search\" and \"map-based search interface\" aligns with STAC's capabilities\
        \ for discovery and filtering of spatial and temporal data.\n   - ODE's reference\
        \ to \"observation detail pages\" can relate to STAC's items, providing metadata\
        \ and download links.\n\nWith this information, you can proceed to write Python\
        \ code that interacts with ODE, using their search functionalities and metadata\
        \ details that align with STAC's approach to cataloguing and retrieving data."
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
      output: "To write Python code to download data from the Orbital Data Explorer\
        \ (ODE) using STAC terminology, it's essential to extract the relevant information\
        \ regarding available data sets, browsing, searching, and downloading functionalities\
        \ from the given text. Here's a breakdown of the relevant information:\n\n\
        1. **Data Sets and Missions**:\n   - ODE provides access to data from several\
        \ lunar missions: \n     - Lunar Reconnaissance Orbiter (LRO)\n     - Gravity\
        \ Recovery and Interior Laboratory (GRAIL)\n     - Clementine\n     - Lunar\
        \ Prospector\n     - Lunar Orbiter\n     - Indian Space Research Organisation's\
        \ Chandrayaan-1\n\n2. **Features and Functionalities**:\n   - **Data Product\
        \ Search**: Allows you to search for orbital science products across different\
        \ missions, instruments, and data sets using criteria such as time, location,\
        \ and product IDs. This aligns with the STAC concept of searching for items\
        \ using specific properties and metadata.\n   - **Data Set Browser**: Enables\
        \ browsing through the available orbital data set files stored in the PDS\
        \ archives.\n   - **Download Cart**: Users can add products to a download\
        \ cart from the product search results and then download them. \n\n3. **Additional\
        \ Tools**:\n   - Additional tools like LOLA RDR Query and DIVINER RDR Query\
        \ for specific products.\n\n4. **Help and Resources**:\n   - Access to help\
        \ and resources for understanding and using the ODE, including potential future\
        \ updates.\n\n5. **Account Management**:\n   - Users have options to sign\
        \ in or create a free account, though it's unclear from the text whether downloading\
        \ data requires an account.\n\nFor implementing the code to interact with\
        \ ODE using Python, you might want to consider using libraries for HTTP requests\
        \ (such as `requests`) and possibly handling STAC metadata if a specific API\
        \ endpoint or metadata format is provided.\n\nHere is a potential approach\
        \ for writing code to interact with ODE:\n\n- **HTTP Requests**: Use the `requests`\
        \ library to interact with the ODE API (assuming an appropriate API endpoint\
        \ is provided by ODE documentation).\n- **Search and Filter**: Utilize search\
        \ parameters compatible with STAC, focusing on fields like missions, instruments,\
        \ and product types.\n- **Download**: Implement functionality to add items\
        \ to a download cart and retrieve them, if applicable.\n- **Error Handling**:\
        \ Ensure the code manages potential issues like connectivity or invalid search\
        \ parameters.\n\nTo proceed, you'll need to refer to any documentation provided\
        \ by ODE or the PDS Geosciences Node to understand specific API endpoints,\
        \ parameters, and response formats that align with STAC terminology."
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
      cache: extraction_cache/ode_rsl_wustl_edu_mercury.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To write Python code to download data from the Mercury Orbital Data
        Explorer (ODE) using STAC terminology, you need to extract the relevant information
        about how to search and download data. Based on the provided text, here are
        the key points that can help inform your code:


        1. **Data Access**: The ODE allows you to search for orbital science products
        across missions, instruments, and data sets using parameters like time, location,
        and product IDs. This means the API or search functionality might support
        querying using these parameters.


        2. **Data Download**: Products can be added to a "Download Cart" from the
        product search, suggesting that after identifying desired data, it can be
        programmatically added to a cart-like structure before initiating downloads.


        3. **JavaScript and Browser Requirements**: It mentions that JavaScript and
        browser frames need to be enabled for the ODE website to function properly.
        While this doesn''t directly affect a Python script, it implies that some
        advanced interaction or web scraping might require enabling these features
        if using a tool like Selenium for automated browsing.


        4. **Documentation and Help**: There are Help & Resources sections available,
        which might contain API documentation or further details on accessing and
        downloading data programmatically.


        5. **Contact Information**: For questions or further assistance, you can contact
        the support team via email at ode@wunder.wustl.edu. This can be useful if
        you encounter issues not covered in the available documentation.


        With these points in mind, you''ll need to investigate further to find specific
        API documentation or endpoints that allow for programmatic access, search,
        and download of data. Normally, this would be in the resources section, or
        by contacting support for API documentation.'
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Home Page You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources Welcome
        to The Mercury Orbital Data Explorer The PDS Geosciences Node Mercury Orbital
        Data Explorer (ODE) provides search, display, and download tools for the PDS
        science data archives of the Messenger mission. Choose one of the above tabs
        to start using ODE. JavaScript must be enabled for the ODE website to function
        properly Browser Frames must be enabled for the ODE website to function properly
        Important Note: ODE has detected that JavaScript is not currently enabled
        in your browser. Please enable JavaScript to allow the website to function
        properly. Data Product Search Search for orbital science products across missions,
        instruments, and data sets via time, location, and product ids. What''s New
        See what''s new with ODE Additional Tools Product Type Coverage Help & Resources
        Access the ODE help, find additional resources, and see what''s coming Data
        Set Browser Browse through the orbital data set files stored in the PDS archives
        Available Data Sets A full list of mission, instrument, and product types
        available in Mercury ODE Download Cart Download products added to the cart
        from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE The Mercury
        Orbital Data Explorer is produced by the PDS Geosciences Node at Washington
        University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mercury
    extraction_005:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_account_login_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology,\
        \ the following steps and information can be extracted and utilized from the\
        \ provided text:\n\n1. **Account Setup:**\n   - You can create a free account\
        \ to log in and access features such as tracking search history, bookmarking\
        \ searches or individual observations, and reviewing cart history. Registration\
        \ requires a valid email address and password.\n\n2. **Sign In:**\n   - Use\
        \ an email and password to sign in. There's an option to remember the email\
        \ address in the browser.\n\n3. **JavaScript Requirement:**\n   - Ensure that\
        \ JavaScript is enabled in your browser for the ODE website to function properly.\n\
        \n4. **Assistance:**\n   - For any problems or assistance, you can contact\
        \ the support team at ode@wunder.wustl.edu.\n\n5. **Data Availability:**\n\
        \   - All data are available at no charge. With a free login, users can enhance\
        \ their experience by using additional features related to search and cart\
        \ functionalities.\n\nWhile the text does not provide direct information about\
        \ accessing data using API or STAC terminology, you may have to explore the\
        \ ODE website further or contact their support for API documentation or STAC-based\
        \ access methods, especially after setting up an account and enabling JavaScript."
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Home Page {1} ##LOC[OK]## {1} ##LOC[OK]## ##LOC[Cancel]## {1} ##LOC[OK]##
        ##LOC[Cancel]## You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Welcome to the
        Orbital Data Explorer. All data are available at no charge. We offer a new
        free login, which allows users to track search history, bookmark searches
        and individual observations (PDS, ESA, and JAXA products), and review cart
        history. More information can be found in the ODE help. To report problems
        or request assistance, contact us at ode@wunder.wustl.edu Log In Email Need
        an account? Sign up Enter valid email address first. Password Remember my
        email address in this browser Sign in Forgot password Important Note: ODE
        has detected that JavaScript is not currently enabled in your browser. Please
        enable JavaScript to allow the website to function properly.

        '
      url: https://ode.rsl.wustl.edu/mercury/account/login.aspx
    extraction_006:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_datasets.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology,\
        \ you would need to consider some key aspects and follow these steps:\n\n\
        1. **Account and Access**: It's mentioned that you can \"Sign in\" or \"Create\
        \ a free account.\" You may need to sign in or create an account to access\
        \ some features or datasets.\n\n2. **Data Search Methods**:\n   - **Data Product\
        \ Search**: This would typically involve searching specific data products\
        \ using keywords or filters.\n   - **Map Search**: If available, this allows\
        \ you to search for data using a spatial map interface.\n\n3. **Tools and\
        \ Resources**: Make use of the \"Tools\" and \"Help & Resources\" sections\
        \ provided by ODE to facilitate data browsing, filtering, and acquisition.\n\
        \n4. **Usage of STAC**:\n   - As you intend to use STAC terminology, you should\
        \ be familiar with terms such as Collections, Items, and Catalogs, which are\
        \ part of the STAC specification for describing geospatial data. If ODE supports\
        \ STAC, you would need to look for endpoints or APIs that provide data in\
        \ STAC format.\n\n5. **Downloading Data**: After finding the required data\
        \ using the search tools, add them to your cart if necessary (mentioned: \"\
        Your cart contents\") and follow instructions to download.\n\nNote: This task\
        \ assumes you have access to a programming environment where you can use Python,\
        \ possibly with libraries like `requests` for making HTTP requests, and potentially\
        \ `pystac` if working directly with STAC data formats."
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Data Set Browser You are an anonymous user. Sign in Create a free account
        Read account help Your cart contents Your cart is empty. Show cart Home Data
        Product Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mercury/datasets
    extraction_007:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_help.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code for downloading data from the Orbital Data Explorer\
        \ (ODE) using STAC terminology, you'll need to focus on how to perform searches\
        \ and downloads programmatically. Although the text snippet provided doesn't\
        \ contain specific API details or direct references to STAC terminology, it\
        \ does suggest a framework for interaction with the platform:\n\n1. **Account\
        \ Management:**\n   - You need to either sign in or create a free account\
        \ to access the data, as suggested by \"Sign in Create a free account\".\n\
        \n2. **Data Access Methods:**\n   - There are multiple ways to search for\
        \ data:\n     - **Data Product Search**: A way to query data based on specific\
        \ product criteria.\n     - **Map Search**: Likely involves geographical or\
        \ spatial queries.\n     - **Data Set Browser**: Possibly a way to browse\
        \ through available datasets.\n\n3. **Cart System:**\n   - The platform uses\
        \ a cart system, as indicated by \"Your cart contents Your cart is empty.\
        \ Show cart.\" This might imply that you can add specific data products to\
        \ a cart for batch downloading.\n\n4. **Help & Resources:**\n   - There is\
        \ a section for \"Help & Resources\" which may provide documentation or guides\
        \ on how to use the ODE effectively.\n\nTo extract data using STAC (SpatioTemporal\
        \ Asset Catalog) terminology, you generally interact with APIs using endpoints\
        \ such as `/search`, `/collections`, and `/items` to filter and download geospatial\
        \ data. The typical steps would involve:\n\n- **Signing In**: Authenticating\
        \ to use the ODE services.\n- **Searching for Data**: Using a search API or\
        \ filters to find the datasets you are interested in.\n- **Using the Cart**:\
        \ Adding items to a cart for bulk actions, which might be an important step\
        \ in the interaction process.\n- **Downloading Data**: Finally, you would\
        \ download the selected datasets.\n\nIn Python, interaction with such an API\
        \ might require libraries like `requests` for dealing with HTTP requests or\
        \ specific STAC client libraries if they are available for the ODE."
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Help and Resources You are an anonymous user. Sign in Create a free account
        Read account help Your cart contents Your cart is empty. Show cart Home Data
        Product Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mercury/help
    extraction_008:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_index_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code to download data from the Orbital Data Explorer\
        \ (ODE) with a focus on STAC (SpatioTemporal Asset Catalog) terminology, here\
        \ are the key points extracted from the text:\n\n1. **Data Product Search**:\
        \ Use the search functionality to find orbital science products. This can\
        \ be done based on different criteria like missions, instruments, data sets,\
        \ time, location, and product IDs.\n\n2. **Download Cart**: You can download\
        \ products that are added to the cart. This implies a two-step process where\
        \ you first search and add the products you want to download into a cart,\
        \ and then proceed with the download.\n\n3. **Enabling JavaScript**: Note\
        \ that JavaScript must be enabled in the browser for the ODE website to function\
        \ correctly. If you are automating the download process via a script, ensure\
        \ that your approach can handle or bypass JavaScript functionalities.\n\n\
        4. **STAC Terminology**:\n   - **Collections**: These can correspond to different\
        \ data sets, missions, or instruments available.\n   - **Items**: Individual\
        \ data products that can be searched and downloaded.\n   - **Assets**: These\
        \ could represent the downloadable files associated with each item.\n\n5.\
        \ **Communication and Support**: For any questions or issues, you can contact\
        \ the support at ode@wunder.wustl.edu.\n\nTo implement the download in Python,\
        \ you might need to use libraries like `requests` for handling HTTP requests\
        \ if there's an API available, or `selenium` if JavaScript interactions are\
        \ required. Here is a simple template of how you might start:\n\n```python\n\
        # Import necessary libraries\nimport requests\n\n# Define base URL and endpoints\n\
        base_url = \"https://mercury.ODE.example.com\"  # Example URL, replace with\
        \ the actual one if available\nsearch_endpoint = \"/search\"\ndownload_endpoint\
        \ = \"/download\"\n\n# Example function to search for data products\ndef search_data_products(query_params):\n\
        \    response = requests.get(f\"{base_url}{search_endpoint}\", params=query_params)\n\
        \    if response.status_code == 200:\n        return response.json()  # Assuming\
        \ the API returns JSON\n    else:\n        print(\"Search failed:\", response.status_code)\n\
        \        return None\n\n# Example function to download data products\ndef\
        \ download_data_product(product_id):\n    response = requests.get(f\"{base_url}{download_endpoint}/{product_id}\"\
        )\n    if response.status_code == 200:\n        with open(f\"{product_id}.data\"\
        , \"wb\") as file:\n            file.write(response.content)\n        print(f\"\
        Downloaded product {product_id} successfully.\")\n    else:\n        print(f\"\
        Failed to download product {product_id}:\", response.status_code)\n\n# Add\
        \ any custom functionality for handling JavaScript or interacting with the\
        \ cart system.\n\n# Example usage\nif __name__ == \"__main__\":\n    # Define\
        \ the query parameters\n    query_params = {\n        \"mission\": \"Messenger\"\
        ,\n        \"instrument\": \"Some Instrument\",\n        \"start_time\": \"\
        YYYY-MM-DD\",\n        \"end_time\": \"YYYY-MM-DD\"\n    }\n    \n    products\
        \ = search_data_products(query_params)\n    if products:\n        for product\
        \ in products.get('items', []):\n            download_data_product(product['id'])\n\
        ```\n\nThis template assumes a REST API is available, which may not be the\
        \ case if the website heavily relies on JavaScript and dynamic content. In\
        \ that case, tools like Selenium or Puppeteer (though Puppeteer is primarily\
        \ for Node.js) might be needed to interact with the web interface."
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Home Page You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources Welcome
        to The Mercury Orbital Data Explorer The PDS Geosciences Node Mercury Orbital
        Data Explorer (ODE) provides search, display, and download tools for the PDS
        science data archives of the Messenger mission. Choose one of the above tabs
        to start using ODE. JavaScript must be enabled for the ODE website to function
        properly Browser Frames must be enabled for the ODE website to function properly
        Important Note: ODE has detected that JavaScript is not currently enabled
        in your browser. Please enable JavaScript to allow the website to function
        properly. Data Product Search Search for orbital science products across missions,
        instruments, and data sets via time, location, and product ids. What''s New
        See what''s new with ODE Additional Tools Product Type Coverage Help & Resources
        Access the ODE help, find additional resources, and see what''s coming Data
        Set Browser Browse through the orbital data set files stored in the PDS archives
        Available Data Sets A full list of mission, instrument, and product types
        available in Mercury ODE Download Cart Download products added to the cart
        from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE The Mercury
        Orbital Data Explorer is produced by the PDS Geosciences Node at Washington
        University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mercury/index.aspx
    extraction_009:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_pagehelp_Content_Web_Interface_User_Account_User_accounts_intro_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To download data from the Orbital Data Explorer (ODE) using STAC (SpatioTemporal
        Asset Catalog) terminology, you would focus on the specific functions and
        capabilities of ODE related to searching and accessing data. From the provided
        text, here are the relevant points for achieving this objective:


        1. **Account Creation and Login**: To access certain features of ODE, such
        as tracking search history and bookmarking items, you need to create and log
        into a user account. This account is used across all versions of ODE (Mars,
        Mercury, Lunar, and Venus).


        2. **Product Search**: Use the product search feature of ODE to find specific
        items or datasets. This might include searching for specific PDS, ESA, and
        JAXA products.


        3. **Map Search**: Utilize the map search feature to find spatial data. This
        would be particularly relevant for accessing data in a manner consistent with
        STAC''s geospatial focus.


        4. **Product Detail Page**: Once a product is located, the product detail
        page will offer more information and potential download options.


        5. **Bookmarks and Cart**: Once logged in, users can bookmark searches or
        individual observations and review or manage these items through a cart system.


        To implement these into your Python code:


        - **Authentication**: Handle user account sessions for login functionality
        if required for specific data access.

        - **Data Search**: Implement functions to interface with ODE''s search API,
        if available, corresponding with product and map searches.

        - **Data Access and Download**: Once desired data products are identified,
        download them using their URLs or any provided API. Use bookmarks or cart
        orders if needed to keep track of multiple products.


        Additionally, consider whether the ODE has an API you can interact with using
        a library like `requests` in Python for querying and downloading data. This
        would require checking ODE''s current documentation or contacting them directly
        via their provided email for detailed technical guidance.'
      prompt: ':::context_prompt :::extraction_prompt ODE User Accounts Skip To Main
        Content Account Settings Logout placeholder Account Settings Logout Filter:
        All Files Submit Search ODE User Accounts A new feature of ODE is an optional
        free user account . This account will be shared with the PDS Geosciences Node''s
        Analyst''s Notebook Website , for user convenience. The same user account
        is used for all versions of ODE. The user account allows ODEusers to track
        their search history, bookmark searches and individual observations (PDS,
        ESA, and JAXAproducts), and review cart history. Users need to log into each
        version of ODE (Mars, Mercury, Lunar, and Venus) to view their histories,
        bookmarks, and cart history for that version of ODE. See the following help
        links for details on various account features. Account maintance Creating
        an account Sign in Forgot password How to bookmark items Product search Map
        search Product detail page MROCoordinated Observation Logged in user options
        User access page History Bookmarks Cart orders If you have questions or have
        problems with the user account options, please contact us at ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm
    extraction_010:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_pagehelp_Content_Web_Interface_User_Account_creating_account_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To write Python code to download data from the Orbital Data Explorer\
        \ (ODE) using STAC terminology, you need to extract the key aspects related\
        \ to STAC (SpatioTemporal Asset Catalog). While the provided text focuses\
        \ on account creation for the ODE, it mentions several actions relevant to\
        \ accessing data:\n\n1. **Creating an Account**: \n   - Navigate to the ODE\
        \ website.\n   - Click on the login icon, and select \"Create an account.\"\
        \n   - Enter your email, password, and CAPTCHA text to create the account.\n\
        \n2. **Post-Account Features**:\n   - Once logged in, you can access additional\
        \ features such as bookmarking product detail pages and search result lists.\n\
        \nWhile this text doesn't specifically discuss STAC terminology, understanding\
        \ user account creation at ODE is crucial as data access can often be gated\
        \ by authentication. To download data programmatically from ODE using Python,\
        \ you will generally need:\n\n- Authorization headers for API requests which\
        \ involves using the email and password from the account creation process.\n\
        - Implementation of STAC API endpoints to search and download datasets, utilizing\
        \ STAC terminology such as Collections, Items, and Assets. \n\nMake sure to\
        \ consult the ODE API documentation to see if it supports STAC directly or\
        \ if you'll need to interface with a custom ODE API to perform STAC-like queries\
        \ and data retrieval."
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
      url: https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/creating_account.htm
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
        https://ode.rsl.wustl.edu/account/login.aspx: unknown
        https://ode.rsl.wustl.edu/download: unknown
        https://ode.rsl.wustl.edu/help: unknown
        https://ode.rsl.wustl.edu/lunar: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mapsearch: unknown
        https://ode.rsl.wustl.edu/mercury: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/account/login.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/datasets: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/help: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/index.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/creating_account.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/sign_in.htm: text/html
        https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm: text/html
        https://ode.rsl.wustl.edu/mercury/tools: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_10_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_15_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_10_3_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_12_11_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_13_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_15_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_21_2025.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_3_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_1_5_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_2_2_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_14_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_4_2_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_1_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_6_26_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_10_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_7_1_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mars_holdings_9_15_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_13_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_30_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_31_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_12_31_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_16_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_1_4_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_4_2_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_19_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_5_30_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_22_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_3_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_6_3_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_7_22_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Mercury_holdings_7_7_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_25_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_2_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_10_4_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_11_21_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_12_9_2023.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_1_24_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_1_29_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_2_12_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_11_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_12_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_20_2013.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_3_28_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_2_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_4_9_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_5_10_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_13_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_8_31_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Moon_holdings_9_17_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_16_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_30_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_11_3_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_1_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_12_2_2014.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_1_5_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_15_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_20_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_26_2025.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_2_2022.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_3_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_2_3_2024.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_16_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_18_2019.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_2_2018.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_3_7_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_4_6_2016.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_5_31_2012.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_6_1_2020.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_8_3_2017.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/Venus_holdings_9_1_2015.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/index.html: text/html
        https://ode.rsl.wustl.edu/odeholdings/oldholding.html: text/html
        https://ode.rsl.wustl.edu/pagehelp/Content/Web_Interface/User_Account/User_accounts_intro.htm: unknown
        https://ode.rsl.wustl.edu/productsearch: unknown
        https://ode.rsl.wustl.edu/tools: unknown
        https://ode.rsl.wustl.edu/venus: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/account/acctCreate.aspx: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/mapsearch: text/html; charset=utf-8
        https://ode.rsl.wustl.edu/venus/productsearch: text/html; charset=utf-8
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
