# orbital-data-explorer

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.


```yaml
"To generate the list of collections in ODE, we can use the following Python code:\n\
  \n```python\nfrom marsode import MarsODE\n\n# Initialize the MarsODE object\node\
  \ = MarsODE()\n\n# Get the list of collections\ncollections = ode.get_collections()\n\
  \nfor collection in collections:\n    print(collection)\n```\n\nThis code will initialize\
  \ the `MarsODE` object and then call the `get_collections` method to fetch the list\
  \ of collections available in ODE. Finally, it will print out the names of the collections.\n\
  \nMake sure to replace `marsode` with the actual package name you have used for\
  \ the ODE data access Python package."

```

```bash
@select orbital-data-explorer-$(@@timestamp)
@assistant script run - \
    script=orbital_data_explorer .

@assets publish push .

@assistant build_README
```



<details>
<summary>output</summary>

```yaml
integration_api_one:
  action: generic
  completed: true
integration_api_two:
  action: generic
  completed: true
researching_the_questions:
  action: generic
  completed: true
  max_iterations: 20
  output: "To generate the list of collections in ODE, we can use the following Python\
    \ code:\n\n```python\nfrom marsode import MarsODE\n\n# Initialize the MarsODE\
    \ object\node = MarsODE()\n\n# Get the list of collections\ncollections = ode.get_collections()\n\
    \nfor collection in collections:\n    print(collection)\n```\n\nThis code will\
    \ initialize the `MarsODE` object and then call the `get_collections` method to\
    \ fetch the list of collections available in ODE. Finally, it will print out the\
    \ names of the collections.\n\nMake sure to replace `marsode` with the actual\
    \ package name you have used for the ODE data access Python package."
  prompt: 'We want to use the following generalized STAC definitions to develop query
    and access mechanisms to  Orbital Data Explorer, ODE for short:

    We consider ODE as a catalog, similar to a STAC catalog. We define the datasets
    within ODE, if they exist, as separate collections, similar to STAC collections.
    We define the semi-atomic unit of data in ODE as a datacube, similar to a STAC
    item.

    write python code to generate the list of collections in ODE. :::input

    '
  visited_urls:
    https://github.com/samiriff/mars-ode-data-access: "GitHub - samiriff/mars-ode-data-access:\
      \ Python package that provides an easy-to-use interface to access data from\
      \ the Mars Orbital Data Explorer Skip to content Navigation Menu Toggle navigation\
      \ Sign in Product GitHub Copilot Write better code with AI Security Find and\
      \ fix vulnerabilities Actions Automate any workflow Codespaces Instant dev environments\
      \ Issues Plan and track work Code Review Manage code changes Discussions Collaborate\
      \ outside of code Code Search Find more, search less Explore All features Documentation\
      \ GitHub Skills Blog Solutions By company size Enterprises Small and medium\
      \ teams Startups Nonprofits By use case DevSecOps DevOps CI/CD View all use\
      \ cases By industry Healthcare Financial services Manufacturing Government View\
      \ all industries View all solutions Resources Topics AI DevOps Security Software\
      \ Development View all Explore Learning Pathways White papers, Ebooks, Webinars\
      \ Customer Stories Partners Executive Insights Open Source GitHub Sponsors Fund\
      \ open source developers The ReadME Project GitHub community articles Repositories\
      \ Topics Trending Collections Enterprise Enterprise platform AI-powered developer\
      \ platform Available add-ons Advanced Security Enterprise-grade security features\
      \ GitHub Copilot Enterprise-grade AI features Premium Support Enterprise-grade\
      \ 24/7 support Pricing Search or jump to... Search code, repositories, users,\
      \ issues, pull requests... Search Clear Search syntax tips Provide feedback\
      \ We read every piece of feedback, and take your input very seriously. Include\
      \ my email address so I can be contacted Cancel Submit feedback Saved searches\
      \ Use saved searches to filter your results more quickly Name Query To see all\
      \ available qualifiers, see our documentation . Cancel Create saved search Sign\
      \ in Sign up Reseting focus You signed in with another tab or window. Reload\
      \ to refresh your session. You signed out in another tab or window. Reload to\
      \ refresh your session. You switched accounts on another tab or window. Reload\
      \ to refresh your session. Dismiss alert samiriff / mars-ode-data-access Public\
      \ Notifications You must be signed in to change notification settings Fork 3\
      \ Star 9 Python package that provides an easy-to-use interface to access data\
      \ from the Mars Orbital Data Explorer License MIT license 9 stars 3 forks Branches\
      \ Tags Activity Star Notifications You must be signed in to change notification\
      \ settings Code Issues 0 Pull requests 0 Actions Projects 0 Security Insights\
      \ Additional navigation options Code Issues Pull requests Actions Projects Security\
      \ Insights samiriff/mars-ode-data-access master Branches Tags Go to file Code\
      \ Folders and files Name Name Last commit message Last commit date Latest commit\
      \ History 21 Commits ode_data_access ode_data_access .gitignore .gitignore LICENSE\
      \ LICENSE README.md README.md VERSION VERSION main.py main.py setup.cfg setup.cfg\
      \ setup.py setup.py View all files Repository files navigation README MIT license\
      \ Mars Orbital Data Explorer Access This project aims to provide an easy-to-use\
      \ interface to access data from the Mars Orbital Data Explorer (ODE) , maintained\
      \ by the Geosciences Node of NASA's Planetary Data System (PDS), via the ODE\
      \ REST Service Since the data return by the ODE usually consists of high-resolution\
      \ map-projected JP2 images, utility methods have also been provided to slice\
      \ each image into equal-size chunks with all black-margins cropped out so that\
      \ they can be processed by appropriate machine learning models. _____      \
      \                          ________  ________  ___________         ________\
      \          __                      _____                                   \
      \ \n  /     \\ _____ _______  ______         \\_____  \\ \\______ \\ \\_   _____/\
      \         \\______ \\ _____ _/  |______              /  _  \\   ____  ____ \
      \ ____   ______ ______\n /  \\ /  \\\\__  \\\\_  __ \\/  ___/  ______  /   |\
      \   \\ |    |  \\ |    __)_   ______  |    |  \\\\__  \\\\   __\\__  \\    ______\
      \  /  /_\\  \\_/ ___\\/ ___\\/ __ \\ /  ___//  ___/\n/    Y    \\/ __ \\|  |\
      \ \\/\\___ \\  /_____/ /    |    \\|    `   \\|        \\ /_____/  |    `  \
      \ \\/ __ \\|  |  / __ \\_ /_____/ /    |    \\  \\__\\  \\__\\  ___/ \\___ \\\
      \ \\___ \\ \n\\____|__  (____  /__|  /____  >         \\_______  /_______  /_______\
      \  /         /_______  (____  /__| (____  /         \\____|__  /\\___  >___\
      \  >___  >____  >____  >\n        \\/     \\/           \\/                \
      \  \\/        \\/        \\/                  \\/     \\/          \\/     \
      \             \\/     \\/    \\/    \\/     \\/     \\/ Project Structure root/\n\
      \u251C\u2500\u2500 ode_data_access/                \n\u2502   \u251C\u2500\u2500\
      \ autocropper.py                    Aligns, rotates and crops images to remove\
      \ black margins\n\u2502   \u251C\u2500\u2500 chunk_processor.py            \
      \    Slices a high-resolution (m x n) image into (m / p x n / p) chunks, where\
      \ each chunk is of size (p x p)\n\u2502   \u251C\u2500\u2500 image_utils.py\
      \                    Utility methods to process images\n\u2502   \u251C\u2500\
      \u2500 lblreader.py                      Reads an LBL file and converts it into\
      \ a map of key-value pairs\n\u2502   \u251C\u2500\u2500 query_processor.py \
      \               Constructs a HTTP Request to be sent to the Orbital Data Explorer,\
      \ using user-defined query parameters \n\u2502   \u251C\u2500\u2500 query_result_processor.py\
      \         Processes the results sent by the Orbital Data Explorer in response\
      \ to a user-defined query\n\u251C\u2500\u2500 LICENSE\n\u251C\u2500\u2500 main.py\
      \                                Provides Sample Usage of package\n\u251C\u2500\
      \u2500 README.md\n\u251C\u2500\u2500 setup.cfg\n\u251C\u2500\u2500 setup.py\n\
      \u2514\u2500\u2500 VERSION Basic Usage Run main.py to generate a sample query\
      \ and fetch sample results: python main.py The entire process consists of 3\
      \ steps: 1. Initialize Query Processor Initialize an instance of the QueryProcessor\
      \ class to process user-defined query parameters, details of which are given\
      \ in the upcoming sections: query_processor = QueryProcessor()\nquery_results\
      \ = query_processor.query_files_urls(target, mission, instrument, product_type,\n\
      \                                                 western_lon, eastern_lon,\
      \ min_lat, max_lat,\n                                                 min_ob_time,\
      \ max_ob_time, product_id, file_name,\n                                    \
      \             number_product_limit, result_offset_number) Supported Query Parameters\
      \ The list of supported query parameters is as shown below: Parameter Description\
      \ target Aimed planetary body, i.e., Mars, Mercury, Moon, Phobos, or Venus mission\
      \ Aimed mission, e.g., MGS or MRO instrument Aimed instrument from the mission,\
      \ e.g., HIRISE or CRISM product_type Type of product to look for, e.g., DTM\
      \ or RDRV11 western_lon Western longitude to look for the data, from 0 to 360\
      \ eastern_lon Eastern longitude to look for the data, from 0 to 360 min_lat\
      \ Minimal latitude to look for the data, from -90 to 90 max_lat Maximal latitude\
      \ to look for the data, from -90 to 90 product_id PDS Product Id to look for,\
      \ with wildcards (*) allowed min_ob_time Minimal observation time in (even partial)\
      \ UTC format, e.g., '2017-03-01' max_ob_time Maximal observation time in (even\
      \ partial) UTC format, e.g., '2017-03-01' file_name File name to look for, with\
      \ wildcards (*) allowed number_product_limit Maximal number of products to return\
      \ (100 at most) result_offset_number Offset the return products, to go beyond\
      \ the limit of 100 returned products remove_ndv Replace the no-data value as\
      \ mentionned in the label by np.nan 2. Initialize Query Result Processor Initialize\
      \ an instance of the QueryResultProcessor class to process the results returned\
      \ by your QueryProcessor instance. In this step, you will have to specify user-defined\
      \ parameters for the chunks and bin type (if applicable): query_result_processor\
      \ = QueryResultProcessor()\nshould_continue = query_result_processor.download(query_results,\
      \ bin_type, product_types)\n\n## Add the following lines only if you wish to\
      \ chunkify all downloaded images\nif should_continue:\n  query_result_processor.process(SAVE_DIR_PREFIX,\
      \ CHUNK_SIZE, SKIP_BLACK_IMAGES, ALIGN_AND_CROP_THRESHOLDS, None) Supported\
      \ Query Result Parameters The list of supported query result parameters is as\
      \ shown below: Parameter Description bin_type Type of binning used in image\
      \ - Bin1 = 0.35 cm/pixel, Bin2 = 2xBin1, Bin4 = 2xBin2 product_types Set of\
      \ product types to which any downloaded product should belong. Eg., PRODUCT\
      \ DATA FILE, BROWSE, GREYSCALE THUMBNAIL Chunk Parameters The following parameters\
      \ can be used to control how chunks are processed: Parameter Description save_dir_prefix\
      \ Prefix to be used in the name of the directory where the chunks of an image\
      \ will be saved. For eg., chunks of an image \"ESP_123_456.JP2\" will be saved\
      \ in a directory named \"save_dir_prefix_ESP_123_456\" chunk_size Size of each\
      \ chunk that will be sliced from a high-resolution image. Eg., 1024 vectorized_chunks\
      \ List in which all chunks of all JP2 images will be aggregated. If not required,\
      \ just assign None skip_black_images Flag to indicate that all images containing\
      \ black pixels near the center should be skipped Chunk Alignment and Cropping\
      \ Thresholds The following parameters can be used to control how a chunk containing\
      \ black margins, is aligned, cropped and/or rotated: Parameter Description max_border_size\
      \ Border to be checked around the image while aligning and cropping black margins\
      \ safety_margin Removes extra pixels from the sides to make sure no black remains\
      \ while aligning and cropping black margins tolerance A gray value is more likely\
      \ to be considered black when you increase the tolerance 3.  Vectorized Chunks\
      \ (Optional) If you wish to accumulate all chunks of all images into a python\
      \ list, then initialize an empty list before step 1, and each time you call\
      \ the QueryResultProcessor for multiple queries, pass this list as the vectorized_chunks\
      \ parameter: query_result_processor.process(SAVE_DIR_PREFIX, CHUNK_SIZE, SKIP_BLACK_IMAGES,\
      \ ALIGN_AND_CROP_THRESHOLDS, vectorized_chunks) Acknowledgements scikit-dataaccess\
      \ Autocroppy scikit-image About Python package that provides an easy-to-use\
      \ interface to access data from the Mars Orbital Data Explorer Topics nasa rest-api\
      \ crop ode mars preprocessing jp2 pds chunks Resources Readme License MIT license\
      \ Activity Stars 9 stars Watchers 1 watching Forks 3 forks Report repository\
      \ Releases No releases published Packages 0 No packages published Languages\
      \ Python 100.0% Footer \xA9 2025 GitHub,\_Inc. Footer navigation Terms Privacy\
      \ Security Status Docs Contact Manage cookies Do not share my personal information\
      \ You can\u2019t perform that action at this time."
    https://ode.rsl.wustl.edu/about/default.htm: ''
    https://ode.rsl.wustl.edu/checksums.html: ''
    https://ode.rsl.wustl.edu/gravity_models.htm: ''
    https://ode.rsl.wustl.edu/login?return_to=https%3A%2F%2Fgithub.com%2Fsamiriff%2Fmars-ode-data-access: ''
    https://ode.rsl.wustl.edu/missions/clps/index.htm: ''
    https://ode.rsl.wustl.edu/missions/mars_express/mars.htm: ''
    https://ode.rsl.wustl.edu/missions/mars_express/spicam.htm: ''
    https://ode.rsl.wustl.edu/missions/messenger/rs.htm: ''
    https://ode.rsl.wustl.edu/missions/messenger/xrs.htm: ''
    https://ode.rsl.wustl.edu/missions/odyssey/themis.html: ''
    https://ode.rsl.wustl.edu/missions/phoenix/ra.htm: ''
    https://ode.rsl.wustl.edu/missions/viking/gravity.html: ''
    https://ode.rsl.wustl.edu/missions/vlander/seismic.html: ''
    https://ode.rsl.wustl.edu/samiriff: ''
    https://ode.rsl.wustl.edu/solutions/industry: ''
    https://ode.rsl.wustl.edu/solutions/industry/financial-services: ''
    https://ode.rsl.wustl.edu/topics/jp2: ''
    https://ode.rsl.wustl.edu/topics/pds: ''
    https://pds-geosciences.wustl.edu/dataserv/default.htm: "PDS Geosciences Node\
      \ Data and Services + NASA Homepage + NASA en Espa\xF1ol + Contact NASA HOME\
      \ DATA AND SERVICES TOOLS ABOUT US CONTACT US SITE MAP Services Analyst's Notebooks\
      \ Orbital Data Explorers Spectral Library FTP Access Workshops Geosciences Node\
      \ Data Mars Mars Exploration Mars 2020 About Mars 2020 PIXL Returned Sample\
      \ Science RIMFAX SHERLOC SuperCam InSight About InSight HP3/RAD IDA RISE SEIS\
      \ MSL About MSL APXS ChemCam CheMin DAN SAM MRO About MRO CRISM SHARAD Gravity/Radio\
      \ Science MER Mars Express About Mars Express ASPERA HRSC MaRS MARSIS OMEGA\
      \ PFS SPICAM SPICE VMC Odyssey About Odyssey THEMIS GRS MARIE Radio Science\
      \ Accelerometer SPICE Phoenix About Phoenix MECA RA TEGA MGS About MGS MOLA\
      \ MOC TES MAG/ER Radio Science Accelerometer SPICE Pathfinder About Pathfinder\
      \ IMP 3-D Summary Image Radio Science Prototype Rovers Viking Orbiter About\
      \ Viking Orbiter VIS-EDR Images MDIM/MDTM IRTM MAWD LOS Gravity VO/Mariner 9\
      \ Topo Viking Lander About Viking Lander EDR Images Rock Data Set Labeled Release\
      \ Seismic Data Mariner About Mariner Mariner Mars 1969 Images Earth Based Data\
      \ About Earth Based Data HST Venus Magellan About Magellan F-BIDR C-BIDR F-MIDR\
      \ C 1,2,3-MIDR ALT-EDR ARCDR GXDR SCVDR GVDR BSR LOSAPDR Spherical Harmonic,\
      \ Topo and Gravity Radio Tracking Pre-Magellan Venus Radar Venera Mercury MESSENGER\
      \ About MESSENGER GRS/NS MASCS MLA Radio Science XRS Moon Moon Data GRAIL CLPS\
      \ Chandrayaan-1 Chang'e LCROSS LRO About LRO Diviner LEND LOLA Mini-RF Radio\
      \ Science Apollo Kaguya MSX Lunar Prospector About Lunar Prospector Level 0\
      \ Data Level 1 Spectrometer Data Reduced Spectrometer Data Spherical Harmonics\
      \ Gravity Models LOS Gravity MAG/ER Data ODF Data Lunar Radar 70 cm Lunar Radar\
      \ 12.6 cm (S-Band) Lunar Radar South Pole DEM Lunar Spectroscopy Clementine\
      \ About Clementine Gravity/Topo Raw LIDAR LWR Brightness Temperature Raw Bistatic\
      \ Radar Reduced Bistatic Radar Pre-Magellan Earth Earth Data Amboy Crater GRSFE\
      \ Laboratory Data Nevada LIDAR Pre-Magellan Asteroids NEAR About NEAR NLR Radio\
      \ Science Gravity Models All Geosciences DOIs All Geosciences Data \r\n\tHoldings\
      \ Help Frequently Asked \t\t\t\t\t\t\t\t\t\t\t\t\tQuestions Geosciences Node\
      \ Forums Help for Data Users Help \r\n                                     \
      \       for Data Reviewers Help for Proposers About PDS4 About Checksums Cite\
      \ PDS On Your Poster Email Us Scheduled Maintenance This site may be down on\
      \ Thursdays between 7:00 and 9:30 pm Central Time for maintenance. Data The\
      \ Geosciences Node \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tarchives data \r\n\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\trelated to the study \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \tof moons and planets \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tof the inner Solar\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSystem. The \r\n\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\tnavigation bar on \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tthe left side of \r\
      \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\teach page has links \r\n\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\tto data sets grouped \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tby planet,\
      \ mission, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand instrument. \r\n\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\tClick the links to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\texpand\
      \ the list and \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlocate the data of \r\n\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\tinterest. Another way to \r\n\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\tlocate data is to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tstart at the list\
      \ of all Geosciences Node \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tdata holdings ,\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\twhere data sets are \r\n\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tlisted in \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\talphabetical order\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tby mission and \r\n\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\tinstrument name. Services Some \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      datasets \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\thave \r\n\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tcustomized \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tsearch tools\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tto help the \r\n\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tuser select \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand view \r\n\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tdata \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      products. Analyst's \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNotebooks - provide\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\taccess to \r\n\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\tlanded \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmission data \r\n\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tarchives by \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\tintegrating \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tsequence \r\n\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\tinformation, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      engineering \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand science \r\n\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\tdata, and \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tdocumentation\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tinto \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\tstandard \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tweb-accessible \r\n\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\tpages. Perseverance Curiosity Opportunity \r\n\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand Spirit Phoenix Apollo Orbital Data \r\n\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tExplorers - provide \r\n\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\tsearch, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tdisplay, and \r\
      \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tdownload \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\ttools for \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\torbital data \r\n\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\tintegrated \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      across \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tinstruments, \r\n\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\tmissions, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand nodes.\
      \ M ars L unar M ercury V enus PDS \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGeosciences\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSpectral \r\n\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\tLibrary - a collection \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tof \r\
      \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlaboratory \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\tspectra of \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEarth, \r\n\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\tlunar, and \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      meteorite \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmaterials to \r\n\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\tbe used to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcompare\
      \ to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tflight \r\n\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\tmeasurements. \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThe tool \r\n\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tallows \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \tsearching of \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tspectra \r\n\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\tbased on the \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmaterial\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tclassification \r\n\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\tand other \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tparameters.\
      \ Odyssey GRS Data Node - provides \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcustom-generated\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGRS data \r\n\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\tproducts \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttailored to \r\n\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\tthe user's \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \tspecifications. TES Data \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNode - provides\
      \ a search \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttool for the \r\n\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\tMGS TES Data \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      Archive.\_Constrain \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tsearch by \r\n\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\tposition, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \torbit \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tnumber, scan \r\n\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\tlength, time \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tof day,\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tatmospheric \r\n\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tconditions, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand \r\n\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\tobservation \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      \t\ttype. Anonymous FTP \r\n                        Access - explains \r\n\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\thow to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      download \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGeosciences \r\n\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\t\t\t\tNode data \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tusing FTP.\
      \ Geosciences \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNode Site - If the data\
      \ \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tset you want \r\n\t\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tis not \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tonline, \r\n\t\t\t\
      \t\t\t\t\t\t\t\t\t\t\t\t\t\tcontact us \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
      at geosci@wunder.wustl.edu . Workshops Workshops - the \r\n\t\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\tGeosciences Node \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\thosts workshops\
      \ to \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\thelp users learn \r\n\t\t\t\t\t\t\t\t\
      \t\t\t\t\t\t\tmore about \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tparticular data \r\
      \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tsets. Receiving PDS Release \r\n\t\t\t\t\t\t\
      Announcements PDS Subscription Service - sign up to \r\n                   \
      \     receive email announcements when PDS releases new \r\n               \
      \         data, software, or documentation. + Freedom of Information Act + NASA\
      \ Strategic Plans + NASA Privacy Statement, Disclaimer, and Accessibility Certification\
      \ + Copyright/Image Use Policy Curator: Jennifer Ward NASA Official: Paul Byrne\
      \ Last Updated: + Comments and Questions"

```

</details>



<details>
<summary>workflow</summary>

![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-02-04-6b8mp6/thumbnail-workflow.png?raw=true)

</details>


[orbital-data-explorer-2025-02-04-6b8mp6](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-02-04-6b8mp6.tar.gz)
