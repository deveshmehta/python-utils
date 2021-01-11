# python-utils

* This will query the meta data of an instance within aws and provide a json formatted output. 

    Usage
    ```
    python metadata2json.py
    ```

* This allows for a particular data key to be retrieved individually

    Usage 
    ```
    python metadata2json-with-keys.py --key meta-data/instance-type
    ```

* A nested object function allows you to pass in the object and a key and get back the value. 
    ```
    Example Inputs
    object = {“a”:{“b”:{“c”:”d”}}}
    key = a/b/c
    
    object = {“x”:{“y”:{“z”:”a”}}}
    key = x/y/z
    value = a
    ```
    Usage 
    ```
    python3 nested-object.py \
            --object {"x":{"y":{"z":"a"}}} \
            --key x/y/z
    ```