# Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.

# ~~~~~~~~~~~~~~~~~~~~~ Importing required packages -

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import webbrowser

# ~~~~~~~~~~~~~~~~~~~~~ Different User pages and respective functions -

# ~~~~~~~~~~ Home Page -

def home_page():
    # Setting the title -
    st.title("TAMIDS Data Science Competition")

    # Desription -
    st.markdown("""
                <p style='text-align: justify;'>
                The 2021 TAMIDS Data Science Competition is about finding the
                impact of research and an approach to help increase the
                influence through selecting relevant subfields/areas.
                </p>
                """, unsafe_allow_html=True)

    # Problem Statement -
    st.write("""
             ## Problem Statement
             """)
    st.markdown("""
                <p style='text-align: justify;'>
            In the competitive world of academia and research, it's important
            to be aware of the peers and stay on top of things. The aim is to
            look at bibliometric data, analyze the connections between
            different research papers and departments to maximize the impact
            of research.
             </p>
                """, unsafe_allow_html=True)

    # Data Collection and Pre-processing -
    st.write("""
             ## Data Collection and Pre-processing
             """)
    st.markdown("""
                <p style='text-align: justify;'>
             The analysis has been made on two groups of data: Grants and Publications. We created a dataset with
             different publication data including abstract, departments, research institutions and citation data.
             ----------------Something about data collection------------
             </p>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: justify;'>
             -----More details on data obtained from web scraping----
             </p>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: justify;'>
             Data Cleaning explanation
             Data Merge
             </p>
                """, unsafe_allow_html=True)

    # Overview -
    st.write("""
             ## Methodology
             """)
    st.markdown("""
                <p style='text-align: justify;'>

                * **Feature Engineering:** Data normalization explained
                * **Unsupervised Learning:** Clustering based on different
                features of the data.
                Rather, with the mapper package, we see a better picture of our
                clusters which brings us to the visualizations.
                * **Dynamic Visualization:** About TDA and other visualization.
                Therefore, the website we have designed is very dynamic and suitable for everyone.
             </p>
                """, unsafe_allow_html=True)

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")


def get_dept_collab_graph(dept_1, dept_2):
    return
    #Getting the graph
    HtmlFile = open(f"",'r',encoding = 'utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2,height = 500)

#------------------ Publication Analysis----------------
def publication_analysis():
    # Setting the title
    st.title('Publication Analysis and NLP')

    #description
    st.markdown("""
                <p style='text-align: justify;'>
                The key aspect of the project was to do Natural Language
                processing on the bibliometric data and find meaningful insights.
                Different keywords are related to different professors and departments
                with a possibility or existence of collaboration.
                """,unsafe_allow_html = True)
    st.write("")

    #Getting the intial Image
    col1, col2, col3 = st.beta_columns((1,2.5,1))

    #Showing initial analysis
    st.markdown("""
                <p style='text-align: justify;'>
                The plot shows this this....
                </p>
                """, unsafe_allow_html = True)
    st.write(" ")
    #Another graph
    st.markdown("""
                <p style='text-align: justify;'>
                Description of the same graph
                   </p>  """,unsafe_allow_html = True )
    st.write(" ")

    col1, col2 = st.beta_columns((1,1))
    dept_lst = [' Aerospace Engineering',' Biochemistry and Biophysics',
    ' Biological and Agricultural Engineering', ' Biomedical Engineering',
    ' Chemical Engineering', ' Computer Science and Engineering',
    ' Learning and Culture', ' Materials Science and Engineering',
    ' Ocean Engineering', ' Park and Tourism Sciences',
    ' Veterinary Integrative Biosciences', 'Animal Science',
    'Biological and Agricultural Engineering', 'Chemistry',
    'Civil Engineering', 'Electrical and Computer Engineering',
    'Mechanical Engineering', 'Molecular and Cellular Medicine',
    'Recreation', 'Teaching', 'Veterinary Physiology and Pharmacology']
    #Getting dept_1 from user
    dept_1 = col1.selectbox("Select department 1",dept_lst)

    #Getting dept_2 from user
    dept_2 = col2.selectbox("Select department 2",dept_lst)

    #Getting the graph
    get_dept_collab_graph(dept_1,dept_2)


    st.markdown("""
                <p style ='text-align: justify;'>
                This graph describes the collaboration which already exists between
                different departments. Top few departments are chose for the sake
                of complexity and large dataset for demonstration.
                </p>
                """,unsafe_allow_html = True)
    st.write("")

    #Dept_collab interactive analysis
    st.markdown("""
                <p style='text-align: justify;'>
                The following interactive graph is about the collaboration
                between different departments and with different publication
                years
                </p>
                """, unsafe_allow_html = True)
    st.write(" ")
    st.write("""
            You can go to the department collaboration page by clicking on the
            link. Below is a snapshot of the dept collaboration network analysis.
            """)
    # To access the network analysis, press the button below -
    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    link = '[Go to Department Network Analysis](TDA_TAMIDS/dept_collab_2.html)'
    col2.markdown(link, unsafe_allow_html=True)
    # url = 'https://ritesh-suhag.github.io./'
    # if col2.button("Go to the Network Analysis"):
    #     webbrowser.open_new_tab(url)

    st.write(" ")
    #Setting the Image
    #image = Image.open('Images/dept_collab.png')

    #Setting the image width
    #st.image(image, use_column_width = True)

    st.write(" ")


    #Univ_collab interactive analysis
    st.markdown("""
                <p style='text-align: justify;'>
                The following interactive graph is about the collaboration
                between different universities, which can be further filtered to
                different departments.</p>
                """,unsafe_allow_html=True)
    st.write(" ")
    st.write("""
            You can go to the University collaboration page by clicking on the
            link. Below is a snapshot of the university collaboration network analysis.
            """)
    # To access the network analysis, press the button below -
    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    link = '[Go to University Network Analysis](https://lucky301910.github.io./)'
    col2.markdown(link, unsafe_allow_html=True)
    # url = 'https://ritesh-suhag.github.io./'
    # if col2.button("Go to the Network Analysis"):
    #     webbrowser.open_new_tab(url)

    st.write(" ")
    #Setting the Image
    image = Image.open('Images/univ_collab.png')

    #Setting the image width
    st.image(image, use_column_width = True)

    st.write(" ")


#------------------ Grant Analysis -------------------------
def get_grant_graph(dept, year):
    # Getting the Graph -
    if year == '2020 - Current':
        year = '2020'
    elif year == '2010 - 2019':
        year = '2010'
    elif year == '2000 - 2009':
        year = '2000'
    elif year == 'Before 1999':
        year = 'old'
    HtmlFile = open(f"", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=500)

def get_grant_analysis():
    #Setting the title
    st.title("Grant Analysis and Natural Language processing")

    #Description
    st.markdown("""
                <p style='text-align: justify;'>
                The data related to funding has information about the topic for
                which the funding was provided and the departments which are
                involved. In addition to the amount, it also has the duration
                of the funding.
                </p>""",unsafe_allow_html = True)
    st.write("")

    #Getting the initial image
    col1, col2, col3 = st.beta_columns((1,2.5,1))

    #Showing intial analysis
    st.markdown("""
                <p style ='text-align: justify;'
                This plot shows.........
                </p>""",unsafe_allow_html = True)
    st.write(" ")
    #Another graph
    st.markdown("""
                <p style = 'text-align: justify;'
                Description of the same graph
                </p>""",unsafe_allow_html=True)
    st.write(" ")

    col1, col2 = st.beta_columns((1,1))
    depts = ['All','Math', 'Physics',
    'Chemistry', 'Earth Science', 'Environmental', 'Biology',
    'Agricultural and Veterinary Sciences', 'Computer Science',
    'Engineering', 'Technology', 'Medical and Health Sciences',
    'Environment and Design', 'Education', 'Economics',
    'Commerce, Management, Tourism and Services', 'Human Society',
    'Psychology and Cognitive Sciences', 'Law',
    'Language, Communication and Culture', 'History and Archaeology',
    'Philosophy and Religious Studies']

    #Geting dept from user
    dept = col1.selectbox("Select department",depts)

    #Getting year info from user
    year = col2.selectbox("Select year range",['All','2020 - Current',
    '2010 - 2019', '2000 - 2009', 'Before 1999'])

    get_grant_graph(dept, year)

    st.markdown("""
                <p  style = 'text-align: justify;'
                This graph describes the funding received by different
                departments over the years. The plot contains information
                about the amount of funding received per year, the total
                amount of funding received for every department.
                </p> """,unsafe_allow_html = True)
    st.write(" ")


    #Grant_collab interactive analysis
    st.markdown("""<p style= 'text-align : justify;'>
                The following interactive graph is about the clustering of
                different departments accoring the connectivity with
                other departments. One can look up multiple departments in
                the searchbox to see the joint grant awards.
                </p>""",unsafe_allow_html = True)
    st.write(" ")

    st.write("""
            You can go to the grant network analysis page by clicking
            on the link. Below is a snapshot of the department-wise Grant
            network analysis""")

    #To access the network analysis, press the button below.

    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    link = '[Go to dept_wise grant analysis](https://lucky301910.github.io./)'
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    #Setting the Image
    #image = Image.open('Images/dept_collab.png')

    #Setting the image width
    #st.image(image, use_column_width = True)

    st.write(" ")

#------------------ Impact score -----------------------------



#------------------ About the Authors -------------------------
def authors():
    # Setting the title -
    st.title("About the Authors")
    st.write(" ")


    # Dividing screen into 2 parts -
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))

    # Setting the image -
    #image = Image.open('Images/tushar.png')

    # Setting the image width -
    col1.write("")
    #col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Tushar Pandey")

    # About section -
    col3.write("""
               Research Area: Quantum Topology

               * **University:** Texas A&M University (Department of Mathematics)
               * **Degree:** PhD Student (2024)
               * **Email:** tusharp@tamu.edu
               * **LinkedIn:** [linkedin.com/in/tushar-pandey1612/](https://www.linkedin.com/in/tushar-pandey1612/)
               * **Github:** [github.com/pandey-tushar](https://github.com/pandey-tushar)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))

    # Setting the image -
    #image = Image.open('Images/sambandh.png')

    # Setting the image width -
    col1.write("")
    col1.write("")
    #col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")

    # About section -
    col3.write("""
               Research Area: Error Estimation and Machine Learning.

               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering)
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/Sambandh](https://github.com/Sambandh)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))

    # Setting the image -
    #image = Image.open('Images/swarnabha.png')

    # Setting the image width -
    col1.write("")
    col1.write("")
    #col1.image(image, use_column_width=True)

    # Abhijit Mahapatra -
    col3.write("## Abhijit Mahapatra")

    # About section -
    col3.write("""
               Research Area: Data Science

               * **University:** Texas A&M University (Department of Computer Engineering)
               * **Degree:** Masters Student (Computer Engineering)
               * **Email:** mahapatraabhijit.9@tamu.edu
               * **LinkedIn:** [linkedin.com/in/abhijit-mahapatra807/](https://www.linkedin.com/in/abhijit-mahapatra807/)
               """)
    st.write("")
    # Dividing screen into 2 parts -
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))

    # Setting the image -
    #image = Image.open('Images/swarnabha.png')

    # Setting the image width -
    col1.write("")
    col1.write("")
    #col1.image(image, use_column_width=True)

    # Swarnabha -
    col3.write("## Swarnabha Roy")

    # About section -
    col3.write("""
               Research Area: Modular Robotics and Virtual Reality.

               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering)
               * **Email:** swarnabha7@tamu.edu
               * **LinkedIn:** [linkedin.com/in/swarnabha-roy-53a588a4/](https://www.linkedin.com/in/swarnabha-roy-53a588a4/)
               * **Github:** [github.com/swarnabha13](https://github.com/swarnabha13)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))

    # Setting the image -
    #image = Image.open('Images/swarnabha.png')

    # Setting the image width -
    col1.write("")
    col1.write("")
    #col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Rohit Dube")

    # About section -
    col3.write("""
               Research Area: Operations Research

               * **University:** Texas A&M University (Department of Industrial Engineering)
               * **Degree:** PhD Student (Industrial Engineering)
               * **Email:** dube.rohit@tamu.edu
               * **LinkedIn:** [linkedin.com/in/rohitdube922/](https://www.linkedin.com/in/rohitdube922/)
               """)
    st.write("")

#* **Github:** [github.com/swarnabha13](https://github.com/swarnabha13)






#--------------------------- Main Application page----------------

st.set_page_config(layout='wide', page_title = 'Bibliometric Research')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar navigation for users -
st.sidebar.header('Navigation tab -')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page',
 'Publication Analysis', 'Grant Analysis',
 'Impact score', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Publication Analysis':
    publication_analysis()


# Second Page -
elif navigation_tab == 'Grant Analysis':
    get_grant_analysis()

# Third Page -
elif navigation_tab == 'Impact score':
    impact_score()

# About Page -
elif navigation_tab == 'About the Authors':
    authors()
