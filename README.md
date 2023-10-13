# Parking Lot Tracker

Latest python version is used

### Get Start

1. Clone the git repository
```bash
git clone https://github.com/Kalyanasundaram-J/parking-lot.git
```

2. Change the current directory to cloned project directory
```bash
cd parking-lot
```
3. Run the project
```bash
python main.py
```
Setup is completed ....

### Use Case

1. To add new level to parking lot use
    ```
    add <level name> <total spot> <spot start number (optional)>
    ```
    - Eg: 
        ```
        add A 20 1
        ```
2. Assign parking space to new vehicle
    ```
    <vehicle number>
    ```
    - Eg:
        ```
        AB12CD3456
        ```
3. Retrieve parking spot number of particular vehicle
    ```
    s <vehicle number>
    ```
    - Eg:
        ```
        s AB12CD3456
        ```
4. Deallocate assigned parking space
    ```
    rm <vehicle number>
    ```
    - Eg:
        ```
        rm AB12CD3456
        ```
5. To show all the information about parking lot
    ```
    info
    ```
6. To exit from the terminal application
    ```
    exit
    ```
    ```
    Y
    ```
