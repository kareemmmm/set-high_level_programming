# SET High Level Programming

This repository contains back-end Python projects covering Object-Relational Mapping (ORM) with MySQL and SQLAlchemy, low-level HTTP networking with `cURL`, and RESTful API interactions using Python's native `urllib` and `requests` library.

---

## 📚 Projects Overview

| Directory | Topic / Focus | Core Technologies |
| :--- | :--- | :--- |
| **`python-object_relational_mapping/`** | Database querying, SQL Injection prevention, ORM modeling | Python, MySQLdb, SQLAlchemy, MySQL |
| **`python-network_0/`** | HTTP requests, header inspection, $O(\log n)$ peak-finding algorithm | Bash, cURL, Python 3 |
| **`python-network_1/`** | Fetching URL status, sending POST data, handling HTTP errors & REST APIs | Python 3, `urllib`, `requests`, GitHub API |

---

## 🛠️ Project Details & Executables

### 1. Object-Relational Mapping (`python-object_relational_mapping/`)
Focuses on connecting Python applications to MySQL databases, migrating raw SQL queries to SQLAlchemy ORM models, and handling object relationships (one-to-many, cascading deletes).

* **MySQLdb Scripts:** `0-select_states.py`, `1-filter_states.py`, `2-my_filter_states.py`, `3-my_safe_filter_states.py`, `4-cities_by_state.py`, `5-filter_cities.py`
* **SQLAlchemy Models:** `model_state.py`, `model_city.py`, `relationship_state.py`, `relationship_city.py`
* **ORM Operations:** `7-model_state_fetch_all.py` through `13-model_state_delete_a.py`, `14-model_city_fetch_by_state.py`, `100-relationship_states_cities.py`–`102-relationship_cities_states_list.py`

### 2. Network Fundamentals #0 (`python-network_0/`)
Covers HTTP methods (GET, POST, DELETE, OPTIONS), header inspection, status code extraction, and algorithm optimization.

* **Bash & cURL Utilities:** `0-body_size.sh`, `1-body.sh`, `2-delete.sh`, `3-methods.sh`, `4-header.sh`, `5-post_params.sh`, `100-status_code.sh`, `101-post_json.sh`, `102-catch_me.sh`
* **Algorithms:** `6-peak.py` ($O(\log n)$ binary search peak-finder) and `6-peak.txt`

### 3. Network Fundamentals #1 (`python-network_1/`)
Covers programmatic HTTP interactions in Python using both low-level (`urllib`) and high-level (`requests`) libraries, including authentication and API integrations.

* **Native `urllib` Scripts:** `0-hbtn_status.py`, `1-hbtn_header.py`, `2-post_email.py`, `3-error_code.py`
* **`requests` Library Scripts:** `4-hbtn_status.py`, `5-hbtn_header.py`, `6-post_email.py`, `7-error_code.py`, `8-json_api.py`
* **API Integrations:** `10-my_github.py` (Basic Auth with Personal Access Tokens), `100-github_commits.py` (Fetching commit history via GitHub API)

---

## 💻 Environment & Requirements

* **OS:** CentOS / Ubuntu Linux
* **Language:** Python 3.8+
* **Database:** MySQL 8.0 / MariaDB
* **Python Libraries Required:**
  ```bash
  pip install mysqlclient sqlalchemy requests
