# Intro to databases

## storing data

1. memory
    - memory will be cleared on every boot/program start.
2. disk
    - for persistance.

## disk storage
-   plain text file
-   structured text file
    - json
    - csv
    - xml
    - ini
    - svg (for images, xml file)
- binary file (cant be interpretated if we dont have the decoder, program doesnt know how to read the data)
    - images
    - audio
    - videos

    ```ini
    ini eg.
    ;this is a comment
    [database]
    driver = mysql
    host = localhost
    port = 2206
    databasename = persondb
    [user]
    username = zeke

    ```
    ```xml
    xml eg.
    <?xml version="1.1" encoding="UTF-8" ?>

    <persons>

        <person>
            <firstname>Matt</firstname>
            <lastname>River</lastname>
            <age>20</age>
        </person>

        <person>
            <firstname>Mary</firstname>
            <lastname>Jones</lastname>
            <age>30</age>
        </person>

    </persons>

    ```

    ```svg
    svg eg.
        <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="200" height="200">
        <rect
            x="2"
            y="2"
            width="196"
            height="196"
            fill="lime"
            stroke-width="4"
            stroke="pink"
          />
        <circle cx="100" cy="100" r="75" fill="orange" />
        </svg>
    ```

    ## Databases 

    includes database handling programs such as manipulating database structure and user etc

    - relational databases
        - sql lang
    - non-relational databases (mongoDb)
        - no sql lang

    ## Datastorage usage

    'client application'
        |
        | (API)
        | 
    'datastorage layer' 
        |
        | (API, SQL)
        |            
    'database engine' 
        |
        | (API, write/read disc)
        |         
    'disk storage' 

    ### Verssion 2 with different storage engine

    'client application'
        |
        | (API)
        |
    'datastorage layer' 
        |
        | (API, SQL)
        |
    'our own dataengine' 
        |
        | (API, write/read disc)
        |
    'disk storage' (API, write/read disc)


## Relational model 

**table: "person"**

id|firstname|lastname|age
:---:|---|---|:---:
1|'Matt|'River'|20
2|'Mary'|'Smith'|30
3|'Mary|'Smith'|10

**table: "computer"**

id|name|price
:---:|---|---:
1|'Brain I'|200
2|'Blast X200 GT'|900


**table: "person_has_computer"**

personid|computerid
:---:|:---:
1|1
1|2
2|1

## Create statement for tables

```sql
CREATE table person (
    id integer primary key, 
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    age integer
);

CREATE table computer (
    id integer primary key, 
    name varchar(50) not null,
    price integer
);

CREATE table person_has_computer (
    personid integer not null,
    computerid integer not null
    primary key(personid, computerid), 
    salary decimal(6,2),
    foreign key personid references perdon(id),
    foreign key computerid references computer(id)
    
);

```