## AirBnB Clone V2 - Flask Web Framework Tasks

This repository contains tasks related to creating web interfaces using Flask for the AirBnB clone V2 project.

### Repository Information:
**GitHub repository:** holbertonschool-AirBnB_clone_v2

### Requirements:

- Python 3.x
- Flask
- MySQL

### Set Up:
Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository. Ensure all tables are created with:

```bash
echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

### Tasks:

**0-5:** Initial tasks to set up Flask and create basic routes.

**6. Odd or Even?**
- Set up Flask to run on `0.0.0.0` port `5000`
- Create routes to display messages and perform simple checks
  - Display if a number is odd or even through a dynamic route
- Repository files: `web_flask/6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html`

**7. Improve Engines**
- Update the storage engines and models
- Implement the close method in the engines
- Implement getter method `cities` in the State model
- Repository files: `models/engine/file_storage.py`, `models/engine/db_storage.py`, `models/state.py`

**8. List of States**
- Create a route `/states_list` that displays a list of all states in storage.
- Use the `strict_slashes=False` option in your route definition.
- Repository files: `web_flask/7-states_list.py`, `web_flask/templates/7-states_list.html`

**9. Cities by States**
- Create a route `/cities_by_states` that displays a list of all states and their associated cities.
- Utilize the `cities` relationship or public getter method based on the storage engine.
- Repository files: `web_flask/8-cities_by_states.py`, `web_flask/templates/8-cities_by_states.html`

**10. States and State**
- Create two routes:
  1. `/states` to display all states.
  2. `/states/<id>` to display a specific state and its cities. If the state doesn't exist, display "Not found!".
- Repository files: `web_flask/9-states.py`, `web_flask/templates/9-states.html`

### Testing:

Most tasks are accompanied by testing commands using `curl`. For example, for task 6:

```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
```

The expected output is an HTML that displays whether the number 89 is odd or even.
