## Template Generator

This is a simple template generator witch works based on a **json** file.

The **JSON** file have some variables wich are replaced on the template based on delimiters, also defined on the **JSON** file

All you need is a meta.json file and the main.py script, once you have both of them you can create you own scripts.

- Required Fields
    - Config
        - input
        - output
        - separator

All the other fields are optionals, you can use all other keywords there in UPPER_CASE form e.g first_name FIRST_NAME,
delimited by the separators e.g separator = {} first_name = 'jhon doe' use on the template {FIRST_NAME}. Just simple as that