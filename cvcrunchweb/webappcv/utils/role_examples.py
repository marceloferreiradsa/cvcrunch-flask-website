resume = """Marcelo ferreira
marcelo.ferreira.dsa@gmail.com  +55 61 999 220 052
https://www.linkedin.com/in/marcelo-ferreira-dsa/
OBJECTIVE: Junior Psychometric Analyst
may 2020 – april 2022
sENIOR strategic ADVISOR, BANCO DO BRASIL – Operations UNity – Analytics Team

Select and acquire data from diverse sources to support team objectives and projects.
Modeled, designed, and maintained DB2 and MySQL databases, overseeing all ETL processes.
Planned, collected requirements, developed, and implemented tailor-made dashboards for all areas within Operations Unity.
Advised internal and external consultants as a Subject Matter Expert in communicating technical features in non-technical language.
Mapped, planned and implemented actions to leverage data-driven culture for all departments under Operations Unity umbrella targeting over eleven thousand employees.
Designed and conducted workshops for operational and management audiences.
march 2018 – april 2020
sENIOR strategic ADVISOR, BANCO DO BRASIL – Operations UNity – cash management Team

Designed and implemented KPIs, visualizations to monitor their progress, and the complete data infrastructure, including database modeling, ETL processes, data source selection, and screen scraping (when needed).
Designed and reviewed operational processes.
Control and manage national and foreign currency cash balance.
Wrote all internal rules and regulations for operational processes.
Elaborated a forecast model for foreign currency demand what reduced risks and costs due to unused balance and unnecessary imports.
Designed visuals to control the balance of all foreign currency internal accounts what ultimately have led to locate the origin of more than USD 2.5 million unreconciled balances. This solved a two-year long problem that have exposed the bank to legal risks and reduced the probability of new unreconciled balances.

december 2015 – february 2018
sENIOR strategic ADVISOR, BANCO DO BRASIL – Operations UNity – teller management Team

Mapped, designed and reviewed all transactions executed by employees and clients on physical and digital channels. 
Elaborated and conducted result presentations for all executives and other major stakeholders involved on the project.
Negotiated strategic actions with executives from all involved areas.
Mapped, designed and reviewed operational processes.
Planned, negotiated and implemented actions to reduce demand for physical channels, mostly bank tellers and ATMs, and redirect them to digital channels what reduced teller transactions from 74 million/month to 45 million/month in a two-year span what represents over USD 30 million /year cost reduction only over transaction costs.
2023 – IN PROGRESS
MBA - DATA SCIENCE AND ANALYTICS, USP/ESALQ
The course aims to cultivate professionals with a solid foundation in data science and analytics, enabling them to conduct data analysis and modeling across diverse fields, including risk management, data mining, data visualization, artificial intelligence, deep learning, and more. The main language used throughout the course is R.

july 2021
training (454 hours) - data scientist foundation, data science academy
The course was composed by 6 individual courses: Machine Learning, Data Visualization and Dashboard Design, Business Analytics, Data Engineering with Hadoop and Spark, Big Data Real-time Analytics with Python and Spark and Big Data Analytics with R and Azure Machine Learning.
SEPTEMBER 2018
undergraduate degree - bachelor of philosophy, universidade do sul de santa catarina
My fascination with universal knowledge has always drawn me towards philosophy, which I consider a logical consequence of this pursuit. In my final article, I delved into the Philosophy of Music. The study of philosophy significantly enhanced my capacity for communication by improving the quality of questions I pose, ultimately sharpening my problem-solving skills.
Soft Skills
Problem-solving, adaptability, teamwork, strategic thinking, active listening and communication.
Hard Skills
R – Knowledge and experience using data analysis, ETL and artificial intelligence model training.
SQL e MySQL – Advanced knowledge and experience using SQL Server, PostgreSQL e MySQL Workbench.
Python – Knowledge and experience using data analysis, ETL and web scraping tools like Beautiful Soup and Selenium.
Power Bi – Proficient in dashboard and report design, with expertise in DAX and M language usage.
Tableau – Dashboard and report design.
HTML / CSS / Javascript – Basic knowledge for frontend and backend development and data integration.
Docker – Basic user knowledge.
English – I possess advanced English language skills at a B2/C1 level, achieved through self-study. While I can engage in conversations, I am actively seeking further training to enhance my proficiency in professional and technical environments, with a particular focus on expanding my specific vocabulary."""

job_description = """SENIOR DATA SCIENTIST - As a Data Scientist, you will balance being a prolific individual contributor to our pipelines, tables, and
models while steering the development of our products and services through the development,
maintenance, and application of data. You will help bridge the gap between Engineering & Modeling
with insights while driving the development of our data services. In addition, you will help to set the
culture, rituals, and processes that underpin a high-functioning team and the organization more
broadly.
AS A DATA SCIENTIST YOU WILL:
Build tools to manage data science modelling and development pipelines.
Development of monitoring for models and data sources; training models for validating
correctness of inputs and matching data points to companies.
Build tools to support data extraction, matching and validation from structured and unstructured
data sources.
Manage the model deployment process and support other team members as they deploy their
models post-development.
Develop testing strategies to ensure our data and models perform accurately across systems.
Support the production of new data sources (e.g. web scraping, public/private APIs,) in a
manner that minimizes development cycles while maximizing potential business applications.
Maintain a clean production environment such that the data models can be easily interpreted and
built upon by other data science and engineering team members.
Present your work, findings, and opinions to both technical and non-technical stakeholders.
WE LOOK FOR TEAMMATES WHO HAVE:
Bachelor/Master in quantitative discipline (computer science, mathematics, statistics,
economics, physics, engineering or related field).
Experience with data engineering projects such as ETL, model deployment, data validation,
feature calculation.
Familiarity with how data science teams review and validate data and machine learning models
An excellent understanding of API design, and experience designing reliable RESTful APIs.
5+ years experience with Python
Familiarity with the tradeoffs of scaling data infrastructure and database systems.
Bias to practical action and creativity using data (we value past or present projects that support
this).
1.	Build tools to manage data science modelling and development pipelines.
2.	Development of monitoring for models and data sources; training models for validating correctness of inputs and matching data points to companies.
4.	Build tools to support data extraction, matching and validation from structured and unstructured data sources.
6.	Manage the model deployment process and support other team members as they deploy their models post-development.
8.	Develop testing strategies to ensure our data and models perform accurately across systems.
9.	Support the production of new data sources (e.g. web scraping, public/private APIs,) in a manner that minimizes development cycles while maximizing potential business applications.
11.	Maintain a clean production environment such that the data models can be easily interpreted and built upon by other data science and engineering team members.
13.	Present your work, findings, and opinions to both technical and non-technical stakeholders.
14.	Experience with data engineering projects such as ETL, model deployment, data validation, feature calculation.
16.	Familiarity with how data science teams review and validate data and machine learning models
17.	An excellent understanding of API design, and experience designing reliable RESTful APIs.
18.	Familiarity with the tradeoffs of scaling data infrastructure and database systems.
19.	Bias to practical action and creativity using data (we value past or present projects that support this).
20. English fluency is a must.
"""

question = [f"1. Resume:{resume}. Job Description:{job_description}. Calculate a score 0-100 depending on the similarities between 'resume' and 'job description'",
            """2. Write and return a new version for the resume according to good practices and formal english. Instead of 'Objective' section, use a 'Profile' 
            section instead; In the 'Education' section you must put only Undergraduate, Graduate and Post Graduate studies. Any other
            courses and trainning must be put in another section like 'Further Education' or any other title you see as appropriate."""
            ]

messages = [{"role": "system",
                "content": """You are a resume reviewer. You are capable of comparing resumes and curriculum vitae with
                job descriptions. You have to verify similarities and the adequacy of the curriculum with what is required in the
                jog description; then, you will calculate a general score from 0 to 100 depending on the adequacy of the resume with 
                what is required in the job description; then you will calculate scores from 0 to 100 for each resume section of the 
                resume depending on the adequacy of that section with what is required in the job description. If there is something in
                the resume that is too little related with the job drescition, it should count as 0. When explicitly required,
                you will retrieve a new resume, reorganized and rewritten observing formality and expressions expected from a resume. """},
            {"role": "user",
             "content": """SENIOR DATA SCIENTIST - As a Data Scientist, you will balance being a prolific individual contributor to our pipelines, tables, and
models while steering the development of our products and services through the development,maintenance, and application of data. You will help bridge the gap between Engineering & Modeling
with insights while driving the development of our data services. In addition, you will help to set the culture, rituals, and processes that underpin a high-functioning team and the organization more
broadly.
AS A DATA SCIENTIST YOU WILL:
Build tools to manage data science modelling and development pipelines.
Development of monitoring for models and data sources; training models for validating
correctness of inputs and matching data points to companies.
Build tools to support data extraction, matching and validation from structured and unstructured
data sources.
Manage the model deployment process and support other team members as they deploy their
models post-development.
Develop testing strategies to ensure our data and models perform accurately across systems.
Support the production of new data sources (e.g. web scraping, public/private APIs,) in a
manner that minimizes development cycles while maximizing potential business applications.
Maintain a clean production environment such that the data models can be easily interpreted and
built upon by other data science and engineering team members.
Present your work, findings, and opinions to both technical and non-technical stakeholders.
WE LOOK FOR TEAMMATES WHO HAVE:
Bachelor/Master in quantitative discipline (computer science, mathematics, statistics,
economics, physics, engineering or related field).
Experience with data engineering projects such as ETL, model deployment, data validation,
feature calculation.
Familiarity with how data science teams review and validate data and machine learning models
An excellent understanding of API design, and experience designing reliable RESTful APIs.
5+ years experience with Python
Familiarity with the tradeoffs of scaling data infrastructure and database systems.
Bias to practical action and creativity using data (we value past or present projects that support
this).
1.	Build tools to manage data science modelling and development pipelines.
2.	Development of monitoring for models and data sources; training models for validating correctness of inputs and matching data points to companies.
4.	Build tools to support data extraction, matching and validation from structured and unstructured data sources.
6.	Manage the model deployment process and support other team members as they deploy their models post-development.
8.	Develop testing strategies to ensure our data and models perform accurately across systems.
9.	Support the production of new data sources (e.g. web scraping, public/private APIs,) in a manner that minimizes development cycles while maximizing potential business applications.
11.	Maintain a clean production environment such that the data models can be easily interpreted and built upon by other data science and engineering team members.
13.	Present your work, findings, and opinions to both technical and non-technical stakeholders.
14.	Experience with data engineering projects such as ETL, model deployment, data validation, feature calculation.
16.	Familiarity with how data science teams review and validate data and machine learning models
17.	An excellent understanding of API design, and experience designing reliable RESTful APIs.
18.	Familiarity with the tradeoffs of scaling data infrastructure and database systems.
19.	Bias to practical action and creativity using data (we value past or present projects that support this)."""},
            {"role":"assistant", 
            "content":"""Overall Score: 65/100
Education: 80/100 - The candidate holds a postgraduate degree in Science/Information Studies and has completed courses related to data analysis. However, a specific quantitative discipline (computer science, mathematics, statistics, economics, physics, engineering, or a related field) is preferred for the role of Senior Data Scientist.
Experience: 70/100 - The candidate has relevant experience in data analytics, process improvement, and project management at Banco do Brasil. The job description requires experience with data engineering projects such as ETL, model deployment, data validation, and feature calculation, which the candidate has some experience with but could be more detailed.
Skills: 60/100 - The candidate possesses skills in R language, SQL, Python, Airflow, and other tools relevant to data science. However, the job description emphasizes experience with Python, API design, and scaling data infrastructure, which could be elaborated on in the resume.
Language: 100/100 - The candidate has listed English as an advanced language proficiency, despite the job description does not require english, the job description is written in english and language knowledges are a valuable asset. Additional languages such as Spanish and French are a plus.
Other Activities: 0/100 - While the candidate's involvement in producing coloring books related to Yoruba religion is commendable, it is not directly relevant to the role of Senior Data Scientist.
Recommendations:
1. Highlight specific projects related to data engineering, model deployment, and data validation to align more closely with the job description.
2. Emphasize experience with Python, API design, and scaling data infrastructure.
3. Provide more details on how past projects demonstrate a bias to practical action and creativity using data.
4. Consider removing or minimizing the section related to producing coloring books, as it may not be directly relevant to the position.
A revised version of the resume will be provided to enhance alignment with the job description."""}]
    
