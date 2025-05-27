# Mobile-Device-Usage-and-User-Behavior
Analyzes mobile device user behavior based on application usage data, operating system (Android/iOS), age, and daily data consumption. The goal is to understand user usage patterns and preferences to support more effective business decision making and marketing strategies.

## Repository Outline
```
P2M3/Maulana-Yusuf-T
│
├── airflow_ES.yaml
├── P2M3_Maulana_Yusuf_ddl.txt
├── P2M3_Maulana_Yusuf_DAG_Graph.jpg
├── P2M3_Maulana_Yusuf_conceptual.txt
├── P2M3_Maulana_Yusuf_GX.ipynb
├── README.md
├── .gitignore
├── .env
│
├── /dags
│   └── P2M3_Maulana_Yusuf_DAG.py
│
├── /data
│   └── P2M3_Maulana_Yusuf_data_clean.csv
|   └── P2M3_Maulana_Yusuf_data_raw.csv
│
├── /images
│   ├── Introduction & Objective.png
│   ├── Plot & Insight 01.png
│   ├── Plot & Insight 02.png
│   ├── Plot & Insight 03.png
│   ├── Plot & Insight 04.png
│   ├── Plot & Insight 05.png
│   ├── Plot & Insight 06.png
│   └── Conclusion & Recommendations.png

```

**Content of this project**:
1. **`README.md`** - General description about the project.<br>
2. **`P2M3_Maulana_Yusuf_GX.ipynb`** - The main notebook contains the data exploration process, data validation using Great Expectations, data visualization, and conclusions from the analysis results.<br>
3. **`P2M3_Maulana_Yusuf_ddl.txt`** - Contains Data Definition Language (DDL) which describes the structure of database tables such as column names, data types, and relationships between tables.<br>
4. **`P2M3_Maulana_Yusuf_conceptual.txt`** - Describes the conceptual design of a database in the form of relationships between entities, including the main entity and its attributes.<br>
5. **`/dags`** - Contains DAG (Directed Acyclic Graph) files used by Apache Airflow to automatically orchestrate ETL workflows.<br>
6. **`/data`** - Contains raw datasets and transformed results (cleaned) used in ETL and analysis processes.
7. **`/images`** - Contains visual images such as insight graphs, plots, and supporting illustrations such as diagrams and conclusions.<p>

## Problem Background
In recent years, there has been a dramatic shift in the way individuals consume digital content, especially with relation to mobile devices.  Because smartphone use is increasing, a broad variety of applications are easily accessible, and content can be customized, mobile devices are becoming the main platform for media consumption and other digital activities.  However, companies that sell digital products and information still have trouble understanding the habits and preferences of their customers.  A thorough grasp of mobile user behavior is essential for product development, marketing, and sales tactics.

## Project Output
1. **Data Validation with Great Expectations**:<br>
The **`P2M3_Maulana_Yusuf_GX.ipynb`** notebook contains the data validation process using Great Expectations, including the configuration and validation results of several types of expectations to ensure data quality before use.
2. **Concept and Pipeline Documentation**:<br>
a) **`P2M3_Maulana_Yusuf_conceptual.txt`**: Explanation of the data pipeline concept that was built.<br>
b) **`P2M3_Maulana_Yusuf_ddl.txt`**: Documentation of table/data structure (data definition language).>br
c) **`airflow_ES.yaml`**: Configuration for integration with Elasticsearch using Airflow.<p>
3. **Data Pipeline with Apache Airflow**:<br>
a) **`dags/`** folder: Contains DAG (Directed Acyclic Graph) to schedule and organize data processing flow.<br>
b) **`P2M3_Maulana_Yusuf_DAG_Graph.jpg`**: Visualization of the pipeline flow executed by Airflow.<p>
4. **Visualisation and Insight**:<br>
**Images/ folder**: Stores visualization images and insights generated from the data, including:<br>
    a) Operating system usage analysis.<br>
    b) Age distribution and number of applications.<br>
    c) Other insights depicted in graphical form.<p>
5. **Conclusion and Recommendations**: <br>
Listed in the notebook and the **`Conclusion & Recommendations.png`** image, it explains the final results of the analysis and the suggested strategies based on the data findings.

## Data
The dataset used in this project is the **Mobile Device Usage and User Behavior Dataset** obtained from [Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset/data). This dataset contains 700 user data that include measures like data use, battery depletion, screen-on time, and app usage time.  In order to facilitate meaningful analysis and modeling, each entry is divided into one of five user behavior classes, ranging from light to extreme usage.

General data characteristics:
- Number of rows: **`700`** rows of data.
- Number of columns: **`11`** features.<p>

The features consist of a combination of numeric and categorical data and no missing values ​​and duplicated data.

## Method
1. **`ETL Pipeline with Apache Airflow`**:<br>
a) Using DAG (Directed Acyclic Graph) to schedule and manage Extract, Transform, Load (ETL) processes.<br>
b) The dags/ file contains the DAG script, while P2M3_Maulana_Yusuf_DAG_Graph.jpg illustrates the task flow visually.<p>

2. **`Data Validation with Great Expectations (GX)`**:<br>
a) Validate data quality through various expectations, such as:<br>
a.1) **`expect_column_values_to_not_be_null`**.<br>
a.2) **`expect_column_values_to_be_between`**.<br>
a.3) **`expect_column_values_to_match_regex`**.<br>
a.4) **`expect_column_values_to_be_unique`**.<br>
a.5) **and many more**.<br>
b) All processes are recorded in **`P2M3_Maulana_Yusuf_GX.ipynb`**.

3. **`Elasticsearch Integration`**:<p>
a) ETL output data is loaded into Elasticsearch for visualization and fast searching.
b) Integration configuration is managed through the **`airflow_ES.yaml`** file.

4. **`Data Visualization and Analysis`**:<br>
Using **Kibana** to create graphs and visual explorations:
    a) Age distribution vs number of apps.
    b) Data usage comparison between Android and iOS.
    c)Visualizations are stored in the **`images/`** folder.

5. **`Conceptual and Technical Documentation`**:<br>
a) **`P2M3_Maulana_Yusuf_conceptual.txt`**: Explanation of the workflow and concept of the ETL pipeline.
b) **`P2M3_Maulana_Yusuf_ddl.txt`**: Provides data structures as technical references.

## Stacks
Stack and tools used in this project include:
- **`Programming Language`**: Python 3

**`Libraries`**:
1. **`Pandas`** – For data manipulation
2. **`SQLAlchemy`** – Fetching data from the database to be validated with Great Expectations or sent to Elasticsearch.
3. **`AirFlow`** – Compiling ETL workflows with DAG (Directed Acyclic Graph).
4. **`ElasticSearch`** – Validated data will be sent to Elasticsearch so that it can be visualized in Kibana.
5. **`Great Expectations (GX)`** - Python library for performing data quality validation (with Jupyter Notebook).

**`Tools`**:
1. **Jupyter Notebook** – for exploration of Great-Expectations.
2. **Visual Studio Code** – for writing **`.py`** files.
3. **GitHub** – for version control and collaboration.

---

**Additional References:**
- [Great Expectations documentation](https://docs.greatexpectations.io/docs/home/)
- [Apache AirFlow Documentation](https://airflow.apache.org/docs/)
